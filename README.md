# Canfield-High-school-Data-Analysis

## Description
This essentially charts out the financial data of canfield high school. Please pass that damn levy.

## Summarys
### Income v.s. Expenditures
<img width="1400" height="600" alt="canfield_income_vs_expenditures" src="https://github.com/user-attachments/assets/03ca86c4-8f3b-410e-b25f-2f5c0b77c6a8" />

Income grew from $13.3M to $35.0M over 30 years, and expenditures grew from $13.0M to $33.8M. The district ran a surplus in 27 of the 30 years.

The only deficits were in FY1999 (-$3.0M), FY2000 (-$7.3M) and FY2002 (-$0.6M). The FY2000 spike came from one-time capital spending of about $9.7M, including $8.75M in construction, rather than operating costs. From FY2003 to FY2024 the district ran a surplus every year, usually $2–4M.

What it means: That long run of surpluses built up the cash reserves the district relies on today. But the margin is narrowing as expenditures rise faster than income. The surplus fell to $0.3M in FY2023, the smallest since FY2002, before recovering to $1.2M in FY2024.

### Projected Income v.s. Expenditures
<img width="1000" height="600" alt="canfield_projected_income_vs_expenditures" src="https://github.com/user-attachments/assets/a7d42140-9976-4ec0-bf9f-32f621bcff39" />

The November 2024 forecast shows income staying flat at $31–32M while expenditures rise from $29.6M to $35.6M, an increase of $6M. Deficit spending starts in FY2025, and the annual gap grows from -$0.7M to -$4.6M by FY2029.

Cost drivers: Salaries and benefits make up about 84% of the budget, and health insurance, inflation and operating costs keep rising.

Revenue limits: New Ohio property tax laws (HB 129, 186, 309 and 335) cap how much revenue can grow, and a 2.5% county property tax cut reduces collections by about $380K a year.

What it means: The deficit is already happening. The district reported a $1.25M deficit for 2025-26 and expects about $2.5M for 2026-27. Cost reductions through attrition are projected to save about $500K. The district's main fix is a 5.9-mill operating levy on the November ballot, projected to raise $5.3M a year, which is more than the largest projected annual deficit. It would cost about $207 a year per $100,000 of home value.


### Reserve Days Projections
<img width="1000" height="600" alt="canfield_reserve_days" src="https://github.com/user-attachments/assets/818151f7-7e9e-454b-8175-ad1b9ea7a60d" />

Reserve days measure how long the district could operate on its cash balance if all revenue stopped. Roughly 50 days is the minimum a district should maintain.

Reserves were 223 days in FY2022 and are projected to fall to 128 days in FY2026 and 44 days in FY2028, below the minimum. The February 2026 forecast showed reserves going negative (-16 days) in FY2029. The spring 2026 update revised that to 4 days.

What it means: The cash balance is being used to cover the annual deficits, and at the projected rate it runs out by FY2029. The district set aside a one-time $4M for capital needs, but monthly operating costs are about $3M, so that would cover only about six weeks. Without new revenue or further cost reductions, the district risks state fiscal oversight.

Note: only four years were reported. The line between them is connected for readability, and the years in between are not actual data.




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


