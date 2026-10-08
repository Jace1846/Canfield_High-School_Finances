"""

this is used to clean census data to fill in the gaps that Urban could not (2020-2024)

"""

import pandas as pd

path = "/excel Beuraeu Data RAW/elsec24.xlsx"  # change this to your file

df = pd.read_excel(path)
canfield = df[df["NAME"].str.contains("CANFIELD", na=False)].iloc[0]

year = 2000 + int(canfield["YRDATA"])
income = int(canfield["TOTALREV"]) * 1000        # Census lists thousands
expenditures = int(canfield["TOTALEXP"]) * 1000

result = pd.DataFrame([{"year": year, "income": income, "expenditures": expenditures}])
result.to_csv(f"canfield_{year}.csv", index=False)
print(result)