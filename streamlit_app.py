# !pip install streamlit yfinance
# !pip install yfinance

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# 設定股票代碼
ticker = '2330.TW'

# 顯示標題
st.title(f"{ticker} 2330.TW")

# 下載資料
data = yf.download(ticker, period='3y')

# 顯示股價資料
st.write("Stock Price：", data.tail())

# 繪製收盤價走勢圖
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data.index, data['Close'], label='Close', color='blue')
ax.set_title(f'{ticker} 2330.TW - lasted 3 years')
ax.set_xlabel('date')
ax.set_ylabel('close (TWD)')
ax.legend()
ax.grid(True)
st.pyplot(fig)
