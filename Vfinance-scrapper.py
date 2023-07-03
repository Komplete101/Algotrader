
import datetime as dt
import pandas as pd
import yfinance as yf
#data = yf.download("MSFT", period = "1mo", interval="5m")
#Can be data = yf.download("Stock abreviations", start = "yyyy-mm-dd", end = "yyyy-mm-dd")


stocks = ["AMZN","TSLA",'MSFT',"GOOG","GM","INTC","PG"]
start = dt.datetime.today()-dt.timedelta(360)
end = dt.datetime.today()
cl_price = pd.DataFrame()

alldata = {}
#Loops over the specific stocks
for stock in stocks:
    cl_price[stock] = yf.download(stock,start,end)["Adj Close"]
#This loops through every stock in stocks and add the data in adjusted close

for stock in stocks:
    alldata[stock] = yf.download(stock,start,end)