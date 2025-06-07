# modules/data_fetch.py

import yfinance as yf
import pandas as pd

def fetch_data(symbol, period="5d", interval="5m"):
    try:
        df = yf.download(tickers=symbol, period=period, interval=interval, progress=False)
        df.dropna(inplace=True)
        df.reset_index(inplace=True)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
