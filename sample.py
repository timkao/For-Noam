import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

# Choose the stocks we want to see and lenghth of the data.
stock_set = ['AAPL', 'MSFT', 'ITW']
begin_date = '1/1/2002'
functions = ['mean', 'std']

# Base on the information above. Get the data from Yahoo Finance. We check the adjusted stock price grouped by year.
data_g = web.get_data_yahoo(stock_set, begin_date)
data2 = data_g['Adj Close'].groupby(lambda x: x.year).agg(functions)

# Draw the average stock price and the standard deviation of the price by year. 
data_fig = data2.unstack().swaplevel(0, 1).unstack(0).unstack(0)
fig, axes = plt.subplots(1, 2)
data_fig[functions[0]].plot(kind = 'line', ax=axes[0], color=['r', 'b', 'k'], 
							alpha = 0.7, title = 'Stock Price Mean', marker = 'o', linestyle = 'dashed', grid = True)
data_fig[functions[1]].plot(kind = 'bar',  ax=axes[1], color=['r', 'b', 'k'], 
							alpha = 0.5, stacked = False, title = 'Standard Deviation', grid = True)

# Use least squares regression to perform factor analysis on stock returns 
data3 = data_g['Adj Close'].pct_change().dropna()
data3[stock_set[1:]].corrwith(data3[stock_set[0]])
pd.ols(y = data3[stock_set[0]], x = data3[stock_set[1:]])
