🚀 Azure Transaction Analytics Platform

A scalable, enterprise-grade data engineering pipeline for analyzing multi-channel transaction data using Azure Databricks, Delta Lake, and Azure Data Lake Storage Gen2. This platform provides actionable insights into customer behavior, product performance, and marketing campaign effectiveness.
🎯 Overview
The Azure Transaction Analytics Platform processes large-scale transaction data from web, mobile, and in-store channels, stored in ADLS Gen2. Built with Apache Spark and Delta Lake, it ensures efficient data processing, robust data quality monitoring, and optimized storage. The pipeline generates insights such as average order value per customer, popular products and categories, and campaign performance, storing results in managed Delta tables for downstream analytics.
Key Features

Multi-Channel Data Integration: Combines transaction data from web, mobile, and in-store channels.
Advanced Analytics: Insights into customer behavior, product performance, and campaign ROI.
Data Quality Monitoring: Detects missing values, outliers, and ensures data consistency.
Scalable Processing: Leverages Apache Spark for high-performance data processing.
Delta Lake Storage: Supports ACID transactions, time travel, and optimized storage.
Modular Codebase: Reusable functions for maintainability and extensibility.
Error Handling: Robust validation and error management for reliable execution.

🏗️ Architecture
┌───────────────────────────┐    ┌────────────────────────┐    ┌──────────────────────┐
│       Data Sources        │    │    Azure ADLS Gen2     │    │  Azure Databricks    │
│                           │    │                        │    │                      │
│  • Web Transactions       ├──▶│  • transactions/*.csv  │───▶│  • Data Loading      │
│  • Mobile Transactions    │    │  • products.csv        │    │  • Cleaning          │
│  • In-Store Transactions  │    │  • Delta Tables        │    │  • Analytics         │
└───────────────────────────┘    └────────────────────────┘    │  • Quality Monitoring│
                                                              │  • Delta Storage     │
                                                              └──────────────────────┘

📋 Prerequisites

Azure Subscription with:
Azure Data Lake Storage Gen2
Azure Databricks workspace


Databricks Cluster with:
Apache Spark 3.4+
Delta Lake 2.4.0 (io.delta:delta-core_2.12:2.4.0)
Python 3.8+


ADLS Gen2 Configuration:
Secret scope (azure-storage) with storage-access-key
Transaction data in transactions/*.csv and product data in products.csv



🚀 Quick Start
1. Clone the Repository
git clone https://github.com/Sangam919/Final-Project.git
cd azure-transaction-analytics

2. Configure ADLS Gen2 Credentials
Set up a Databricks secret scope:
databricks secrets create-scope --scope azure-storage
databricks secrets put --scope azure-storage --key storage-access-key

Update src/config.py with your ADLS Gen2 storage account and container names (default: mydatalake2004, transaction-data).
3. Upload Data to ADLS Gen2
Ensure your ADLS Gen2 container has:
/transaction-data/
├── transactions/
│   ├── transaction_1.csv
│   ├── transaction_2.csv
│   └── ...
└── products.csv

4. Deploy on Databricks

Import the repository into your Databricks workspace using Repos.
Create a cluster with Delta Lake support (see Configuration below).
Run the pipeline in a notebook:%run /Repos/<your-repo>/src/pipeline.py



📊 Data Schema
Transaction Data (transactions/*.csv)



Column
Type
Description



transaction_id
String
Unique transaction identifier


customer_id
String
Unique customer ID


product_id
String
Product involved in transaction


quantity
Integer
Number of units purchased


price
Double
Unit price


transaction_date
Timestamp
Transaction date and time


campaign_id
String
Marketing campaign identifier


Product Data (products.csv)



Column
Type
Description



product_id
String
Unique product identifier


description
String
Product description


category
String
Product category


unit_price
Double
Unit price


🔧 Configuration
Databricks Cluster
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

Directory Structure
├── src/
│   ├── __init__.py           # Makes src a Python package
│   ├── config.py             # ADLS connection and file verification
│   ├── data_loader.py        # Data loading with predefined schemas
│   ├── data_cleaner.py       # Data cleaning and quality checks
│   ├── analytics.py          # Analytics and insights generation
│   ├── delta_utils.py        # Delta Lake operations
│   ├── pipeline.py           # Main pipeline orchestration
├── README.md                 # Project documentation
├── .gitignore                # Git ignore file

📊 Analytics Features
Customer Analytics

Average order value per customer
Total revenue and transaction count per customer
Outlier detection for customer revenue

Product Analytics

Top-selling products by quantity and revenue
Product performance by description

Category Analytics

Category performance by units sold and revenue

Marketing Campaign Analysis

Campaign revenue and transaction count
Unique customers per campaign

Data Quality Monitoring

Missing value detection and reporting
Outlier detection for quantity, price, and revenue
Data quality scoring and metadata tracking
Persistent quality metrics in data_quality_summary Delta table

🏃‍♂️ Usage Example
Run the pipeline in a Databricks notebook:
%run /Repos/<your-repo>/src/pipeline.py

This executes the full pipeline, which:

Connects to ADLS Gen2
Loads transaction and product data
Cleans and enriches data with channel information
Generates analytics
Saves results to Delta tables in analytics_db
Optimizes storage and monitors data quality

Query the results in Databricks:
SELECT * FROM analytics_db.customer_analytics LIMIT 5;
SELECT * FROM analytics_db.data_quality_summary;

🛠️ Development
Adding New Features

Extend analytics.py for additional insights (e.g., time-series analysis).
Update data_cleaner.py for new quality checks.
Modify pipeline.py to include new steps.

Testing

Test each module (config.py, data_loader.py, etc.) in a Databricks notebook.
Use sample data to validate analytics output.

📈 Future Improvements

Add unit tests for each module using pytest.
Implement incremental data loading for streaming updates.
Schedule the pipeline using Databricks Workflows.
Integrate visualizations with Databricks Dashboards or Power BI.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙌 Acknowledgments

Built with ❤️ by Sangam Srivastav
Powered by Apache Spark, Delta Lake, and Azure Databricks
