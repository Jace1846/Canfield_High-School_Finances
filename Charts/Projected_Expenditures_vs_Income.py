import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project = Path(__file__).parent.parent   # Charts/ -> project folder
df = pd.read_csv("/home/jason/PycharmProjects/Canfield High-School Finances/Cleaned Data /canfield_projected_income_expenditures_FY2024-2029.csv")
x = df["fiscal_year"]
income = df["income"] / 1e6
spending = df["expenditures"] / 1e6

plt.figure(figsize=(10, 6))
plt.plot(x, income, marker="o", color="blue", label="Income")
plt.plot(x, spending, marker="o", color="red", label="Expenditures")

# Label deficit years
for yr, i, s in zip(x, income, spending):
    if s > i:
        plt.text(yr, s + 0.15, f"-${s - i:.1f}M", color="red", ha="center")

plt.xticks(x)
plt.title("Canfield Local Schools: Projected Income vs. Expenditures (general fund)")
plt.xlabel("Fiscal year")
plt.ylabel("$ millions")
plt.grid(alpha=0.3)
plt.legend(loc="upper left", fontsize="small")
plt.figtext(0.99, 0.01, "Source: district five-year forecast (Nov 2024), via The Vindicator",
            ha="right", fontsize=8)
plt.tight_layout(rect=(0, 0.03, 1, 1))
plt.savefig("canfield_projected_income_vs_expenditures.png")
plt.show()