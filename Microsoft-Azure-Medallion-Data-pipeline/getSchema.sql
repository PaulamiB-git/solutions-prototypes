SELECT
s.name AS SchemaName,
t.name AS tableName
FROM sys.tables t
INNER JOIN sys.schemas s
ON t.schema_id = s.schema_id
WHERE s.name = 'Sales'