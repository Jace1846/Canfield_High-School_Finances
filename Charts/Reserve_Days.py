import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project = Path(__file__).parent.parent   # Charts/ -> project folder
df = pd.read_csv("/home/jason/PycharmProjects/Canfield High-School Finances/Cleaned Data /canfield_reserve_days_FY2022-2029.csv")

feb = df[df["forecast"] == "Feb 2026 forecast"]
update = df[df["forecast"] == "Spring 2026 updated forecast"]

plt.figure(figsize=(10, 6))
plt.plot(feb["fiscal_year"], feb["reserve_days"], marker="o", color="purple", label="Feb 2026 forecast")
plt.scatter(update["fiscal_year"], update["reserve_days"], color="orange", s=60, label="Spring 2026 update")

# Label each point with its value
for _, r in df.iterrows():
    plt.text(r["fiscal_year"] + 0.12, r["reserve_days"], str(r["reserve_days"]), va="center")

plt.axhline(50, color="red", linestyle="--", label="~50-day minimum")
plt.axhline(0, color="black", linewidth=0.8)

plt.xticks(range(df["fiscal_year"].min(), df["fiscal_year"].max() + 1))
plt.title("Canfield Local Schools: Days the District Can Run on Reserves")
plt.xlabel("Fiscal year")
plt.ylabel("Days")
plt.grid(alpha=0.3)
plt.legend(loc="upper right", fontsize="small")
plt.figtext(0.99, 0.01, "Source: district forecasts via The Vindicator (Feb and May 2026)",
            ha="right", fontsize=8)
plt.tight_layout(rect=(0, 0.03, 1, 1))
plt.savefig("canfield_reserve_days.png")
plt.show()