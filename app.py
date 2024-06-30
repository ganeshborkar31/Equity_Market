from datetime import datetime
import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

import streamlit as st
from streamlit_option_menu import option_menu

from pandas_datareader import data as pdr
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

###  pakages 
from packeges import tech
from packeges import about
from packeges import fundament
from packeges import account
from packeges import home
from packeges import disclaimer


st.set_page_config(
    page_title="Stock Price Predictor",
    page_icon="📈 ",
)


# nse=pd.read_csv('/home/ganesh/Projects/BE_Project/NSE.csv')
# symbols=np.array(nse["Symbol"])

# symbol = st.sidebar.selectbox('Select dataset for prediction', symbols)

# st.title("Predictive Analysys for "+ symbol)
# symbol = symbol+'.NS'



#stock = st.text_input("Enter the Stock ID", "TCS.NS") 
       

def run():
    # app = st.sidebar(
    with st.sidebar:        
        app = option_menu(
            menu_title='Menu ',
            options=['Home','Account','about','Disclaimer'],
            icons=['house-fill','person-circle','info-circle-fill',	'warning','⚠️'],
            menu_icon='chat-text-fill',
            default_index=1,
            
    #         styles={
    #             "container": {"padding": "5!important","background-color":'black'},
    # "icon": {"color": "white", "font-size": "23px"}, 
    # "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
    # "nav-link-selected": {"background-color": "#02ab21"},}
            
            )
    if app == "Home":
        try:
            home.home_def()
        except IndexError as e:
            st.write(e) 
            
    if app == 'about':
        about.aboutus() 
    if app == 'Account':
        account.acc()
        
    if app == 'Disclaimer':
        disclaimer.display_disclaimer()
    
    
    
run() 
 


# sym=yf.Ticker(symbol)
# end = datetime.now()
# start = datetime(end.year-20,end.month,end.day)
# #interval
# #period


# @st.cache_data
# def load_data(ticker):
#     data = yf.download(ticker, start, end)
#     data.reset_index(inplace=True)
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(symbol)
# #data_load_state.text('Loading data... done!')


# def calculate_price_difference(stock_data):
#     latest_price = stock_data.iloc[-1]["Close"]
#     previous_year_price = stock_data.iloc[-252]["Close"] if len(stock_data) > 252 else stock_data.iloc[0]["Close"]
#     price_difference = latest_price - previous_year_price
#     percentage_difference = (price_difference / previous_year_price) * 100
#     return price_difference, percentage_difference



# if data is not None:
#     price_difference, percentage_difference = calculate_price_difference(data)
#     latest_close_price = data.iloc[-1]["Close"]
#     max_52_week_high = data["High"].tail(252).max()
#     min_52_week_low = data["Low"].tail(252).min()

#     col1, col2, col3, col4 = st.columns(4)
# #     with col0:
# #         st.metric("Market Capital", f"₹{market_cap:.2f}")
#     with col1:
#         st.metric("Close Price", f"₹{latest_close_price:.2f}")
#     with col2:
#         st.metric("Price Difference (YoY)", f"₹{price_difference:.2f}", f"{percentage_difference:+.2f}%")
#     with col3:
#         st.metric("52-Week High", f"₹{max_52_week_high:.2f}")
#     with col4:
#         st.metric("52-Week Low", f"₹{min_52_week_low:.2f}")
        
        
# forecasting,fundamental,technical = st.tabs(['Forecasting','Fundamental','Technical'])

# with forecasting:
#     st.write("fore")

#     n_years = st.slider('Years of prediction:', 1, 5)
#     period = n_years * 365

#     st.subheader("Candlestick Chart")
#     candlestick_chart = go.Figure(data=[go.Candlestick(x=data['Date'], open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])])
#     candlestick_chart.update_layout(title=f"{symbol} Candlestick Chart", xaxis_rangeslider_visible=False)
#     st.plotly_chart(candlestick_chart, use_container_width=True)

#     st.subheader("Summary")
#     st.dataframe(data.tail())

#     # st.subheader('Raw data')
#     # st.write(data.tail())


#     # Plot raw data
#     def plot_raw_data():
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
#         fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
#         fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
#         st.plotly_chart(fig)
        
#     plot_raw_data()

#     # Predict forecast with Prophet.
#     df_train = data[['Date','Close']]
#     df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

#     m = Prophet()
#     m.fit(df_train)
#     future = m.make_future_dataframe(periods=period)
#     forecast = m.predict(future)

#     # Show and plot forecast
#     st.subheader('Forecast data')
#     st.write(forecast.tail())
        
#     st.subheader(f'Forecast Plot for {n_years} years')
#     fig1 = plot_plotly(m, forecast)
#     st.plotly_chart(fig1,use_container_width=True)

#     st.write("Forecast Components")
#     fig2 = m.plot_components(forecast)
#     st.write(fig2)

# with fundamental :
    
#     #st.write(fundament.get_market_cap(sym))
#     st.metric("Market Cap", f"₹{fundament.get_market_cap(sym):.2f}")
    
#     fundament.fund(symbol)
#     st.subheader('Balance Sheet')
#     bs=sym.balance_sheet
#     st.dataframe(bs)
    
#     st.subheader('Cash Flow')
#     bs=sym.cashflow
#     st.dataframe(bs)
    
#     st.subheader('Income Statement')
#     bs=sym.income_stmt
#     st.dataframe(bs)
    
# with technical:
#     st.write("tech")
    
#     # aal_df['std_close'] = data["close"].rolling(5).std()
#     # aal_df['mean_close'] = data["close"].rolling(5).mean()
#     # aal_df['twenty_mean_close'] = data["close"].rolling(20).mean()

#     f,(std_ax, avg_ax) = plt.subplots(1, 2, figsize=(18,5))

#     std_ax.plot(data["Date"], data["Close"].rolling(5).std(), color="r", label="Standard Deviation")
#     std_ax.legend(loc="upper left")
#     std_ax.set_title("Standard Deviation of Stock  \n")

#     avg_ax.plot(data["Date"], data["Close"].rolling(5).mean(), color="g", label="5-day MA")
#     avg_ax.plot(data["Date"], data["Close"].rolling(20).mean(), color="k", label="20-day MA")
#     avg_ax.legend(loc="upper left")
#     avg_ax.set_title("5 Day Average  \n Closing Price")
    
#     st.pyplot(plt.gcf())
    

#     tech.normalized(data["Close"],data["High"],data["Low"],data["Date"])





























