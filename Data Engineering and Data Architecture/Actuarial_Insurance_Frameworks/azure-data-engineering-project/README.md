# Azure Data Engineering Project — Olist E-Commerce Pipeline

An end-to-end enterprise data engineering platform on **Microsoft Azure**, implementing a **Medallion Architecture** (Bronze → Silver → Gold) using **Azure Data Factory**, **Azure Databricks**, **ADLS Gen2**, **MongoDB**, and **Synapse Analytics** — built on the Olist Brazilian e-commerce dataset.

---

## 🏗️ Architecture

![Architecture Diagram](ss/Architecture%20Diagram.png)

**Flow:**
1. **Data Sources** — Raw CSVs pulled via HTTP from GitHub + a relational **SQL table**.
2. **Data Ingestion** — Azure Data Factory orchestrates ingestion into ADLS Gen2.
3. **Raw Data (Bronze)** — Landed in ADLS Gen2 as-is.
4. **Data Transformation** — Azure Databricks cleans, joins, and enriches the data, pulling in a lookup/enrichment table from a **NoSQL (MongoDB) database**.
5. **Transformed Data (Silver)** — Written back to ADLS Gen2 in Parquet format.
6. **Serving (Gold)** — Azure Synapse Analytics (serverless SQL pool) exposes curated views on top of the Silver layer.
7. **Visualization** — Power BI, Tableau, and Microsoft Fabric consume the Gold layer for reporting.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Source Simulation | Google Colab (seeding MySQL + MongoDB) |
| Orchestration | Azure Data Factory |
| Storage | Azure Data Lake Storage Gen2 |
| Compute / Transformation | Azure Databricks (PySpark) |
| Enrichment Store | MongoDB (NoSQL) |
| Relational Source | MySQL |
| Serving Layer | Azure Synapse Analytics (Serverless SQL Pool) |
| Security | Azure AD App Registration (Service Principal), IAM RBAC |
| Visualization | Power BI / Tableau / Microsoft Fabric |

---

## 📊 Dataset

The pipeline uses the **Olist Brazilian E-Commerce** public dataset, made up of 8 relational CSV files:

- `olist_customers_dataset`
- `olist_geolocation_dataset`
- `olist_order_items_dataset`
- `olist_order_payments_dataset`
- `olist_order_reviews_dataset`
- `olist_orders_dataset`
- `olist_products_dataset`
- `olist_sellers_dataset`

To make the project reflect a more realistic, multi-source enterprise scenario (rather than pulling everything from one place), the original flat dataset was deliberately split across two different systems — a relational database and a NoSQL store — before the actual pipeline was built.

### Entity Relationship Diagram

![ER Diagram](ss/Screenshot%202026-09-10%20202029.png)

---

## 0️⃣ Source Setup — Seeding MySQL & MongoDB (Google Colab)

📓 [`DataIngestionToSql&MongoDB.ipynb`](DataIngestionToSql%26MongoDB.ipynb)

This is a **one-time setup notebook**, run in **Google Colab**, that simulates having two independent upstream source systems instead of a single flat GitHub dataset:

1. All Olist CSVs originally lived together in one place (GitHub).
2. In Colab, two of the dataset files were uploaded separately.
3. One file was loaded into a hosted **MySQL** instance (acting as the relational operational source).
4. The other file was loaded into a hosted **MongoDB** instance (acting as the NoSQL enrichment source).

This split is what makes the downstream pipeline non-trivial: Azure Data Factory later has to ingest from **both** GitHub (HTTP CSVs) **and** MySQL, while Databricks separately connects to **MongoDB** to enrich the data during transformation — instead of everything being a simple single-source copy job.

> This notebook is a source-provisioning script, not part of the recurring ADF/Databricks pipeline — it only needed to run once to stand up the MySQL and MongoDB databases shown in the architecture diagram.

![Shared Databases](ss/Screenshot%202026-09-12%20200554.png)

---

## 1️⃣ Ingestion — Azure Data Factory & App Registration

Once MySQL and MongoDB were seeded (see step 0 above), the actual ingestion pipeline pulls from the **real** sources: GitHub (HTTP CSVs) + MySQL.

A **parametrized ADF pipeline** dynamically loops through source tables using `Lookup` → `ForEach` → `Copy Data` activities, pulling data from the SQL source into ADLS Gen2.

![ADF Pipeline Run](ss/Screenshot%202026-09-07%20182406.png)

### Lookup Configuration — `ForEachInputFor.json`

📄 [`ForEachInputFor.json`](ForEachInputFor.json)

For the CSVs sourced directly from GitHub, the ADF pipeline needs a list of files to fetch and what to name each one. This JSON is the input to the **Lookup** activity, which then drives the **ForEach → Copy Data** loop shown above.

Each entry pairs a raw GitHub file URL with its target file name:

```json
{
  "csv_relative_url": "BigDataProjects/refs/heads/main/Project-Brazillian%20Ecommerce/Data/olist_customers_dataset.csv",
  "file_name": "olist_customers_dataset.csv"
}
```

For every entry, Copy Data downloads the file from `csv_relative_url` and writes it into ADLS Gen2 as `file_name` — letting one parametrized pipeline ingest all GitHub-hosted datasets instead of a hardcoded Copy Data activity per file.

