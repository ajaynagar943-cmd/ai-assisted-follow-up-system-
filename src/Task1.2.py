import pandas as pd
import numpy as np
from pathlib import Path

file_path1 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "appointments.csv"

)

df = pd.read_csv(file_path1)

print("Shape : ", df.shape)

print(df.info())

print("No of Null Entries in each column : \n", df.isnull().sum())

print("No of Duplicated Records : ", df.duplicated().sum())

#Droping duplicate rows
df = df.drop_duplicates()

#cleaning booking_channel column
print(df["booking_channel"].unique())
df["booking_channel"] = df["booking_channel"].str.strip().str.title()
print(df["booking_channel"].unique())

#Converting appt_date and booked_on columns to datetime formate
df["appt_date"] = pd.to_datetime(df["appt_date"],errors = "coerce")
df["booked_on"] = pd.to_datetime(df["booked_on"],errors = "coerce")


#droping rows with Missing appt_date or status 
df = df.dropna(subset=["appt_date"]).reset_index(drop = True)
print("No of rows in DataFrame", df.shape[0])

df = df.dropna(subset=["status"]).reset_index(drop = True)
print("No of rows in DataFrame", df.shape[0])


#Saving cleaned df to a csv file

file_path2 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "clean_appointments_pass1.csv"

)
df.to_csv(file_path2,index = False)

