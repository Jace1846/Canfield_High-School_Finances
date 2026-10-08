# Canfield-High-school-Data-Analysis

## Description
This essentially charts out the financial data of canfield high school. Please pass that damn levy.

## Summarys
### Income v.s. Expenditures
<img width="1400" height="600" alt="canfield_income_vs_expenditures" src="https://github.com/user-attachments/assets/03ca86c4-8f3b-410e-b25f-2f5c0b77c6a8" />


### Projected Income v.s. Expenditures
<img width="1000" height="600" alt="canfield_projected_income_vs_expenditures" src="https://github.com/user-attachments/assets/a7d42140-9976-4ec0-bf9f-32f621bcff39" />


### Reserve Days Projections
<img width="1000" height="600" alt="canfield_reserve_days" src="https://github.com/user-attachments/assets/818151f7-7e9e-454b-8175-ad1b9ea7a60d" />





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


