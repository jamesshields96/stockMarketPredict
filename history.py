import yfinance as yf, pandas as pd, shutil, os, time, glob, smtplib, ssl
from get_all_tickers import get_tickers as gt 

tickers = ["FB", "AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]

print("The amount of stocks chosen to observe: " + str(len(tickers)))

# The first two lines are responsible for removing the cvs files and replacing them with new files
shutil.rmtree("C:/Users/User/Desktop/Side Projects/stockMarketPredict/Stocks/")
os.mkdir("C:/Users/User/Desktop/Side Projects/stockMarketPredict/Stocks/")

Amount_of_API_Calls = 0

Stock_Failure = 0
Stocks_Not_Imported = 0

i=0
#This loop is responsible for storing the historical data for each ticker in our list
while(i < len(tickers)) and (Amount_of_API_Calls < 1000):
    try:
        stock = tickers[i]
        temp = yf.Ticker(str(stock))
        Hist_data = temp.history(period="max") #Tells yFinance what kind of data we want about this stock
        Hist_data.to_csv("C:/Users/User/Desktop/Side Projects/stockMarketPredict/Stocks/"+stock+".csv") # Saves the historical data in csv format
        time.sleep(2)
        Amount_of_API_Calls += 1
        Stock_Failure = 0
        i += 1
    except ValueError:
        print("Yahoo Finance Backend Error, Attempting to fix")
        if Stock_Failure > 5:
            i+=1
            Stocks_Not_Imported += 1
        Amount_of_API_Calls += 1
        Stock_Failure +=1

        
print("The amount of stocks we successfully imported: " + str(i - Stocks_Not_Imported))