import pandas as pd

def load_data():
    df = pd.read_csv("/melb_data.csv")
    return df