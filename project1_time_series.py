
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Create Monthly Sales Data
# -----------------------------
dates = pd.date_range(start="2025-01-01", periods=12, freq='ME')
sales = [1200, 1500, 1700, 1600, 1800, 2000, 2100, 1900, 2200, 2500, 2700, 3000]

df = pd.DataFrame({
    "Date": dates,
    "Sales": sales
})

# -----------------------------
# Step 2: Line Chart (Time Series)
# -----------------------------
plt.figure()
plt.plot(df["Date"], df["Sales"], marker='o')
plt.title("Monthly Sales Over Time (2025)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_line_chart.png")
plt.show()

# -----------------------------
# Step 3: Quarterly Aggregation
# -----------------------------
df["Quarter"] = df["Date"].dt.to_period("Q")
quarterly_sales = df.groupby("Quarter")["Sales"].sum()

# -----------------------------
# Step 4: Bar Chart (Category Comparison)
# -----------------------------
plt.figure()
plt.bar(quarterly_sales.index.astype(str), quarterly_sales.values)
plt.title("Quarterly Sales Comparison")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("quarterly_sales_bar_chart.png")
plt.show()

# -----------------------------
# Step 5: Pie Chart (Share Distribution)
# -----------------------------
plt.figure()
plt.pie(
    quarterly_sales.values,
    labels=quarterly_sales.index.astype(str),
    autopct='%1.1f%%'
)
plt.title("Sales Share by Quarter")
plt.tight_layout()
plt.savefig("quarterly_sales_pie_chart.png")
plt.show()

# -----------------------------
# Step 6: Print Summary
# -----------------------------
print("Project Completed Successfully!")
print("\nSummary:")
print("Sales show steady growth throughout the year,")
print("with Q4 contributing the highest share of total revenue.")
