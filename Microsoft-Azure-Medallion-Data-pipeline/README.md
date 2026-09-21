# Data Migration and Analytics using Microsoft Azure (Data Engineering)
In this project we are going to create an end-to-end data pipeline that moves the data from an On-Prem SQL database and following steps such as Data Ingestion, Data Transformation, Data Loading, Data Governance and finally Data Reporting using Microsoft Power BI.




# Project Goals 

1. Data Ingestion - Create a data ingestion pipeline to extract data from on-premises SQL Server Database using Azure Data Factory
2. Data Storage - Create a centralized repository to store data from SQL Server Database into Azure Data Lake Gen 2 storage.
3. Data Transformation - Create ETL job to extract the data, do simple transformations and load the clean data using Azure Databricks.
4. Data Governance - Create Azure key vaults and Active Directory to monitor and govern the whole project using Azure roles.
5. Data Analytics - Create data integration pipeline with Power BI using Azure Synapse Analytics to create powerful visualizations.



# Data Architecture

The architecture (Data flow) used in this project uses different Azure functionalities.

<p align="center">
  <img width="950" height="550" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/35edfd98-87ae-4389-81f0-40d1b7021892">
  <h6 align = "center" > Source: Author </h6>
</p>

With the combination of Azure Datalake and Azure Databricks, we can create a lakehouse architecture that follows three layer of data processing: 

* Bronze Layer - This is the exact copy of the data source, in its raw form. All the tables (relational model) or any unstructured data (Non-relational model) is stored in this layer. No transformations are done.
* Silver Layer - In this step, soft data transformations are performed such as fixing data types, column names, date formats, etc. to a standardized format and store in a more structured way.
* Gold Layer - This layer is the cleanest form of data that can be used for downstream tasks. Number of other things could also be implemented at this stage like business rules, conformity checks, etc.

# Dataset Used 
The dataset is an open source database provided by Microsoft namely 'AdventureWorks2017'. It contains a lot of different tables with their corresponding relationships. Dataset link - https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms

# Microsoft Azure Services used in this project
1. **Azure Data Lake Gen2 Storage** - A data lake is a single, centralized repository where you can store all your data, both structured and unstructured. It provides various tools to deal with Big Data analytics based on Azure Blob Storage. It is mainly designed to work with Hadoop and all frameworks that use the Apache HDFS as their data access layer.
2. **Azure Data Factory** - ADF is a fully managed, serverless data intergration service. It allows to create Data Pipelines to Extract, Transform and Load (ELT) data from more than 90 sources. It allows us to choose from more than 90 built-in connectors to acquire data from big data sources such as Amazon Redshift, Google BigQuery, and HDFS.
3. **Azure Databricks** - It is a cloud-based big data analytics platform provided by Microsoft Azure, built on top of Apache Spark. Azure Databricks is a fully managed first-party service that enables an open data lakehouse in Azure. Jupyter notebooks can be used to transform, perform analytics, machine learning, etc. offering the capabilities of Apache Spark.
4. **Azure Synapse Analytics** - Azure Synapse Analytics, formerly known as Azure SQL Data Warehouse, is a cloud-based analytics service provided by Microsoft Azure. It's designed to handle large volumes of data and enable organizations to perform data warehousing, big data analytics, and data integration tasks. It offers a distributed architecture to perform big data analytics.
5. **Azure Key Vault** - Azure Key Vault is a cloud service offered by Microsoft Azure that allows you to securely manage cryptographic keys, secrets, certificates, and other sensitive information used by your applications and services. Key Vault provides a centralized and secure way to store and control access to these sensitive materials.
6. **Azure Active Directory** - Azure Active Directory (Azure AD) is Microsoft's cloud-based identity and access management service. It provides a comprehensive set of capabilities for managing identities, securing access to resources, and enabling seamless authentication and authorization across applications and services. Azure AD is a foundational component of Microsoft's cloud services and plays a crucial role in modern IT infrastructure.
7. **Microsoft Power BI** - Microsoft Power BI is a powerful business intelligence (BI) platform that allows users to visualize and share insights from their data. It enables organizations to connect to a wide range of data sources, transform and shape the data, create interactive reports and dashboards, and share those insights with others. Power BI is designed to help users make data-driven decisions and gain actionable insights from their data.

# Implementation
* **Step 1** - Create a data integration link service to connect SQL server with Azure Data Factory
  Since, the database is located in an on-premises SQL Server, Microsoft Azure needs a way to detect the stored data and able to interact with it.

  <p align="center">
  <img width="400" height="150" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/6e7b18fb-3e14-444d-9610-ae8fe5e32a97">
  <h6 align = "center" > Source: Author </h6>
</p>



  To actualize that, the first step includes creating a Self Hosted Integration Runtime (SHIR) linked service and install it on the physical machine where the server is deployed. 

