---CREATE MASTER KEY ENCRYPTION BY PASSWORD ='your_password';
---CREATE DATABASE SCOPED CREDENTIAL nihaladmin WITH IDENTITY = 'Managed Identity';
---select * from sys.database_credentials


CREATE EXTERNAL FILE FORMAT extfileformat WITH (
    FORMAT_TYPE = PARQUET,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec'
);

CREATE EXTERNAL DATA SOURCE goldlayer WITH (
    LOCATION = 'https://olistdatastoaccount.dfs.core.windows.net/olist-data/gold/',
    CREDENTIAL = nihaladmin
);

CREATE EXTERNAL TABLE gold.finaltable WITH (
    LOCATION = 'Serving',
    DATA_SOURCE = goldlayer,
    FILE_FORMAT = extfileformat
) AS 
SELECT * FROM gold.final2;
