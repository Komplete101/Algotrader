
import datetime as dt
import pandas as pd
import yfinance as yf
data = yf.download("MSFT", period = "1mo", interval="5m")
#Can be data = yf.download("Stock abreviations", start = "yyyy-mm-dd", end = "yyyy-mm-dd")


stocks = ["AMZN","TSLA",'MSFT',"GOOG"]
start = dt.datetime.today()-datetime.timedelta(30)
end = dt.datetime.today()
cl_price = pd.DataFrame()

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj close'"]