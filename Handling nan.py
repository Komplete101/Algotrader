# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:17:17 2023

@author: Chiboy
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AAPL","MSFT","NVDA","INTC", "AMD", "BBY","FB"]
start = dt.datetime.today()-dt.timedelta(days=3650)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohlcv_data = {}

for stock in stocks:
    cl_price[stock] = yf.download(stock,start,end)["Adj Close"]
    
#cl_price.fillna(method = "bfill",axis=0,inplace=True)

cl_price.dropna(axis=0,how="any",inplace = True)