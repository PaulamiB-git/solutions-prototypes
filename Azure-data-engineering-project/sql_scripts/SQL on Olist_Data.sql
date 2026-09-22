
SELECT 
     *
FROM 
    OPENROWSET(
        BULK 'https://olistdatastoaccount.dfs.core.windows.net/olist-data/silver/',
        FORMAT = 'PARQUET'
    ) AS result1

