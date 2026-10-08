"""

this is used to clean census data to fill in the gaps that Urban could not (2020-2024)

"""

import sys
import pandas as pd

#insert where the file is here
path = sys.argv[1] if len(sys.argv) > 1 else input("Path to the Excel file: ").strip()

df = pd.read_excel(path, dtype=str)
canfield = df[df["NCESID"] == "3904831"].iloc[0]   # sorted by school ID

year = 2000 + int(canfield["YRDATA"]) #canfield hs was here in year "25" lol
out = pd.DataFrame([{
    "year": year,
    "rev_total": int(canfield["TOTALREV"]) * 1000,
    "exp_total": int(canfield["TOTALEXP"]) * 1000,
}])

out.to_csv(f"canfield_{year}.csv", index=False)
print(out)
print(f"Saved canfield_{year}.csv")