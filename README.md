# 🚀 Azure Transaction Analytics Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.4+-orange.svg)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-2.4.0+-green.svg)](https://delta.io/)
[![Azure](https://img.shields.io/badge/Azure-Data%20Lake%20Gen2-blue.svg)](https://azure.microsoft.com/en-us/services/storage/data-lake-storage/)

A powerful data engineering pipeline for analyzing multi-channel transaction data (web, mobile, in-store) using Azure Databricks, Delta Lake, and Azure Data Lake Storage Gen2. Unlock insights into customer behavior, product performance, and marketing campaign success with a scalable, robust solution.

## 🌟 Why This Project?

This platform processes large-scale transaction data, delivering actionable insights for businesses. Built with Apache Spark and Delta Lake, it ensures fast processing, reliable storage, and high data quality. Whether you're analyzing sales trends or campaign ROI, this pipeline has you covered.

## ✨ Key Features

* **Multi-Channel Analytics**: Combines web, mobile, and in-store data
* **Actionable Insights**: Tracks customer spending, top products, and campaign performance
* **Data Quality**: Detects missing values and outliers for clean data
* **Scalable Processing**: Handles big data with Spark's distributed computing
* **Delta Lake Storage**: Optimized storage with ACID transactions and time travel
* **Modular Code**: Reusable, maintainable Python modules
* **Error Handling**: Robust validation for reliable execution

## 🏗️ Architecture

```
┌──────────────┐    ┌──────────────┐    ┌─────────────────┐
│ Data Sources │───▶│ ADLS Gen2    │───▶│ Azure Databricks │
│ • Web        │    │ • CSV Files  │    │ • Load & Clean  │
│ • Mobile     │    │ • Delta Tables│    │ • Analytics     │
│ • In-Store   │    └──────────────┘    │ • Delta Storage │
└──────────────┘                        └─────────────────┘
```

## 📋 Prerequisites

### Azure Subscription:
* Azure Data Lake Storage Gen2
* Azure Databricks workspace

### Databricks Cluster:
* Spark 3.4+
* Delta Lake 2.4.0 (io.delta:delta-core_2.12:2.4.0)
* Python 3.8+

### ADLS Gen2 Setup:
* Secret scope: azure-storage with storage-access-key
* Data files: transactions/*.csv and products.csv

## 🚀 Get Started

### 1. Clone the Repository

```bash
[git clone https://github.com/Sangam919/Final-Project.git](https://github.com/Sangam919/Final-Project-Pyspark-problem-statement-.git)
cd azure-transaction-analytics
```

### 2. Set Up ADLS Credentials

Create a secret scope in Databricks:

```bash
databricks secrets create-scope --scope azure-storage
databricks secrets put --scope azure-storage --key storage-access-key
```

Update src/config.py with your storage account and container (default: mydatalake2004, transaction-data).

### 3. Prepare Data in ADLS Gen2

Ensure your container has:

```
/transaction-data/
├── transactions/
│   ├── transaction_1.csv
│   ├── transaction_2.csv
│   └── ...
└── products.csv
```

### 4. Run in Databricks

1. Import the repository to Databricks using Repos
2. Create a cluster (see Configuration below)
3. Run the pipeline:

```python
%run /Repos/<your-repo>/src/pipeline.py
```

## 📊 Data Schema

### Transactions (transactions/*.csv)

| Column | Type | Description |
|--------|------|-------------|
| transaction_id | String | Unique transaction ID |
| customer_id | String | Unique customer ID |
| product_id | String | Product ID |
| quantity | Integer | Units purchased |
| price | Double | Unit price |
| transaction_date | Timestamp | Date and time of transaction |
| campaign_id | String | Marketing campaign ID |

### Products (products.csv)

| Column | Type | Description |
|--------|------|-------------|
| product_id | String | Unique product ID |
| description | String | Product description |
| category | String | Product category |
| unit_price | Double | Unit price |

## 🔧 Configuration

### Databricks Cluster

```json
{
  "spark_version": "14.3.x-scala2.12",
  "node_type_id": "Standard_DS3_v2",
  "num_workers": 2,
  "spark_conf": {
    "spark.jars.packages": "io.delta:delta-core_2.12:2.4.0",
    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog"
  }
}
```

### Project Structure

```
├── src/
│   ├── __init__.py       # Python package initializer
│   ├── config.py         # ADLS connection setup
│   ├── data_loader.py    # Loads CSV data
│   ├── data_cleaner.py   # Cleans and validates data
│   ├── analytics.py      # Generates insights
│   ├── delta_utils.py    # Manages Delta tables
│   ├── pipeline.py       # Orchestrates pipeline
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
├── LICENSE               # MIT License
```

## 📈 Analytics Outputs

### Customer Analytics:
* Average order value
* Total revenue and transactions
* Revenue outlier detection

### Product Analytics:
* Top products by sales and revenue
* Product details (description)

### Category Analytics:
* Category sales and revenue

### Campaign Analytics:
* Campaign revenue, transactions, and unique customers

### Data Quality:
* Null value reports
* Outlier detection for quantity, price, and revenue
* Quality metrics in analytics_db.data_quality_summary

## 🏃‍♂️ Run the Pipeline

In a Databricks notebook:

```python
%run /Repos/<your-repo>/src/pipeline.py
```

Query results:

```sql
SELECT * FROM analytics_db.customer_analytics LIMIT 5;
SELECT * FROM analytics_db.data_quality_summary;
```

## 🛠️ Extend the Project

* **Add Features**: Enhance analytics.py for time-series or segmentation
* **Improve Quality**: Add more checks in data_cleaner.py
* **Automate**: Schedule with Databricks Workflows
* **Visualize**: Create dashboards in Databricks or Power BI

## 📜 License

MIT License - Copyright (c) 2025 Sangam Srivastav

## 🙌 Acknowledgments

* **Author**: Sangam Srivastav
* **Tech Stack**: Apache Spark, Delta Lake, Azure Databricks
* **Inspiration**: Modern data engineering for scalable analytics
