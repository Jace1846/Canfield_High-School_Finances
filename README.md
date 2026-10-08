# Canfield-High-school-Data-Analysis

## Description
As K-12 eduication continues to struggle post covid, my home-town of Canfield Ohio is urgently trying to pass a levy to help fund my high school (Canfield High-School of Canfield LSD). To see just how bad the funding problem is, I took it upon myself t write up this mall project in matplotlib to put into perspective the financial peril of this school. Sources include data from the Urban Education API, the US Census Beauvoir, and numbers given (scraped and checked) from the vindicator. PLEASE DO NOT TAKE THIS WITH A GRAIN OF SALT AND IF YOU ARE FROM CANFIELD VOTE FOR THE LEVY.

## Sources For Expenditures vs income
- API endpoint: `https://educationdata.urban.org/api/v1/school-districts/ccd/finance/{year}/?leaid=3904831`

| Fiscal year | Raw file |
|---|---|
| 2021 | https://www2.census.gov/programs-surveys/school-finances/tables/2021/secondary-education-finance/elsec21.xls |
| 2022 | https://www2.census.gov/programs-surveys/school-finances/tables/2022/secondary-education-finance/elsec22.xlsx |
| 2023 | https://www2.census.gov/programs-surveys/school-finances/tables/2023/secondary-education-finance/elsec23.xlsx |
| 2024 | https://www2.census.gov/programs-surveys/school-finances/tables/2024/secondary-education-finance/elsec24.xlsx |

The two were merged with years adjusted into the final csv (URBAN started in fall CENSUS started in spring)
