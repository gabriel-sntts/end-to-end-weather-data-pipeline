import requests
import pandas as pd

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude" : -4.94,
    "longitude" : -37.97,
    "hourly" : "temperature_2m,relative_humidity_2m",
    "forestcast_day": 1
}

response = requests.get(URL, params=params)

data = response.json()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "humidity": data["hourly"]["relative_humidity_2m"]
})

df.to_csv("data/raw/weather_raw.csv", index=False)

print(df.head())