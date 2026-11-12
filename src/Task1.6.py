import pandas as pd
from pathlib import Path

file_path1 = (
    Path(__file__).resolve().parent.parent
    /"data"
    /"processed"
    /"clean_appointments.parquet"
)


df = pd.read_parquet(file_path1)

#sorting data by appointment_id
df = df.sort_values("appointment_id")

#formating date in YYYY-MM-DD formate
df["booked_on"] = df["booked_on"].dt.strftime("%Y-%m-%d")
df["appt_date"] = df["appt_date"].dt.strftime("%Y-%m-%d")

file_path2 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "appointments_clean.csv"

)
df.to_csv(file_path2,index = False)

appointments = df

file_path3 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "clinics_enriched.csv"

)

clinics = pd.read_csv(file_path3)

file_path4 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "load_data.sql"

)

with open(file_path4,"w",newline = "") as file:

    for clinic in clinics.itertuples(index=False):
        clinics_sql = (
        f"INSERT INTO clinics VALUES "
        f"('{clinic.clinic_id}',"
        f"'{clinic.clinic_name}',"
        f"'{clinic.city}',"
        f"'{clinic.tier}',"
        f"{clinic.latitude},"
        f"{clinic.longitude},"
        f"{clinic.temp_c});\n"
        )
        file.write(clinics_sql)


    for appointment in appointments.itertuples(index=False):
        appointments_sql = (
        f"INSERT INTO appointments VALUES "
        f"('{appointment.appointment_id}',"
        f"'{appointment.patient_id}',"
        f"'{appointment.clinic_id}',"
        f"'{appointment.booked_on}',"
        f"'{appointment.appt_date}',"
        f"{appointment.age},"
        f"'{appointment.gender}',"
        f"{appointment.distance_km},"
        f"{appointment.fee_inr},"
        f"'{appointment.booking_channel}',"
        f"'{appointment.visit_type}',"
        f"{appointment.reminder_sent},"
        f"{appointment.prior_no_shows},"
        f"'{appointment.status}',"
        f"{appointment.lead_days},"
        f"{appointment.no_show});\n"
        )
        file.write(appointments_sql)

