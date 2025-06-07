# modules/patterns.py

def detect_patterns(df):
    # Simple Hammer pattern detection
    def is_hammer(row):
        body = abs(row['Close'] - row['Open'])
        lower_shadow = min(row['Open'], row['Close']) - row['Low']
        return lower_shadow > 2 * body

    # Simple Doji pattern detection
    def is_doji(row):
        return abs(row['Close'] - row['Open']) <= (0.1 * (row['High'] - row['Low']))

    df['Hammer'] = df.apply(is_hammer, axis=1)
    df['Doji'] = df.apply(is_doji, axis=1)

    return df
