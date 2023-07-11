# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 20:33:37 2023

@author: Chiboy
"""

import pandas as pd
from yahoofinancials import YahooFinancials
import datetime as dt

all_stocks = ["AAPL", "MSFT","CSCO","AMZN", "INIC"]

close_prices = pd.DataFrame()
beg_date  = (dt.date.today()-dt.timedelta(1825)).strftime("%Y-%m-%d")
end_date = (dt.datetime.today()).strftime("%Y-%m-%d")
for stock in all_stocks:
    yahoo_financials = YahooFinancials(stock)
    json_obj = yahoo_financials.get_historical_price_data(beg_date, end_date,"daily")
    ohlv = json_obj[stock]["prices"]
    temp = pd.DataFrame(ohlv)[["formatted_date","adjclose"]]
    temp.set_index("formatted_date",inplace = True)
    temp.dropna(inplace = True)
    close_prices[stock] =temp["adjclose"]