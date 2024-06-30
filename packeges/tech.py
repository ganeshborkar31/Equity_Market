# aal_df['std_close'] = aal_df["close"].rolling(5).std()
# aal_df['mean_close'] = aal_df["close"].rolling(5).mean()
# aal_df['twenty_mean_close'] = aal_df["close"].rolling(20).mean()

# f, (std_ax, avg_ax) = plt.subplots(1, 2, figsize=(18,5))

# std_ax.plot(aal_df["date"], aal_df["std_close"], color="r", label="Standard Deviation")
# std_ax.legend(loc="upper left")
# std_ax.set_title("Standard Deviation American Airlines \n (AAL)")

# avg_ax.plot(aal_df["date"], aal_df["mean_close"], color="g", label="5-day MA")
# avg_ax.plot(aal_df["date"], aal_df["twenty_mean_close"], color="k", label="20-day MA")
# avg_ax.legend(loc="upper left")
# avg_ax.set_title("5 Day Average AAL \n Closing Price")
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import streamlit as st
import ta
# import yfinance as yf


def normalized(close,high,low,date):
    
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18,5))

    close_normalized = np.log(close)
    high_normalized = np.log(high)
    low_normalized = np.log(low)

    ax1.plot(date, close_normalized)
    ax1.set_title("Normalized Close Price")
    ax2.plot(date, high_normalized, color="g")
    ax2.set_title("Normalized High Price")
    ax3.plot(date,low_normalized, color="r")
    ax3.set_title("Normalized Low Price")
    st.pyplot(f)
    


def load_data(ticker):
    data = yf.download(ticker, start="2020-01-01", end="2024-01-01")
    return data

def plot_data(data, indicator_data=None, title="Stock Prices"):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'],data['Close'],label='Close Price',color='black')
    if indicator_data is not None:
        plt.plot(data['Date'] ,indicator_data,label=indicator_data.name, alpha=0.7,color='r')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

def tech_analysis(data,symbol):
    st.title("Stock Technical Analysis")

    # Sidebar for user inputs
    #ticker = st.sidebar.text_input("Enter Stock Ticker", value='AAPL')
    selected_indicator = st.selectbox("Select Indicator", ["None", "SMA", "EMA"])
    ticker=symbol
    # Load data
    #data = load_data(ticker)

    if selected_indicator == "None":
        plot_data(data)
    if selected_indicator == "SMA":
        sma_window = st.slider("SMA Window", min_value=5, max_value=60, value=20)
        data['SMA'] = ta.trend.sma_indicator(data['Close'], window=sma_window)
        plot_data(data, data['SMA'], title=f"{ticker} with SMA")
    if selected_indicator == "EMA":
        ema_window = st.slider("EMA Window", min_value=5, max_value=60, value=20)
        data['EMA'] = ta.trend.ema_indicator(data['Close'], window=ema_window)
        plot_data(data, data['EMA'], title=f"{ticker} with EMA")
    if selected_indicator == "RSI":
        rsi_window = st.sidebar.slider("RSI Window", min_value=5, max_value=30, value=14)
        data['RSI'] = ta.momentum.rsi(data['Close'], window=rsi_window)
        plot_data(data['Close'])
        st.write("RSI Chart:")
        st.line_chart(data['RSI'])



    
    
    