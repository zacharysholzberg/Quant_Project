#src/utils.py

import pandas as pd

def read_data(name):
    return pd.read_csv(f"/Users/zacharysholzberg/Desktop/Quant_Project/data/{name}.csv")