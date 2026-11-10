import csv
import json
from pathlib import Path


def parse_row(row):
   '''
   from dictionary row :
   converts age,fee_inr,prior_no_show -> int  and distance_km -> float
   returns coverted dictionary

   '''

   converted_row = {}
   for key in row:
     match key:
        case "age": converted_row["age"] = int(row["age"])
        case "fee_inr": converted_row["fee_inr"] = int(row["fee_inr"])
        case "prioe_no_show": converted_row["prior_no_show"] = int(row["prior_no_show"])
        case "distance_km" : converted_row["distance_km"] = float(row["distance_km"])
        case _ : converted_row[key] = row[key]
   return converted_row



file_path = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "appointments.csv"
)

rejected =[]
accepted = []

try:

    with open(file_path, "r", newline="") as file:

        reader = csv.DictReader(file)

        print(f"Header : {reader.fieldnames}")
        row_count = 0
        for row in reader:
            row_count += 1

            try :
                accepted.append(parse_row(row))
            except ValueError :
                rejected.append(row)
            except Exception as e:
                print(f"Unexpected error: {e}")


        print(f"No of rows : {row_count}")

        
           

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

except Exception as e:
    print(f"Unexpected error: {e}")



file_path2 = (
    Path(__file__).resolve().parent.parent
    / "data"
   /"processed"
   /"rejected_rows.json"
)


with open(file_path2,"w") as file:
    json.dump(rejected, file, indent=2)


file_path3 = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "processed"
    / "accepted_rows.json"
)

with open(file_path3,"w") as file:
    json.dump(accepted, file, indent=2)








