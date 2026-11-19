# AI-Assisted Patient Follow-Up System
## Overview
This project aims to help healthcare provider to automate patient follow-up processes using data analysis and AI techniques.

## Objectives
Track patient follow-up schedules
Identify patients requiring follow-up
Generate reminder recommendations
Predict missed appointments
## Dataset
The project currently uses three CSV files:
appointments.csv 
clinics.csv
followup_notes.csv

## Tech Stack
Python
Pandas
NumPy
Scikit-learn
Git & GitHub


## Project Structure

``` text

│   README.md
│   
├───data
│   ├───processed
│   │       accepted_rows.json
│   │       appointments_clean.csv
│   │       clean_appointments.csv
│   │       clean_appointments.parquet
│   │       clean_appointments_pass1.csv
│   │       clean_appointments_pass1.parquet
│   │       clean_appointments_pass2.csv
│   │       clean_appointments_pass2.parquet
│   │       clinics_enriched.csv
│   │       load_data.sql
│   │       rejected_rows.json
│   │       
│   └───raw
│           appointments.csv
│           clinics.csv
│           followup_notes.csv
│           
└───src
        Task1.1.py
        Task1.2.py
        Task1.3.py
        Task1.4.py
        Task1.5.py
        Task1.6.py
        
```
## Highlights
 Initial setup and data exploration phase.
 - using Path from pathlib to overcome file path issue when running the project on defferent machines.
 - saving a parquet file to preserve datatypes of the dataframe because csv coverts everything to string.



