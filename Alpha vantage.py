# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 21:42:39 2023

@author: Chiboy
"""

from alpha_vantage.timeseries import TimeSeries
import pandas as pd

key_path = open("C:\\Users\\15623\\Documents\\AlphaAPI_key.txt","r").read()

ts  = TimeSeries(key_path, output_format="pandas")
data = ts.get_intraday(symbol="AMZN",outputsize="full")[0]
data.columns = ["open","high","low",'close',"volume"]


all_stocks = ["AAPL", "MSFT","CSCO","AMZN", "INIC"]
close_prices = pd.DataFrame()

for stock in all_stocks:    
    starttime = time.time()
    ts = TimeSeries(key_path, output_format="pandas")
    data = ts.get_intraday(symbol = stock, interval = "1min", outputsize = "full")[0]
    data.columns = ["open", 'high', 'low', 'close', 'volume']
    close_prices[stock] = data["close"]