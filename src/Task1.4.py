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

print(df.info())
