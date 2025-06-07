# modules/chart_annotations.py

import plotly.graph_objects as go

def plot_candlestick_with_indicators(df):
    fig = go.Figure()

    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=df['Datetime'] if 'Datetime' in df.columns else df['Date'],
        open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'],
        name='Candlestick'
    ))

    # Bollinger Bands
    fig.add_trace(go.Scatter(x=df.index, y=df['BB_upper'], mode='lines', name='BB Upper'))
    fig.add_trace(go.Scatter(x=df.index, y=df['BB_lower'], mode='lines', name='BB Lower'))

    # Volume bars
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume', opacity=0.3))

    # Annotations for patterns
    for i, row in df.iterrows():
        if row['Hammer']:
            fig.add_trace(go.Scatter(
                x=[i], y=[row['High']],
                mode="text", text=["Hammer"],
                textposition="top center", name="Hammer", textfont=dict(color="red")
            ))
        if row['Doji']:
            fig.add_trace(go.Scatter(
                x=[i], y=[row['High']],
                mode="text", text=["Doji"],
                textposition="top center", name="Doji", textfont=dict(color="blue")
            ))

    fig.update_layout(xaxis_rangeslider_visible=False)
    return fig
