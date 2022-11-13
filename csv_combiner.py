import sys
import os
import pandas as pd
from pathlib import Path

def csv_combine(relative_path = __file__, file_list = None): 
    if file_list is None:
        file_list = sys.argv[1:]
    
    df = pd.concat([pd.read_csv(Path(relative_path).parent/fp).assign(filename=os.path.basename(fp).split('/')[-1].split('.')[0]) for fp in file_list])
    
    root = Path(relative_path).parent/"fixtures/combined.csv"
    df.to_csv(root, index = False)
    
    print("successfully saved!")

if __name__ == "__main__": 
    csv_combine()
    
    