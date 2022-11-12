import os
import pandas as pd
from pathlib import Path

#list all the files from the directory (relative path)
path = Path(__file__).parent/"fixtures"
print(path)
file_list = os.listdir(path)
combineFileName = "combined.csv"

# make sure combined.csv is not there or it will throw FileNotFound error at line14
if combineFileName in file_list:
    file_list.remove(combineFileName)

# relative path
df = pd.concat([pd.read_csv(path /fp).assign(filename=os.path.basename(fp).split('.')[0]) for fp in file_list])

file_path = path /combineFileName

df.to_csv(file_path, index = False)
print("successfully saved!")


    