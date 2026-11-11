import csv
import pandas as pd
from pathlib import Path
import requests


file_path1 = (
    Path(__file__).resolve().parent.parent
    /"data"
    /"raw"
    /"clinics.csv"
)
clinic_data = []
temp_c = []
with open(file_path1,"r",newline = "") as file:
    reader = csv.DictReader(file)

    for row in reader :
        clinic_data.append(row)

for clinic in clinic_data:
    for attempt in range(2):
        try:
            response = requests.get("https://api.open-meteo.com/v1/forecast",
            params={"latitude":clinic["latitude"], "longitude":clinic["longitude"],
            "hourly": "temperature_2m", "forecast_days": 1},timeout=10) 

            response.raise_for_status()   

            data = response.json()
            temp_c.append(data["hourly"]["temperature_2m"][0])

            break

        except (requests.exceptions.RequestException,KeyError,IndexError )as e :
            if attempt == 1 :
                temp_c.append(None)
                print(f"{clinic['clinic_name']} failed :", e)


df = pd.DataFrame(clinic_data)
df["temp_c"] = temp_c

file_path2 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "clinics_enriched.parquet"

)
df.to_parquet(file_path2,index = False)

file_path3 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "clinics_enriched.csv"

)
df.to_csv(file_path3,index = False)