# app.py

import streamlit as st
import pandas as pd
import pandas_ta as ta
import plotly.graph_objects as go

from modules.data_fetch import fetch_data
from modules.indicators import add_indicators
from modules.patterns import detect_patterns
from modules.signals import generate_signal
from modules.chart_annotations import plot_candlestick_with_indicators

st.set_page_config(page_title="AI Technical Analysis System", layout="wide")
st.title("AI Powered TradingView - Technical Analysis System")

# User input controls
symbol = st.text_input("Enter Stock Ticker (eg: AAPL, RELIANCE.NS):", value="RELIANCE.NS")
period = st.selectbox("Select Period:", ["1d", "5d", "1mo", "3mo", "6mo", "1y"])
interval = st.selectbox("Select Interval:", ["1m", "5m", "15m", "30m", "60m", "1d"])

if st.button("Analyze"):
    df = fetch_data(symbol, period, interval)
    
    if df.empty:
        st.error("No data fetched. Please check the symbol or interval.")
    else:
        df = add_indicators(df)
        df = detect_patterns(df)
        signal = generate_signal(df)

        st.subheader("Detected Trading Signal:")
        st.success(signal)

        st.subheader("Indicators & Patterns Table:")
        st.dataframe(df.tail(20))

        st.subheader("Candlestick Chart with Annotations:")
        fig = plot_candlestick_with_indicators(df)
        st.plotly_chart(fig, use_container_width=True)
