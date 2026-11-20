import pandas as pd
from pathlib import Path

file_path1 = (Path(__file__).resolve().parent.parent
/"data"
/"processed"
/"clean_appointments.parquet"
)

file_path2 = (Path(__file__).resolve().parent.parent
/"data"
/"processed"
/"clinics_enriched.csv"
)

appointments = pd.read_parquet(file_path1)
clinics = pd.read_csv(file_path2)

#no_shows per clinic
clinics_no_show =appointments.groupby("clinic_id")["no_show"].sum()

#total appointments per clinic
clinics_appointments = appointments.groupby("clinic_id")["clinic_id"].count()

clinics["no_show"] = clinics["clinic_id"].map(clinics_no_show)
clinics["appointments"] = clinics["clinic_id"].map(clinics_appointments)

#no_show percentage
clinics["no_show_pct"] = round(clinics["no_show"]/clinics["appointments"]*100,2)


#clinics having appointments >= 95
print("clinics having appointments >= 95")
print(clinics[clinics["appointments"] >= 95].sort_values("no_show_pct",ascending = False))

