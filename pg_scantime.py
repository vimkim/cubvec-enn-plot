import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# CSV data provided by the user
csv_data = """repeat,limit,dbname,tablename,metric,stat,value
10,50000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,9.8162
10,50000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,min,9.043
10,50000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,max,13.376
10,50000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,median,9.459
10,100000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,18.323
10,100000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,min,17.817
10,100000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,max,18.572
10,100000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,median,18.379
10,150000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,28.4616
10,150000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,min,27.096
10,150000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,max,36.875
10,150000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,median,27.383
10,200000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,36.4844
10,200000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,min,36.228
10,200000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,max,36.88
10,200000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,median,36.438
10,250000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,45.3424
10,250000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,min,44.857
10,250000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,max,46.651
10,250000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,median,45.204
10,300000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,55.3428
10,300000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,min,54.335
10,300000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,max,57.894
10,300000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,median,54.929
10,50000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,3.6382
10,50000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,min,3.513
10,50000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,max,3.808
10,50000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,median,3.666
10,100000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,7.3042
10,100000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,min,7.145
10,100000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,max,7.445
10,100000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,median,7.341
10,150000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,11.049
10,150000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,min,10.811
10,150000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,max,11.365
10,150000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,median,11.01
10,200000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,14.8494
10,200000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,min,14.689
10,200000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,max,15.318
10,200000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,median,14.801
10,250000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,18.775
10,250000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,min,18.267
10,250000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,max,19.725
10,250000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,median,18.615
10,300000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,22.315
10,300000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,min,21.67
10,300000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,max,24.142
10,300000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,median,22.08
10,50000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,avg,3.8845
10,50000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,min,3.831
10,50000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,max,3.948
10,50000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,median,3.89
10,100000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,avg,7.8715
10,100000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,min,7.715
10,100000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,max,8.256
10,100000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,median,7.821
10,150000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,avg,11.7393
10,150000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,min,11.589
10,150000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,max,12.22
10,150000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,median,11.659
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
    sub_df = df[(df["tablename"] == table) & (df["metric"] == "SEQ SCAN TIME")]

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
plt.savefig("pg_scantime.png", dpi=300)
