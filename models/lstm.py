import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

def create_lstm_model(data):
    # Prepare data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.reshape(-1, 1))

    # Create the LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(scaled_data.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))  # Prediction of the next closing value

    model.compile(optimizer='adam', loss='mean_squared_error')
    return model, scaler

# Data should be the closing prices vector
# Example: data = np.array(df['Close'])



from prophet import Prophet

def train_prophet_model(dataframe):
    model = Prophet(daily_seasonality=True)
    model.fit(dataframe)
    return model



import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
import matplotlib.pyplot as plt

def load_data(ticker):
    data = yf.download(ticker, start="2019-01-01", end="2024-01-01")
    return data

def main():
    st.title("Stock Price Prediction Using LSTM and Prophet")

    ticker = st.text_input("Enter Stock Ticker", value='AAPL')
    data = load_data(ticker)

    if st.button("Predict with LSTM"):
        model, scaler = create_lstm_model(data['Close'].values)
        # Add your training and prediction logic here
        st.write("Prediction results from LSTM...")

    if st.button("Predict with Prophet"):
        df_prophet = pd.DataFrame(data.index)
        df_prophet.columns = ['ds']
        df_prophet['y'] = data['Close'].values
        model = train_prophet_model(df_prophet)
        future = model.make_future_dataframe(periods=365)
        forecast = model.predict(future)
        fig1 = plot_plotly(model, forecast)
        st.plotly_chart(fig1)

if __name__ == "__main__":
    main()
