# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 14:55:22 2023

@author: Chiboy
"""

import requests
from bs4 import BeautifulSoup

stocks = ["AAPL","MSFT","NVDA","INTC", "AMD"]
income_statement = {}
balance_sheet_dict = {}
cashflow = {}

for stock in stocks:

    url = 'https://finance.yahoo.com/quote/{}/financials?p={}'.format(stock)
    income = {}
    table_title = {}
    
    headers = {'User-Agent': "Chrome/115.0.5790.171"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    table = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in table:
        heading = t.find_all("div", {"class": "D(tbr) C($primaryColor) D(itb)"})
        for top_row in heading:
            table_title[top_row.get_text(separator= "|").split("|")[0]] = top_row.get_text(separator = "|").split("|")[1:]
            