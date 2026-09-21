create view gold.final2
AS
SELECT 
     *
FROM 
    OPENROWSET(
        BULK 'https://olistdatastoaccount.dfs.core.windows.net/olist-data/silver/',
        FORMAT = 'PARQUET'
    ) AS result2
where order_status='delivered'

select * from gold.final2