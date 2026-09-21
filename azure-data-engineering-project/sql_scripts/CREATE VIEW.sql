create schema gold
create view gold.final
AS
SELECT 
     *
FROM 
    OPENROWSET(
        BULK 'https://olistdatastoaccount.dfs.core.windows.net/olist-data/silver/',
        FORMAT = 'PARQUET'
    ) AS result1

select * from gold.final