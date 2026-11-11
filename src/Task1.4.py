import numpy as np
import pandas as pd
from pathlib import Path 

file_path1 = (
    Path(__file__).resolve().parent.parent
    /"data"
    /"processed"
    /"clean_appointments_pass2.parquet"
)


df = pd.read_parquet(file_path1)

#adding lead_days & no_show columns

#calculating lead days
df["lead_days"] = (df["appt_date"]-df["booked_on"]).dt.days

#calculating no_show
df["no_show"] = np.where(df["status"] == "No-Show",1,0)
print("No of No-Show : ",df["no_show"].sum())


X = df[["age","distance_km","fee_inr","lead_days"]].to_numpy()
X_mean = X.mean(axis= 0)

#number and share of rows with lead_days > 14
no_of_rows = (X[:,3] >14).sum()
print(f"no of rows with lead_days > 14 : {no_of_rows}")
share_of_rows = (X[:,3] >14).mean()
print(f"share of rows with lead_days > 14 : {(share_of_rows*100).round(1)}%")

#Calculating Z Score for distance_km
Z_distance = ((X[:,1] - X_mean[1])/X[:,1].std())
#Rows having |Z_distance| > 2
rows= (np.abs(Z_distance)>2).sum()
print("Rows having |Z_distance| > 2 : ",rows)



file_path2 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "clean_appointments.parquet"

)
df.to_parquet(file_path2,index = False)

file_path3 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "clean_appointments.csv"

)
df.to_csv(file_path3,index = False)

