import duckdb

query = """
SELECT
    date,
    AVG(temperature) AS avg_temperature,
    MAX(humidity) AS max_humidity
FROM 'data/processed/weather_processed.parquet'
GROUP BY date
ORDER BY date
"""

result = duckdb.sql(query)

print(result.df())