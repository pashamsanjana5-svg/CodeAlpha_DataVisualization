import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sp500_companie.csv")

# Chart 1: Companies by Sector
sector_counts = df["Sector"].value_counts()

plt.figure(figsize=(10,6))
sector_counts.plot(kind="bar")
plt.title("Number of Companies by Sector")
plt.xlabel("Sector")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig("sector_bar_chart.png")
plt.show()

# Chart 2: Sector Share Pie Chart
plt.figure(figsize=(8,8))
sector_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sector Distribution in S&P 500")
plt.ylabel("")
plt.tight_layout()
plt.savefig("sector_pie_chart.png")
plt.show()

# Chart 3: Top 10 Headquarters Locations
top_hq = df["Headquarters"].value_counts().head(10)

plt.figure(figsize=(10,6))
top_hq.plot(kind="bar")
plt.title("Top 10 Headquarters Locations")
plt.xlabel("Location")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig("top_headquarters_chart.png")
plt.show()

print("Charts created successfully!")