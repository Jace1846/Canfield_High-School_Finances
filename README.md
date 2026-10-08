# Canfield-High-school-Data-Analysis

## Description
This essentially charts out the financial data of canfield high school. Please pass that damn levy.

## Summarys
### Income v.s. Expenditures
<img width="1400" height="600" alt="canfield_income_vs_expenditures" src="https://github.com/user-attachments/assets/03ca86c4-8f3b-410e-b25f-2f5c0b77c6a8" />

Income grew from $13.3M to $35.0M, and expenditures grew from $13.0M to $33.8M. The district brought in more than it spent in 27 of the 30 years.

The only deficits were in FY1999 (-$3.0M), FY2000 (-$7.3M) and FY2002 (-$0.6M). In FY2000, expenditures jumped to $27.1M before falling back to $20.3M the next year. From FY2003 to FY2024 the district ran a surplus every year, usually between $2M and $4M.

What it means: The district has a long record of income covering its spending. In recent years, though, the gap between the two lines has narrowed. The surplus fell to $0.3M in FY2023, the smallest since FY2002, before rising to $1.2M in FY2024.

### Projected Income v.s. Expenditures
<img width="1000" height="600" alt="canfield_projected_income_vs_expenditures" src="https://github.com/user-attachments/assets/a7d42140-9976-4ec0-bf9f-32f621bcff39" />

Income is projected to stay flat: $31.0M in FY2024, peaking at $32.0M in FY2028, then back to $31.0M in FY2029. Over the same period, expenditures are projected to rise every year, from $29.6M to $35.6M, an increase of $6.0M.

FY2024 is the last projected surplus (+$1.4M). After that, the deficit grows each year: -$0.7M, -$1.4M, -$1.9M, -$2.6M and -$4.6M by FY2029. Altogether, that's about $11.2M more spent than earned from FY2025 to FY2029.

What it means: The deficit isn't a one-year problem. It gets bigger every year because spending keeps rising while income doesn't. By FY2029, the district is projected to spend about 15% more than it takes in.


### Reserve Days Projections
<img width="1000" height="600" alt="canfield_reserve_days" src="https://github.com/user-attachments/assets/818151f7-7e9e-454b-8175-ad1b9ea7a60d" />

Reserve days show how long the district's savings alone could cover normal spending. The forecast still assumes normal income. The savings shrink because they're used to cover each year's deficit.

Reserves are projected to fall from 223 days (FY2022) to 128 (FY2026) and 44 (FY2028), below the roughly 50-day minimum. In FY2029 they reach -16 days in the February forecast, revised to 4 days in the spring update.

What it means: The savings are running out, dropping below the minimum by FY2028 and reaching about zero by FY2029. The school is essentially broke as hell.




## Sources
### Sources For Expenditures vs income
- API endpoint: `https://educationdata.urban.org/api/v1/school-districts/ccd/finance/{year}/?leaid=3904831`

| Fiscal year | Raw file |
|---|---|
| 2021 | https://www2.census.gov/programs-surveys/school-finances/tables/2021/secondary-education-finance/elsec21.xls |
| 2022 | https://www2.census.gov/programs-surveys/school-finances/tables/2022/secondary-education-finance/elsec22.xlsx |
| 2023 | https://www2.census.gov/programs-surveys/school-finances/tables/2023/secondary-education-finance/elsec23.xlsx |
| 2024 | https://www2.census.gov/programs-surveys/school-finances/tables/2024/secondary-education-finance/elsec24.xlsx |

The two were merged with years adjusted into the final csv (URBAN started in fall CENSUS started in spring) and can be found in the cleaned data directory under: canfield_income_expenditures_FY1995-2024.csv

### Vidnicator Sources for Projections as well as reserve Timeline (Scraped but checked for Hallucinations)
- https://www.vindy.com/news/local-news/2026/02/canfield-schools-fall-into-distress-status/
- https://www.vindy.com/news/local-news/2026/05/canfield-school-chief-offers-strategic-plan-for-schools/
- https://www.vindy.com/news/local-news/2026/02/canfield-schools-fall-into-distress-status/


