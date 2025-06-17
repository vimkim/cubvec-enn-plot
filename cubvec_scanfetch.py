import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

csv_data = """
repeat,limit,dbname,tablename,metric,stat,value
10,50000,testdb,tbl_256_300000,SCAN FETCH,avg,19296
10,50000,testdb,tbl_256_300000,SCAN FETCH,min,18060
10,50000,testdb,tbl_256_300000,SCAN FETCH,max,20449
10,50000,testdb,tbl_256_300000,SCAN FETCH,median,19201
10,100000,testdb,tbl_256_300000,SCAN FETCH,avg,35120
10,100000,testdb,tbl_256_300000,SCAN FETCH,min,33421
10,100000,testdb,tbl_256_300000,SCAN FETCH,max,37729
10,100000,testdb,tbl_256_300000,SCAN FETCH,median,35294
10,150000,testdb,tbl_256_300000,SCAN FETCH,avg,54247
10,150000,testdb,tbl_256_300000,SCAN FETCH,min,49307
10,150000,testdb,tbl_256_300000,SCAN FETCH,max,72034
10,150000,testdb,tbl_256_300000,SCAN FETCH,median,52331
10,250000,testdb,tbl_256_300000,SCAN FETCH,avg,88645
10,250000,testdb,tbl_256_300000,SCAN FETCH,min,83733
10,250000,testdb,tbl_256_300000,SCAN FETCH,max,107828
10,250000,testdb,tbl_256_300000,SCAN FETCH,median,85719
10,300000,testdb,tbl_256_300000,SCAN FETCH,avg,106032
10,300000,testdb,tbl_256_300000,SCAN FETCH,min,97039
10,300000,testdb,tbl_256_300000,SCAN FETCH,max,116320
10,300000,testdb,tbl_256_300000,SCAN FETCH,median,105239
10,50000,testdb,tbl_768_300000,SCAN FETCH,avg,67709
10,50000,testdb,tbl_768_300000,SCAN FETCH,min,66543
10,50000,testdb,tbl_768_300000,SCAN FETCH,max,69012
10,50000,testdb,tbl_768_300000,SCAN FETCH,median,67982
10,100000,testdb,tbl_768_300000,SCAN FETCH,avg,130318
10,100000,testdb,tbl_768_300000,SCAN FETCH,min,128801
10,100000,testdb,tbl_768_300000,SCAN FETCH,max,134083
10,100000,testdb,tbl_768_300000,SCAN FETCH,median,130060
10,150000,testdb,tbl_768_300000,SCAN FETCH,avg,202411
10,150000,testdb,tbl_768_300000,SCAN FETCH,min,199029
10,150000,testdb,tbl_768_300000,SCAN FETCH,max,208005
10,150000,testdb,tbl_768_300000,SCAN FETCH,median,202534
10,200000,testdb,tbl_768_300000,SCAN FETCH,avg,304342
10,200000,testdb,tbl_768_300000,SCAN FETCH,min,280808
10,200000,testdb,tbl_768_300000,SCAN FETCH,max,312619
10,200000,testdb,tbl_768_300000,SCAN FETCH,median,309143
10,250000,testdb,tbl_768_300000,SCAN FETCH,avg,375661
10,250000,testdb,tbl_768_300000,SCAN FETCH,min,352855
10,250000,testdb,tbl_768_300000,SCAN FETCH,max,401961
10,250000,testdb,tbl_768_300000,SCAN FETCH,median,375720
10,300000,testdb,tbl_768_300000,SCAN FETCH,avg,454667
10,300000,testdb,tbl_768_300000,SCAN FETCH,min,452056
10,300000,testdb,tbl_768_300000,SCAN FETCH,max,459638
10,300000,testdb,tbl_768_300000,SCAN FETCH,median,453688
10,50000,testdb,tbl_1536_150000,SCAN FETCH,avg,141777
10,50000,testdb,tbl_1536_150000,SCAN FETCH,min,134988
10,50000,testdb,tbl_1536_150000,SCAN FETCH,max,143772
10,50000,testdb,tbl_1536_150000,SCAN FETCH,median,142461
10,100000,testdb,tbl_1536_150000,SCAN FETCH,avg,308302
10,100000,testdb,tbl_1536_150000,SCAN FETCH,min,295837
10,100000,testdb,tbl_1536_150000,SCAN FETCH,max,319426
10,100000,testdb,tbl_1536_150000,SCAN FETCH,median,308621
10,150000,testdb,tbl_1536_150000,SCAN FETCH,avg,477383
10,150000,testdb,tbl_1536_150000,SCAN FETCH,min,451712
10,150000,testdb,tbl_1536_150000,SCAN FETCH,max,499946
10,150000,testdb,tbl_1536_150000,SCAN FETCH,median,480845
10,200000,testdb,tbl_256_300000,SCAN FETCH,avg,67532
10,200000,testdb,tbl_256_300000,SCAN FETCH,min,66107
10,200000,testdb,tbl_256_300000,SCAN FETCH,max,69005
10,200000,testdb,tbl_256_300000,SCAN FETCH,median,67429
"""

df = pd.read_csv(StringIO(csv_data))
df = df[df["metric"] == "SCAN FETCH"]

plt.figure(figsize=(12, 6))
for tbl in df["tablename"].unique():
    tbl_df = df[df["tablename"] == tbl]
    pivot = tbl_df.pivot(index="limit", columns="stat", values="value").sort_index()
    for stat in ["avg", "min", "max", "median"]:
        plt.plot(pivot.index, pivot[stat], marker="o", label=f"{tbl} - {stat}")

plt.title("SCAN FETCH Values vs Limit")
plt.xlabel("Limit")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("cubvec_scanfetch.png", dpi=300)
