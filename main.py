# Azure Databricks Data Engineering Project
# Author: Sangam Srivastav 
# Description: Enhanced pipeline with insights & quality monitoring

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from delta.tables import DeltaTable
import pandas as pd

# ========================== 1. CONNECTION SETUP ==========================

def setup_adls_connection():
    try:
        storage_account = "mydatalake2004"
        container = "transaction-data"
        access_key = dbutils.secrets.get(scope="azure-storage", key="storage-access-key")
        spark.conf.set(f"fs.azure.account.key.{storage_account}.dfs.core.windows.net", access_key)
        print("✅ ADLS connection successful.")
        return storage_account, container
    except Exception as e:
        print(f"❌ Failed to connect to ADLS: {e}")
        return None, None

def verify_files_exist(account, container):
    try:
        base_path = f"abfss://{container}@{account}.dfs.core.windows.net/"
        files = dbutils.fs.ls(base_path)
        for file in files:
            print(f"📄 {file.name} - {file.size} bytes")
        return [f.name for f in files]
    except Exception as e:
        print(f"❌ Could not list files: {e}")
        return []

# ========================== 2. DATA LOADING ==========================

def load_csv(file_path, file_name):
    try:
        print(f"📥 Loading {file_name}...")
        df = spark.read.option("header", "true").option("inferSchema", "true").csv(file_path)
        print(f"✅ Loaded {df.count()} rows with {len(df.columns)} columns from {file_name}")
        df.show(5)
        return df
    except Exception as e:
        print(f"❌ Error reading {file_name}: {e}")
        return None

def load_transaction_data(account, container):
    path = f"abfss://{container}@{account}.dfs.core.windows.net/"
    return load_csv(path + "transactions.csv", "transactions"), load_csv(path + "products.csv", "products")

# ========================== 3. DATA CLEANING ==========================

def clean_data(df, name):
    try:
        print(f"🧹 Cleaning {name} data")
        df = df.dropna(how="all").dropDuplicates()
        df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).show()
        return df
    except Exception as e:
        print(f"❌ Error cleaning {name}: {e}")
        return df

def add_quality_flags(df):
    return df.withColumn("data_quality_score", when(col("transaction_id").isNull(), 0.0).otherwise(1.0))\
             .withColumn("processed_at", current_timestamp())\
             .withColumn("record_hash", hash(*[col(c) for c in df.columns]))

# ========================== 4. CHANNEL ENRICHMENT ==========================

def enrich_channels(df):
    return df.withColumn("channel", 
                         when(col("transaction_id").rlike("^WEB"), "web")
                        .when(col("transaction_id").rlike("^MOB"), "mobile")
                        .otherwise("in-store"))

# ========================== 5. ANALYTICS & INSIGHTS ==========================

def generate_analytics(transactions, products):
    joined = transactions.join(products, "product_id", "left")

    customer_df = joined.groupBy("customer_id").agg(
        count("transaction_id").alias("transactions"),
        sum(col("quantity") * col("price")).alias("revenue")
    ).withColumn("avg_order_value", col("revenue") / col("transactions"))

    product_df = joined.groupBy("product_id").agg(
        sum("quantity").alias("sold"),
        sum(col("quantity") * col("price")).alias("revenue")
    )

    category_df = joined.groupBy("category").agg(
        sum("quantity").alias("units_sold"),
        sum(col("quantity") * col("price")).alias("category_revenue")
    )

    campaign_df = joined.groupBy("campaign_id").agg(
        count("*").alias("transactions"),
        sum(col("quantity") * col("price")).alias("campaign_revenue"),
        countDistinct("customer_id").alias("unique_customers")
    )

    # Outlier detection on revenue
    revenue_stats = customer_df.select(mean("revenue").alias("mean"), stddev("revenue").alias("std")).collect()[0]
    mean_val, std_val = revenue_stats["mean"], revenue_stats["std"]
    customer_df = customer_df.withColumn(
        "is_outlier", (col("revenue") > (mean_val + 3 * std_val)) | (col("revenue") < (mean_val - 3 * std_val))
    )

    return joined, customer_df, product_df, category_df, campaign_df

# ========================== 6. DELTA LAKE ==========================

def create_delta_table(df, table_name, db="analytics_db"):
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {db}")
    df.write.format("delta").mode("overwrite").saveAsTable(f"{db}.{table_name}")
    print(f"✅ Created table: {db}.{table_name}")

def optimize_table(table):
    spark.sql(f"OPTIMIZE {table} ZORDER BY (customer_id)")
    spark.sql(f"VACUUM {table} RETAIN 168 HOURS")

def create_data_quality_table(df):
    null_summary = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])
    null_summary = null_summary.withColumn("total_rows", lit(df.count()))
    create_delta_table(null_summary, "data_quality_summary")

# ========================== 7. PIPELINE EXECUTION ==========================

def execute_pipeline():
    print("🚀 Executing Data Engineering Pipeline")
    account, container = setup_adls_connection()
    if not account: return

    if not verify_files_exist(account, container): return

    tx_df, pr_df = load_transaction_data(account, container)
    tx_df, pr_df = clean_data(tx_df, "transactions"), clean_data(pr_df, "products")
    tx_df, pr_df = add_quality_flags(tx_df), add_quality_flags(pr_df)
    tx_df = enrich_channels(tx_df)

    joined, cust_df, prod_df, cat_df, camp_df = generate_analytics(tx_df, pr_df)

    create_delta_table(joined, "transactions_insights")
    create_delta_table(cust_df, "customer_analytics")
    create_delta_table(prod_df, "product_analytics")
    create_delta_table(cat_df, "category_analytics")
    create_delta_table(camp_df, "campaign_analytics")
    create_data_quality_table(tx_df)

    optimize_table("analytics_db.transactions_insights")
    print("🎉 Pipeline execution complete.")

# ========================== 8. MAIN ==========================

if __name__ == "__main__":
    execute_pipeline()
