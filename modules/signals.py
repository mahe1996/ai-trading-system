# modules/signals.py

def generate_signal(df):
    last = df.iloc[-1]

    signal = "Neutral"

    if last['RSI'] < 30 and last['ADX'] > 20 and last['Close'] > last['BB_lower']:
        signal = "Potential BUY Signal"
    elif last['RSI'] > 70 and last['ADX'] > 20 and last['Close'] < last['BB_upper']:
        signal = "Potential SELL Signal"
    else:
        signal = "Neutral / No Clear Signal"

    return signal
