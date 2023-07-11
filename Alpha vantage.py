# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 21:42:39 2023

@author: Chiboy
"""
import time
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

key_path = open("C:\\Users\\15623\\Documents\\AlphaAPI_key.txt","r").read()

#ts  = TimeSeries(key_path, output_format="pandas")
#data = ts.get_intraday(symbol="USD",outputsize="full")[0]
#data.columns = ["open","high","low",'close',"volume"]



close_prices = pd.DataFrame()
all_stocks = ["AAPL", "MSFT","CSCO","AMZN", "INIC"]
call_counter = 0
for stock in all_stocks:    
    start_time = time.time()
    ts = TimeSeries(key_path, output_format="pandas")
    data = ts.get_intraday(symbol = stock, interval = "1min", outputsize = "compact")[0]
    call_counter+=1
    data.columns = ["open", 'high', 'low', 'close', 'volume'] 
    data = data.iloc[::-1]
    close_prices[stock] = data["close"]
    if call_counter==5:
        call_counter=0
        time.sleep(60-((time.time()-start_time)%60.0))