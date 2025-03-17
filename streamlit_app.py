!pip install streamlit yfinance

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# 設定股票代碼
ticker = '2330.TW'

# 顯示標題
st.title(f"{ticker} 台積電股價走勢")

# 下載資料
data = yf.download(ticker, period='3y')

# 顯示股價資料
st.write("股價資料：", data.tail())

# 繪製收盤價走勢圖
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data.index, data['Close'], label='收盤價', color='blue')
ax.set_title(f'{ticker} 台積電股價走勢 - 過去3年')
ax.set_xlabel('日期')
ax.set_ylabel('收盤價 (TWD)')
ax.legend()
ax.grid(True)
st.pyplot(fig)
