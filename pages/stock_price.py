import pandas as pd
import plotly.express as px
import requests
import streamlit as st
import urllib3

urllib3.disable_warnings()


def get_stock_data(url, param, data_res):
    try:
        response = requests.get(url=url, params=param, verify=False)
        response.raise_for_status()
        st.session_state.stock_data = response.json()[data_res]
    except requests.exceptions.RequestException as e:
        st.write(f"Request Failed: {e}")
        st.session_state.stock_data = "Invalid Ticker"


API_ENDPOINT = st.secrets["ALPHA_VANTAGE_ENDPOINT"]
API_KEY = st.secrets["ALPHA_VANTAGE_API_KEY"]
data_time = ["TIME_SERIES_DAILY", "TIME_SERIES_WEEKLY", "TIME_SERIES_MONTHLY"]
data_response = ["Time Series (Daily)", "Weekly Time Series", "Monthly Time Series"]
data_values = []

st.title("Stock Price App")
st.text_input(label="", label_visibility="hidden", key="ticker", placeholder="Enter the ticker")
st.selectbox(label="Select time", options=["", "Last 100 days", "Last 100 weeks", "Last 100 months"], key="duration")

if st.session_state.duration == "Last 100 days":
    data_time = data_time[0]
    data_response = data_response[0]

elif st.session_state.duration == "Last 100 weeks":
    data_time = data_time[1]
    data_response = data_response[1]

elif st.session_state.duration == "Last 100 months":
    data_time = data_time[2]
    data_response = data_response[2]

if st.session_state.ticker:
    params = {
        "function": data_time,
        "symbol": st.session_state.ticker,
        "datatype": "json",
        "apikey": API_KEY
    }
else:
    params = {}
st.button(label="Get Stock Price", key="get_stock_price", on_click=get_stock_data,
          args=(API_ENDPOINT, params, data_response))
if "stock_data" in st.session_state:
    stock_data = st.session_state.stock_data
    if isinstance(stock_data, dict):
        df = pd.DataFrame.from_dict(stock_data, orient="index")
        df = df.reset_index().rename(columns={'index': 'Date'})
        df['Date'] = pd.to_datetime(df['Date'])
        df['4. close'] = df['4. close'].astype(float).map(lambda x: f'{x:.2f}')
        fig = px.line(df, x='Date', y='4. close', title='Stock Price over Time')
        st.plotly_chart(fig)
    else:
        st.write(stock_data)
