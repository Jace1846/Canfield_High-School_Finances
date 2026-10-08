import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project = Path(__file__).parent.parent   # Charts/ -> project folder
df = pd.read_csv("/home/jason/PycharmProjects/Canfield High-School Finances/Cleaned Data /canfield_income_expenditures_FY1995-2024.csv")
x = df["fiscal_year"]
income = df["income"] / 1e6
spending = df["expenditures"] / 1e6

plt.figure(figsize=(14, 6))
plt.plot(x, income, marker="o", color="blue", label="Income")
plt.plot(x, spending, marker="o", color="red", label="Expenditures")

# Label deficit years
for yr, i, s in zip(x, income, spending):
    if s > i:
        plt.text(yr, s + 0.5, f"-${s - i:.1f}M", color="red", ha="center")

plt.text(x.iloc[-1] + 0.3, income.iloc[-1], "Income", color="blue")
plt.text(x.iloc[-1] + 0.3, spending.iloc[-1], "Expenditures", color="red")

plt.xticks(x, rotation=45)
plt.title("Canfield Local Schools: Income vs. Expenditures")
plt.xlabel("Fiscal year")
plt.ylabel("$ millions")
plt.grid(alpha=0.3)
plt.legend(loc="upper left", fontsize="small")
plt.tight_layout()
plt.savefig("canfield_income_vs_expenditures.png")
plt.show()