import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# CSV data provided by the user
csv_data = """repeat,limit,dbname,tablename,metric,stat,value
10,50000,testdb,tbl_256_300000,SCAN TIME,avg,27
10,50000,testdb,tbl_256_300000,SCAN TIME,min,22
10,50000,testdb,tbl_256_300000,SCAN TIME,max,34
10,50000,testdb,tbl_256_300000,SCAN TIME,median,27
10,100000,testdb,tbl_256_300000,SCAN TIME,avg,50
10,100000,testdb,tbl_256_300000,SCAN TIME,min,43
10,100000,testdb,tbl_256_300000,SCAN TIME,max,57
10,100000,testdb,tbl_256_300000,SCAN TIME,median,50
10,150000,testdb,tbl_256_300000,SCAN TIME,avg,56
10,150000,testdb,tbl_256_300000,SCAN TIME,min,37
10,150000,testdb,tbl_256_300000,SCAN TIME,max,98
10,150000,testdb,tbl_256_300000,SCAN TIME,median,53
10,250000,testdb,tbl_256_300000,SCAN TIME,avg,89
10,250000,testdb,tbl_256_300000,SCAN TIME,min,74
10,250000,testdb,tbl_256_300000,SCAN TIME,max,155
10,250000,testdb,tbl_256_300000,SCAN TIME,median,78
10,300000,testdb,tbl_256_300000,SCAN TIME,avg,122
10,300000,testdb,tbl_256_300000,SCAN TIME,min,90
10,300000,testdb,tbl_256_300000,SCAN TIME,max,157
10,300000,testdb,tbl_256_300000,SCAN TIME,median,125
10,50000,testdb,tbl_768_300000,SCAN TIME,avg,58
10,50000,testdb,tbl_768_300000,SCAN TIME,min,45
10,50000,testdb,tbl_768_300000,SCAN TIME,max,66
10,50000,testdb,tbl_768_300000,SCAN TIME,median,60
10,100000,testdb,tbl_768_300000,SCAN TIME,avg,95
10,100000,testdb,tbl_768_300000,SCAN TIME,min,86
10,100000,testdb,tbl_768_300000,SCAN TIME,max,115
10,100000,testdb,tbl_768_300000,SCAN TIME,median,94
10,150000,testdb,tbl_768_300000,SCAN TIME,avg,135
10,150000,testdb,tbl_768_300000,SCAN TIME,min,127
10,150000,testdb,tbl_768_300000,SCAN TIME,max,153
10,150000,testdb,tbl_768_300000,SCAN TIME,median,133
10,200000,testdb,tbl_768_300000,SCAN TIME,avg,268
10,200000,testdb,tbl_768_300000,SCAN TIME,min,200
10,200000,testdb,tbl_768_300000,SCAN TIME,max,316
10,200000,testdb,tbl_768_300000,SCAN TIME,median,266
10,250000,testdb,tbl_768_300000,SCAN TIME,avg,267
10,250000,testdb,tbl_768_300000,SCAN TIME,min,175
10,250000,testdb,tbl_768_300000,SCAN TIME,max,350
10,250000,testdb,tbl_768_300000,SCAN TIME,median,300
10,300000,testdb,tbl_768_300000,SCAN TIME,avg,404
10,300000,testdb,tbl_768_300000,SCAN TIME,min,386
10,300000,testdb,tbl_768_300000,SCAN TIME,max,430
10,300000,testdb,tbl_768_300000,SCAN TIME,median,403
10,50000,testdb,tbl_1536_150000,SCAN TIME,avg,126
10,50000,testdb,tbl_1536_150000,SCAN TIME,min,112
10,50000,testdb,tbl_1536_150000,SCAN TIME,max,138
10,50000,testdb,tbl_1536_150000,SCAN TIME,median,125
10,100000,testdb,tbl_1536_150000,SCAN TIME,avg,232
10,100000,testdb,tbl_1536_150000,SCAN TIME,min,169
10,100000,testdb,tbl_1536_150000,SCAN TIME,max,283
10,100000,testdb,tbl_1536_150000,SCAN TIME,median,257
10,150000,testdb,tbl_1536_150000,SCAN TIME,avg,281
10,150000,testdb,tbl_1536_150000,SCAN TIME,min,233
10,150000,testdb,tbl_1536_150000,SCAN TIME,max,396
10,150000,testdb,tbl_1536_150000,SCAN TIME,median,259
10,200000,testdb,tbl_256_300000,SCAN TIME,avg,67
10,200000,testdb,tbl_256_300000,SCAN TIME,min,40
10,200000,testdb,tbl_256_300000,SCAN TIME,max,79
10,200000,testdb,tbl_256_300000,SCAN TIME,median,72
"""

# Load the data into a DataFrame
df = pd.read_csv(StringIO(csv_data))

# Ensure the data types are correct
df["limit"] = df["limit"].astype(int)
df["value"] = df["value"].astype(float)

# Unique table names
tables = df["tablename"].unique()

# Color palette for different tables
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple"]

plt.figure(figsize=(10, 6))

for idx, table in enumerate(tables):
    sub_df = df[(df["tablename"] == table) & (df["metric"] == "SCAN TIME")]

    # Pivot to get stats in columns for easy plotting
    pivot_df = sub_df.pivot(index="limit", columns="stat", values="value").sort_index()

    limits = pivot_df.index
    avg_values = pivot_df["avg"]
    min_values = pivot_df["min"]
    max_values = pivot_df["max"]
    median_values = pivot_df["median"]

    color = colors[idx % len(colors)]

    # Plot average scan time
    plt.plot(limits, avg_values, marker="o", color=color, label=f"{table} Avg")
    # Plot candle-like vertical lines for min and max
    plt.vlines(
        limits,
        min_values,
        max_values,
        color=color,
        linewidth=2,
        alpha=0.6,
        label=f"{table} Min/Max",
    )
    # Plot median values
    plt.scatter(
        limits, median_values, marker="x", color=color, s=80, label=f"{table} Median"
    )

# Labels and title
plt.xlabel("Limit")
plt.ylabel("Scan Time")
plt.title("Scan Time vs Limit for All Tables")
plt.legend(ncol=3, fontsize=8)
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.savefig("cubvec_scantime.png", dpi=300)
