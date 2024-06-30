import streamlit as st 
import yfinance as yf
import requests

#Initial UI
# def fund(sym):

#     ticker = st.text_input('Ticker', sym).upper()
#     buttonClicked = st.button('Set')

#     #Callbacks
#     if buttonClicked:
#         requestString = f"""https://query1.finance.yahoo.com/v10/...{ticker}?modules=assetProfile%2Cprice"""
#         request = requests.get(f"{requestString}", headers={"USER-AGENT": "Mozilla/5.0"})
#         json = request.json()
#         data = json["quoteSummary"]["result"][0]

#         st.header("Profile")

#         st.metric("sector", data["assetProfile"]["sector"])
#         st.metric("industry", data["assetProfile"]["industry"])
#         st.metric("website", data["assetProfile"]["website"])
#         st.metric("marketCap", data["price"]["marketCap"]["fmt"])

#         with st.expander("About Company"):
#             st.write(data["assetProfile"]["longBusinessSummary"])

def get_market_cap(stock):
    # Create a ticker object
    #stock = yf.Ticker(stock)
    
    # Fetch market cap
    market_cap = stock.info['marketCap']
    
    return market_cap


def load_info(sym):
    try:
        info = sym.info
    except:
        st.subheader("Check Network Connection ")
    else :
        return info

def display_fundamentals(info):
    st.write("### Company Overview")
    
    if st.button("Overview"):
        st.write(info.get('longBusinessSummary'))
        
    if st.button("Key Financial Metrics"):
        metrics = {
            "Market Cap": info.get('marketCap'),
            "Price-to-Earnings Ratio (PE)": info.get('trailingPE'),
            "Price-to-Book Ratio (PB)": info.get('priceToBook'),
            "Dividend Yield": info.get('dividendYield'),
            "Return on Equity": info.get('returnOnEquity'),
            "Profit Margins": info.get('profitMargins'),
            "Earnings Growth": info.get('earningsGrowth')
        }

        st.write("### Key Financial Metrics")
        for key, value in metrics.items():
            st.metric(label=key, value=value)

def dsp_fundamental(sym):
    st.title("Stock Fundamental Analysis")
    info = load_info(sym)
    display_fundamentals(info)
    

