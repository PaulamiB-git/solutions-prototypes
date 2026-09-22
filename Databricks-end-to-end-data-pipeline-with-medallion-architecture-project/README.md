# Retail Data Engineering Project using Azure Databricks

## Project Overview

This project demonstrates an end-to-end retail data engineering pipeline built using Azure Databricks. The project follows the Medallion Architecture to ingest, transform, validate, and prepare retail data for analytics.

The pipeline implements incremental data loading, idempotent processing, Spark Structured Streaming, Delta Lake, Unity Catalog, data quality expectations, and dimensional modeling.

The Gold layer includes dimensional tables implemented using Slowly Changing Dimensions (SCD) Type 1 and Type 2.

---

## Architecture

The project follows the Medallion Architecture:

Source Data  
↓  
**Bronze Layer**  
↓  
**Silver Layer**  
↓  
**Gold Layer**  
↓  
Analytics / Reporting

### Bronze Layer

The Bronze layer stores raw ingested data with minimal transformation.

### Silver Layer

The Silver layer performs data cleansing, transformation, validation, and preparation of data for downstream processing.

### Gold Layer

The Gold layer contains business-ready dimensional data optimized for analytics and reporting.

---

## Technologies Used

- Azure Databricks
- PySpark
- Python
- SQL
- Apache Spark Structured Streaming
- Delta Lake
- Azure Data Lake Storage Gen2 (ADLS Gen2)
- Unity Catalog
- Spark Declarative Pipelines (SDP)
- SCD Type 1
- SCD Type 2
- Change Data Capture (CDC)

---

## Key Features

### 1. Medallion Architecture

Implemented a three-layer data architecture:

- Bronze – Raw data
- Silver – Cleansed and transformed data
- Gold – Analytics-ready dimensional data

This provides clear separation between ingestion, transformation, and business logic.

---

### 2. Incremental Data Loading

The pipeline processes new data incrementally instead of unnecessarily reprocessing the complete dataset.

This improves processing efficiency and reduces unnecessary compute consumption.

---

### 3. Idempotent Processing

The pipeline is designed to support idempotent processing so that repeated executions do not unnecessarily create duplicate records.

This is important for reliable production data pipelines.

---

### 4. Spark Structured Streaming

Spark Structured Streaming is used to process data incrementally between pipeline layers.

Example:

```python
spark.readStream.table(
    "databricks035_catalog.silver.products"
)

---

### 5. Data Quality

Implemented Lakeflow expectations to validate incoming data.

Example:

```python
rules = {
    "rule1": "product_id IS NOT NULL",
    "rule2": "product_name IS NOT NULL"
}
