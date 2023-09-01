# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 11:44:08 2023

@author: Chiboy
"""

import requests
from bs4 import BeautifulSoup

stocks  = ["AAPL","MSFT","NVDA","INTC", "AMD", "BBY"]
key_statistics = {}

for stock in stocks:
    
    url = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'.format(stock,stock)

    headers = {'User-Agent': "Chrome/115.0.5790.171"}
    page = requests.get(url, headers = headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    table = soup.find_all("table" , {"class" : "W(100%) Bdcl(c)"})
    
    temp_stats = {}
    for t in table:
        rows = t.find_all("tr")
        for row in rows:
            temp_stats[row.get_text(separator = "|").split("|")[0]] = row.get_text(separator = "|").split('|')[-1]
    key_statistics[stock] = temp_stats