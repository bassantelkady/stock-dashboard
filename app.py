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

import yfinance as yf

data = yf.download(tickers, period="6mo")['Close']

import plotly.graph_objects as go

fig = go.Figure()

for col in data.columns:
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data[col],
        name=col
    ))

st.plotly_chart(fig, use_container_width=True)




returns = (data.iloc[-1] / data.iloc[0] - 1) * 100

best_stock = returns.idxmax()

st.success(f"🏆 Best Stock: {best_stock} ({returns.max():.2f}%)")



for stock in tickers:
    df = yf.download(stock, period="1y")

    df['MA50'] = df['Close'].rolling(50).mean()
    df['MA200'] = df['Close'].rolling(200).mean()

    if df['MA50'].iloc[-1] > df['MA200'].iloc[-1]:
        st.write(f"📈 {stock}: BUY")
    else:
        st.write(f"📉 {stock}: SELL")