### Bronze Layer in ADLS Gen2

All raw datasets landed in the `olist-data/bronze` container.

![Bronze Layer](ss/Screenshot%202026-09-06%20154313.png)

### Security — Service Principal & Access Control

An **Azure AD App Registration** authenticates Databricks against ADLS Gen2 via OAuth (Service Principal).

![App Registration](ss/Screenshot%202026-09-08%20151852.png)

Access is scoped through **IAM role assignments** — the app registration and Databricks managed identity are granted `Storage Blob Data Contributor` on the storage account.

![Storage IAM Roles](ss/Screenshot%202026-09-12%20190608.png)

> ⚠️ **Security note:** Never hardcode client secrets in notebooks or commit them to source control. Use **Azure Key Vault** and reference secrets via `dbutils.secrets.get()` instead. All credentials used in this project have since been rotated and the underlying Azure resources have been decommissioned.

---

## 2️⃣ Transformation — Azure Databricks

Transformation logic lives in:
📓 [`DataBricks Code For Transformation.ipynb`](DataBricks%20Code%20For%20Transformation.ipynb)

In Databricks, the raw Bronze data and the MongoDB source were brought together and turned into a clean, analysis-ready dataset:

1. **Read** the raw CSV data landed in ADLS Gen2 (Bronze layer).
2. **Clean and standardize** it — renaming columns, fixing types, and filtering out irrelevant or bad records.
3. **Join** the individual Olist tables (orders, customers, products, sellers, order items, etc.) into a single unified dataset.
4. **Enrich** that dataset with additional data pulled from **MongoDB**.
5. **Aggregate** the data and derive insights — for example, delivery delay time broken down by payment type.
6. **Write** the final, transformed dataset back to ADLS Gen2 as Parquet (Silver layer), ready for Synapse to consume.

### Final Joined DataFrame

Output of the join across orders, customers, products, sellers, and order items:

![Final DataFrame](ss/Screenshot%202026-09-10%20214447.png)

### Exploratory Visualization

In-notebook visualization of delivery delay time by payment type:

![Delay Time Visualization](ss/Screenshot%202026-09-10%20214430.png)

---

## 3️⃣ Serving — Azure Synapse Analytics

SQL scripts for the Gold-layer views are in [`sql_scripts/`](sql_scripts/). Synapse's **serverless SQL pool** reads the Silver-layer Parquet files directly via `OPENROWSET`, and curated views are built on top for consumption.

### Workspace Overview

![Synapse Workspace](ss/Screenshot%202026-09-12%20173902.png)

### Querying the Silver Layer

Synapse serverless SQL pool reads the Silver-layer Parquet files directly via `OPENROWSET`, without needing to load the data into a dedicated database first. This lets the data be queried immediately as soon as Databricks writes it back to ADLS Gen2.

The exact query used for this step is available in [`sql_scripts/`](sql_scripts/).

### Gold Layer — All Orders View

On top of the Silver-layer query, a `gold.final` view was created inside a new `gold` schema. This view exposes the complete, joined and enriched dataset — every order, regardless of status — as a single queryable object for downstream tools.

Script: [`sql_scripts/`](sql_scripts/)

### Gold Layer — Delivered Orders Only View

A second view, `gold.final2`, was created on top of the same Silver data but filtered down to only orders with `order_status = 'delivered'`. This gives a cleaner, ready-to-use dataset for delivery-performance and fulfillment analysis without needing to repeat the filter logic in every downstream query or report.

Script: [`sql_scripts/`](sql_scripts/)

### Gold Layer View – Query Result

The screenshot below shows the `gold.final` view being created in Synapse serverless SQL pool. It uses `OPENROWSET` to read the Silver-layer Parquet data directly from ADLS Gen2, then exposes the joined dataset for querying.



![Gold Layer View](ss/Screenshot%202026-09-12%20191718.png)

### Gold / Serving Layer Output

The final curated Parquet files produced by this process are written to the `gold/Serving` path in ADLS Gen2, ready to be picked up by Power BI, Tableau, or Fabric.

![Gold Serving Layer](ss/Screenshot%202026-09-12%20195842.png)

---

## 4️⃣ Visualization

The Gold layer views (`gold.final`, `gold.final2`) can be connected to:
- **Power BI** — via the built-in Synapse serverless SQL endpoint
- **Tableau** — via ODBC/JDBC connector to Synapse
- **Microsoft Fabric** — via direct lake/warehouse integration

---

## 📁 Repository Structure

```
azure-data-engineering-project/
├── README.md
├── DataBricks Code For Transformation.ipynb   # PySpark: cleaning, joins, MongoDB enrichment, aggregation
├── DataIngestionToSql&MongoDB.ipynb           # Colab: one-time seeding of MySQL + MongoDB source systems
├── ForEachInputFor.json                        # Lookup input driving the ADF ForEach/Copy Data loop
├── data/                                       # Sample/reference data
├── sql_scripts/                                # Synapse SQL: OPENROWSET queries, gold.final / gold.final2 views
└── ss/                                          # Project screenshots (referenced in this README)
```

---
