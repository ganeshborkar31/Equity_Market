import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def load_data(user_input):
    # Assuming input is a CSV file with 'ds' for dates and 'y' for values
    data = pd.read_csv(user_input)
    data['ds'] = pd.to_datetime(data['ds'])
    data.set_index('ds', inplace=True)
    return data

def decompose_time_series(series, model='additive', period=30):
    result = seasonal_decompose(series, model=model, period=period)
    return result

def plot_components(result):
    fig, axs = plt.subplots(4, 1, figsize=(10, 8))
    axs[0].plot(result.observed)
    axs[0].set_title('Original Data')
    axs[1].plot(result.trend.dropna())
    axs[1].set_title('Trend')
    axs[2].plot(result.seasonal.dropna())
    axs[2].set_title('Seasonality')
    axs[3].plot(result.resid.dropna())
    axs[3].set_title('Residuals')
    for ax in axs:
        ax.set_xlabel('Date')
    plt.tight_layout()
    return fig

def main():
    st.title("Manual Time Series Analysis")
    st.sidebar.header("Settings")

    uploaded_file = st.sidebar.file_uploader("Upload your time series CSV", type=["csv"])
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        if st.sidebar.button('Analyze'):
            period = st.sidebar.slider('Select Seasonality Period', min_value=5, max_value=365, value=30)
            model_type = st.sidebar.radio("Select Model Type", ('additive', 'multiplicative'))
            
            st.subheader("Time Series Decomposition")
            result = decompose_time_series(data['y'], model=model_type, period=period)
            fig = plot_components(result)
            st.pyplot(fig)

            st.subheader("Forecast Future Values")
            future_periods = st.sidebar.number_input('Enter number of future periods:', min_value=1, max_value=100, value=20)
            forecast = forecast_future(result.trend.dropna(), result.seasonal, future_periods)
            st.line_chart(forecast)

def forecast_future(trend, seasonality, periods):
    last_value = trend.iloc[-1]
    future_trend = np.linspace(last_value, last_value * (1 + 0.05), periods)  # Simple linear growth assumption
    repeated_seasonality = np.tile(seasonality, int(np.ceil(periods / len(seasonality))))[:periods]
    forecast = future_trend + repeated_seasonality
    return forecast

# if __name__ == "__main__":
#     main()