<p align="center">
  <img width="500" height="350" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/209c6c93-b4ad-4a54-bea5-42e4c02e0e0f">
  <h6 align = "center" > Source: Author </h6>
</p>

Start the installed integration runtime and ADF is ready to be integrated with On-prem SQL Server Database. Create a new pipeline in ADF to copy data from SQL Server to Azure Data Lake Storage Gen2. It is important to select the Source and Sink properties to define the correct data flow. The pipeline consists of two parts, firstly, the lookup table that will query the name and schema of each table stored in the SQL Server Database. Secondly, creating a ForEach element that runs a for-loop through the output of lookup table activity and store it in bronze storage layer which is exact copy of the SQL database. The folder structure is supposed to look like Layer/Schema/TableName/TableName.parquet.

<p align="center">
  <img width="400" height="250" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/a290089c-66cf-404d-951c-cc59979c4803">
  <h6 align = "center" > Source: Author </h6>
</p>

* **Step 2** - Mounting the database to perform Data Transformation using Azure Databricks
  To do any kind of transformations, we need some compute power to do perform them. In Azure databricks, the 'compute' option gives us the capability to fire spark clusters and perform data transformations.


<p align="center">
  <img width="400" height="150" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/ccde7b46-ad0a-4bff-9b4c-40c215192c76">
  <h6 align = "center" > Source: Author </h6>
</p>

  Using the workspace tab, we can create jupyter notebooks to mount the data from three layers into the datalake. The notebook will use the resources configured by spark clusters. The data transformations would be different for different projects, we are doing a simple transfomation such as modifying the datetime format to date format. The file is loaded in parquet format which is a column-based data format and is highly efficient.


* **Step 3** - Connecting Azure Data Factory with Azure Databricks to create data pipelines for data transformations.
  The data is ever increasing and we need a way to automate the data ingestion and transformation processes as much as possible.

  <p align="center">
  <img width="400" height="150" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/814e5b57-14de-42bb-8de2-ecf1058d9fa9">
  <h6 align = "center" > Source: Author </h6>
</p>

In this step, we will be connecting Azure Databricks to create data pipeline that will be triggered automatically whenever there is new data. Similar to step 1, we will create two new Databricks notebook activities following the data ingestion part, i.e bronze to silver and silver to gold. Connect the output of ForEach activity to bronze to silver notebook.

<p align="center">
  <img width="900" height="250" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/45cc86a1-3058-4530-abf4-8ad1cd6a1153">
  <h6 align = "center" > Source: Author </h6>
</p>

The outpur from bronze to silver layer goes to silver to gold layer where the final transformations will happen and put the final data in gold container. The final data will be in delta format since this new format can handle schema changes and can keep track of file versions. One interesting thing is that we can monitor the execution of Azure Databricks notebook in real time, which could come handy to debug the code while runtime. 


* **Step 4** - Load the data to Azure Synapse Analytics for further big data analytics
  Azure Synapse Analytics is built on top of Azure Data Factory, so many options can be found in the Synapse Analytics. In Azure Synapse Analytics, we can create databases which is not available in ADF.

<p align="center">
  <img width="400" height="150" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/08312ac8-2164-4f3c-a746-bfc5129f3df4">
  <h6 align = "center" > Source: Author </h6>
</p>


Azure Synapse Analytics could be thought of as the combination of both Azure Databricks and Azure Data Factory. Firstly we will create a Serverless Azure SQL Database to load the data into Azure Synapse Analytics. In serverless database, the data will already be available in the datalake, we will just be using the built-in SQL pool to directly query the gold data. Azure Synapse Analytics already has a link to Azure Data Lake Storage which will make the task even easier. We shall create a gold database view in serverless SQL database in order for us to query the data directly from Synapse workspace. Since the views are only referencing the data stored in datalake, any changes in datalake will also be reflected in Synapse database views. 

<p align="center">
  <img width="450" height="250" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/dc162e7f-6638-4783-ac34-83dd57eb9998">
  <h6 align = "center" > Source: Author </h6>
</p>

Now, we have completed the data loading part.

* **Step 5** - Connecting PowerBI to Azure Synapse Analytics to create interactive visualizations
  The PowerBI desktop will be used and the data source will be marked as Azure Synapse Analytics SQL views.

<p align="center">
  <img width="400" height="150" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/36a45150-5433-49b7-8555-620f9f765ae1">
  <h6 align = "center" > Source: Author </h6>
</p>

PowerBI will load all the gold data views stored in Synapse Analytics. Below are some of the dashboard reporting created using PowerBI. 


<p align="center">
  <img width="800" height="400" src="https://github.com/chayansraj/Microsoft-Azure-Data-Engineering-End-to-End/assets/22219089/752dace5-67bd-468f-801c-e6795b086424">
  <h6 align = "center" > Source: Author </h6>
</p>







