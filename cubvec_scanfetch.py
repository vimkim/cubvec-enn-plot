import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# CSV data
csv_data = """repeat,limit,dbname,tablename,metric,stat,value
10,50000,testdb,tbl_256_300000,SCAN TIME,avg,27
10,100000,testdb,tbl_256_300000,SCAN TIME,avg,50
10,150000,testdb,tbl_256_300000,SCAN TIME,avg,56
10,250000,testdb,tbl_256_300000,SCAN TIME,avg,89
10,300000,testdb,tbl_256_300000,SCAN TIME,avg,122
10,50000,testdb,tbl_768_300000,SCAN TIME,avg,58
10,100000,testdb,tbl_768_300000,SCAN TIME,avg,95
10,150000,testdb,tbl_768_300000,SCAN TIME,avg,135
10,200000,testdb,tbl_768_300000,SCAN TIME,avg,268
10,250000,testdb,tbl_768_300000,SCAN TIME,avg,267
10,300000,testdb,tbl_768_300000,SCAN TIME,avg,404
10,50000,testdb,tbl_1536_150000,SCAN TIME,avg,126
10,100000,testdb,tbl_1536_150000,SCAN TIME,avg,232
10,150000,testdb,tbl_1536_150000,SCAN TIME,avg,281
10,200000,testdb,tbl_256_300000,SCAN TIME,avg,67
"""

# Load data
df = pd.read_csv(StringIO(csv_data))

# Pivot data
pivot_df = df.pivot(index="limit", columns="tablename", values="value")

# Plot and save
pivot_df.plot(marker="o")
plt.title("SEQ SCAN TIME vs Limit by Table")
plt.xlabel("Limit")
plt.ylabel("SEQ SCAN TIME (avg)")
plt.grid(True)
plt.legend(title="Table Name")
plt.tight_layout()

# Save the figure
plt.savefig("cubvec_seq_scan_time.png", dpi=300)
