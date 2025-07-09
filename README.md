# 🚀 Azure Transaction Analytics Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.0+-orange.svg)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-2.0+-green.svg)](https://delta.io/)
[![Azure](https://img.shields.io/badge/Azure-Data%20Lake%20Gen2-blue.svg)](https://azure.microsoft.com/en-us/services/storage/data-lake-storage/)

A comprehensive enterprise-grade solution for analyzing multi-channel transaction data using Azure Databricks, Delta Lake, and Azure Data Lake Storage Gen2. This platform provides real-time insights into customer behavior, product performance, and marketing campaign effectiveness.

## 🎯 Overview

The Azure Transaction Analytics Platform is designed to handle large-scale transaction data from multiple channels (web, mobile, in-store) and provide actionable business insights. Built with modern data engineering best practices, it leverages the power of Apache Spark and Delta Lake for efficient data processing and storage.

### Key Features

* **Multi-Channel Data Integration**: Seamlessly combines transaction data from web, mobile, and in-store channels
* **Real-Time Analytics**: Provides instant insights into customer behavior and sales performance
* **Data Quality Monitoring**: Comprehensive data validation and quality assessment
* **Scalable Architecture**: Built on Apache Spark for handling large datasets
* **Delta Lake Integration**: ACID transactions and time travel capabilities
* **Marketing Campaign Analysis**: Detailed ROI analysis for marketing campaigns
* **Customer Segmentation**: Advanced customer analytics and segmentation

## 🏗️ Architecture

```
┌───────────────────────────┐    ┌────────────────────────┐    ┌──────────────────────┐
│   Data Sources  │    │   Azure ADLS     │    │ Azure Databricks│
│                 │    │     Gen2         │    │                 │
│  • Web Store    ├──▶│                  │───▶│  • Data Loading │
│  • Mobile App   │    │  • Raw Data      │    │  • Processing   │
│  • In-Store POS │    │  • Processed     │    │  • Analytics    │
└──────────────────────┘    │  • Delta Tables  │    │  • Validation   │
                        └──────────────────┘    └──────────────────┘
                                 ▲                        │
                                 │                        │
                                 └──────────────────────────────────────┘
                                     Delta Lake Storage
```

## 📋 Prerequisites

* **Azure Subscription** with access to:

  * Azure Data Lake Storage Gen2
  * Azure Databricks
* **Python 3.8+**
* **Apache Spark 3.0+**
* **Delta Lake 2.0+**

## 🚀 Quick Start

### 1. Clone the Repository

```bash
https://github.com/Sangam919/Final-Project.git
cd azure-transaction-analytics
```

### 2. Set Up Environment Variables

Create a `.env` file:

```bash
AZURE_STORAGE_ACCOUNT_NAME=your_storage_account
AZURE_STORAGE_ACCESS_KEY=your_access_key
AZURE_CONTAINER_NAME=your_container_name
```

### 3. Upload Sample Data

```
/your-container/
├── transactions/
│   ├── web_transactions.csv
│   ├── mobile_transactions.csv
│   └── in-store_transactions.csv
└── products/
    └── product_info.csv
```

### 4. Deploy on Databricks

* Create a cluster with Delta Lake support
* Upload and run the pipeline script or notebook

## 📊 Data Schema

### Transaction Data

| Column            | Type    | Description                     |
| ----------------- | ------- | ------------------------------- |
| transaction\_id   | String  | Unique transaction identifier   |
| customer\_id      | String  | Unique customer ID              |
| product\_id       | String  | Product involved in transaction |
| quantity          | Integer | Number of units purchased       |
| transaction\_date | Date    | Transaction date                |
| channel           | String  | Sales channel (web/mobile/pos)  |
| campaign\_id      | String  | Campaign identifier             |
| amount            | Double  | Total transaction value         |

### Product Data

| Column        | Type   | Description               |
| ------------- | ------ | ------------------------- |
| product\_id   | String | Unique product identifier |
| product\_name | String | Name of product           |
| category      | String | Product category          |
| price         | Double | Unit price                |
| description   | String | Product description       |
| brand         | String | Product brand             |

## 🔧 Configuration

### Databricks Cluster

```json
{
  "spark_version": "11.3.x-scala2.12",
  "node_type_id": "Standard_DS3_v2",
  "num_workers": 2,
  "spark_conf": {
    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog"
  }
}
```

## 📊 Analytics Features

### Customer Analytics

* Average order value per customer
* Customer lifetime value
* Purchase frequency analysis
* Customer segmentation (High Value, Frequent, Recent, Regular)

### Product Analytics

* Top-selling products
* Category performance
* Revenue by product
* Inventory turnover analysis

### Marketing Campaign Analysis

* Campaign ROI calculation
* Channel effectiveness
* Customer acquisition cost
* Campaign attribution analysis

### Data Quality Monitoring

* Missing value detection
* Outlier identification
* Data consistency checks
* Quality score calculation

## 🏃‍♂️ Usage Example

```python
from src.transaction_analyzer import TransactionAnalyzer

analyzer = TransactionAnalyzer(
    storage_account_name="datalake2004",
    access_key="your_access_key is hide that why i not added here",
    container_name="transaction-data"
)

results = analyzer.run_complete_analysis()
analyzer.display_results(results)
```


this is my last readme so update it based on the updation
