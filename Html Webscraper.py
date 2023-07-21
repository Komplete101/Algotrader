# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 14:55:22 2023

@author: Chiboy
"""

import requests
from bs4 import BeautifulSoup




income_statement = {}
url = 'https://finance.yahoo.com/quote/AAPL/financials?p=AAPL&guccounter=1'
headers = {'User-Agent': "Chrome/114.0.5735.199 "}
page = requests.get(url, headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")
table = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
for t in table:
    rows = t.find_all("div", {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
    for row in rows:
        income_statement[row.get_text(separator= " | ").split("|")[0]] = row.get_text(separator= " | ").split(" | ")[1]
        