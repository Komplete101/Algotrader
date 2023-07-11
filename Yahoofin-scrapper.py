# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:26:51 2023

@author: Chiboy
"""

from yahoofinancials import YahooFinancials

stock = "TSLA"
yahoo_financials = YahooFinancials(stock)
data  = yahoo_financials.get_historical_price_data("2020-04-28", "2023-07-05","daily")                                   
#provide start date end date and period 