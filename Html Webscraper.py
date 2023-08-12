# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 14:55:22 2023

@author: Chiboy
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

stocks = ["AAPL","MSFT","NVDA","INTC", "AMD", "BBY"]
income_statement_dict= {}
balance_sheet_dict = {}
cashflow_dict= {}

for stock in stocks:

    url = 'https://finance.yahoo.com/quote/{}/financials?p={}&guccounter=1'.format(stock,stock)
    income_statement = {}
    table_title = {}
    
    headers = {'User-Agent': "Chrome/115.0.5790.171"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    table = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in table:
        heading = t.find_all("div", {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator= "|").split("|")[0]] = top_row.get_text(separator = "|").split("|")[1:]
        rows = t.find_all("div", {"class", "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            income_statement[row.get_text(separator = "|").split("|")[0]] = row .get_text(separator = "|").split("|")[1:]  
            
    temp = pd.DataFrame(income_statement).T
    temp.columns = table_title["Breakdown"]
    income_statement_dict[stock] = temp

for stock in stocks:

    url = 'https://finance.yahoo.com/quote/{}/cash-flow?p={}&guccounter=1'.format(stock,stock)
    cashflow = {}
    table_title = {}
    
    headers = {'User-Agent': "Chrome/115.0.5790.171"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    table = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in table:
        heading = t.find_all("div", {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator= "|").split("|")[0]] = top_row.get_text(separator = "|").split("|")[1:]
        rows = t.find_all("div", {"class", "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            cashflow[row.get_text(separator = "|").split("|")[0]] = row .get_text(separator = "|").split("|")[1:]  
            
    temp = pd.DataFrame(cashflow).T
    temp.columns = table_title["Breakdown"]
    cashflow_dict[stock] = temp
    
    
    
for stock in stocks:

    url = 'https://finance.yahoo.com/quote/{}/balance-sheet?p={}&guccounter=1'.format(stock,stock)
    balance_sheet = {}
    table_title = {}
    
    headers = {'User-Agent': "Chrome/115.0.5790.171"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    table = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in table:
        heading = t.find_all("div", {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator= "|").split("|")[0]] = top_row.get_text(separator = "|").split("|")[1:]
        rows = t.find_all("div", {"class", "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            balance_sheet[row.get_text(separator = "|").split("|")[0]] = row .get_text(separator = "|").split("|")[1:]  
            
    temp = pd.DataFrame(balance_sheet).T
    temp.columns = table_title["Breakdown"]
    balance_sheet_dict[stock] = temp
    
for stock in stocks:
    for col in income_statement_dict[stock].columns:
        income_statement_dict[stock][col] = income_statement_dict[stock][col].str.replace(',|-','')
        income_statement_dict[stock][col] = pd.to_numeric(income_statement_dict[stock][col], errors = "coerce")
        