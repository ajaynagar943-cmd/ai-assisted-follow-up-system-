import numpy as np
import pandas as pd
from pathlib import Path 

file_path1 = (
    Path(__file__).resolve().parent.parent
    /"data"
    /"processed"
    /"clean_appointments_pass1.csv"
)

df = pd.read_csv(file_path1)

#replacing age <1 or age >100 with NaN
df["age"] = df["age"].mask(((df["age"]<1 )|(df["age"]>100)), pd.NA)

#filling missing values
df["age"] = df["age"].fillna(round(df["age"].median())).astype(int)
df["distance_km"] = df["distance_km"].fillna(df["distance_km"].median())

#Setting upper and lower limit for distance_kn & fee_inr
distance_q1 = df["distance_km"].quantile(.25)
fee_q1 = df["fee_inr"].quantile(.25)

distance_q3 = df["distance_km"].quantile(.75)
fee_q3 = df["fee_inr"].quantile(.75)

distance_iqr = distance_q3 - distance_q1
fee_iqr = fee_q3 - fee_q1

distance_upperlimit = distance_q3 + 1.5*distance_iqr
distance_lowerlimit = distance_q1 - 1.5*distance_iqr

fee_upperlimit = fee_q3 + 1.5*fee_iqr
fee_lowerlimit =  fee_q1 - 1.5*fee_iqr

print(
    "No of outliers in distance_km : ",
    ((df["distance_km"]<distance_lowerlimit)|(df["distance_km"]>distance_upperlimit)).sum()
    )

df["distance_km"] = df["distance_km"].clip(distance_lowerlimit,distance_upperlimit).round(1)

print(
    "No of outliers in fee_inr : ",
    ((df["fee_inr"]<fee_lowerlimit)|(df["fee_inr"]>fee_upperlimit)).sum()
    )

df["fee_inr"] = df["fee_inr"].clip(fee_lowerlimit,fee_upperlimit).round().astype(int)

file_path2 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "clean_appointments_pass2.csv"

)
df.to_csv(file_path2,index = False)
