import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download stock data
stock = yf.download("GOOGL", start="2023-01-01", end="2023-03-31")

# If columns are MultiIndex, flatten them
if isinstance(stock.columns, pd.MultiIndex):
    stock.columns = stock.columns.get_level_values(0)

# Bar plot of Volume
plt.figure()
plt.bar(stock.index, stock["Volume"])
plt.title("Alphabet Inc. Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
