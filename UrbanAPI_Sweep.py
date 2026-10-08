"""

 Pull all of Canfield financial data into a csv file called canfield_fianace.csv

required libraries: requests, pandas

"""

import requests
import pandas as pd

url = "https://educationdata.urban.org/api/v1/school-districts/ccd/finance/{}/?leaid=3904831"

rows = []
for year in range(1994, 2021):
    rows += requests.get(url.format(year)).json()["results"]

df = pd.DataFrame(rows)[["year", "rev_total", "exp_total"]]
df.to_csv("canfield_finance.csv", index=False)
print(df)

