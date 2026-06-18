import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download stock data (Alphabet Inc. - Google)
stock = yf.download("GOOGL", start="2023-01-01", end="2023-12-31")

# Line plot of Closing price
plt.figure()
plt.plot(stock.index, stock["Close"])
plt.title("Alphabet Inc. Stock Price")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.xticks(rotation=45)
plt.show()
