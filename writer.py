
import os
from datetime import datetime
import pandas as pd

def save_to_parquet(df):
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(f"data/{today}", exist_ok=True)
    symbol = df['symbol'].iloc[0].replace('=X', '')
    path = f"data/{today}/{symbol}.parquet"
    df.to_parquet(path, index=False)
