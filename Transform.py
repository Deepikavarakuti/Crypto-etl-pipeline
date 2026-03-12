import pandas as pd
from datetime import datetime

def transform_data(df):
    
    df["timestamp"] = datetime.now()

    df["crypto_name"] = df["crypto_name"].str.upper()

    return df