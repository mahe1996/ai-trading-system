# modules/indicators.py

import pandas_ta as ta

def add_indicators(df):
    # Bollinger Bands
    bb = ta.bbands(df['Close'], length=20)
    df['BB_upper'] = bb['BBU_20_2.0']
    df['BB_lower'] = bb['BBL_20_2.0']

    # RSI
    df['RSI'] = ta.rsi(df['Close'], length=14)

    # ATR
    df['ATR'] = ta.atr(df['High'], df['Low'], df['Close'], length=14)

    # ADX
    adx = ta.adx(df['High'], df['Low'], df['Close'], length=14)
    df['ADX'] = adx['ADX_14']

    # Volume SMA20
    df['Volume_SMA20'] = df['Volume'].rolling(window=20).mean()

    return df
