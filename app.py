import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("📊 Stock Dashboard")

ticker = st.text_input("Enter Stock", "AAPL")

data = yf.download(ticker, start="2023-01-01")

st.write(data.tail())

fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name="Close"))

st.plotly_chart(fig)
