import pandas as pd

#ler os dados do raw
df = pd.read_csv("data/raw/weather_raw.csv")

#convertemos colunas de data para o tipo datetime
df["time"] = pd.to_datetime(df["time"])

df["date"] = df["time"].dt.date
df["hour"] = df["time"].dt.hour

#salva no parquet
df.to_parquet("data/processed/weather_processed.parquet", index=False)

print(df.head())
print(df.dtypes)