import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# CSV data
csv_data = """repeat,limit,dbname,tablename,metric,stat,value
10,50000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,9.8162
10,100000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,18.323
10,150000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,28.4616
10,200000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,36.4844
10,250000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,45.3424
10,300000,vimkimdb,tbl_256_300000,SEQ SCAN TIME,avg,55.3428
10,50000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,3.6382
10,100000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,7.3042
10,150000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,11.049
10,200000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,14.8494
10,250000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,18.775
10,300000,vimkimdb,tbl_768_300000,SEQ SCAN TIME,avg,22.315
10,50000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,avg,3.8845
10,100000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,avg,7.8715
10,150000,vimkimdb,tbl_1536_150000,SEQ SCAN TIME,avg,11.7393
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
plt.savefig("pg_seq_scan_time.png", dpi=300)
