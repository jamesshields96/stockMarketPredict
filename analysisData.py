import yfinance as yf, pandas as pd, shutil, os, time, glob, smtplib, ssl
from get_all_tickers import get_tickers as gt 

list_files = (glob.glob("C:/Users/User/Desktop/Side Projects/stockMarketPredict/Stocks/*.csv"))
new_data = [] # This array is used to hold all the stock names and their respective OBV score
interval = 0

while interval < len(list_files):
    Data = pd.read_csv(list_files[interval]).tail(10) # Gets the last 10 days of data, change the tail number to increase or decrease amount of days
    pos_move = [] # List of days where the stock price increased
    neg_move = [] # List of days where the stock price decreased
    OBV_Value = 0 # Sets the initial OBV to zero
    count = 0
    while(count < 10): # This number needs to be changed to match the number in the tail from above
        if Data.iloc[count,1] < Data.iloc[count,4]:
            pos_move.append(count)
        elif Data.iloc[count,1] > Data.iloc[count,4]:
            neg_move.append(count)
        count += 1
    count2 = 0
    for i in pos_move:
        OBV_Value = round(OBV_Value - (Data.iloc[i,5]/Data.iloc[i,1]))
    for i in neg_move:  # Subtracts the volumes of negative days from OBV_Value, divide by opening price to normalize across all stocks
        OBV_Value = round(OBV_Value - (Data.iloc[i,5]/Data.iloc[i,1]))
    Stock_Name = ((os.path.basename(list_files[interval])).split(".csv")[0])  # Get the name of the current stock we are analyzing
    new_data.append([Stock_Name, OBV_Value])  # Add the stock name and OBV value to the new_data list
    interval += 1

df = pd.DataFrame(new_data, columns = ['Stock', 'OBV_Value'])  # Creates a new dataframe from the new_data list
df["Stocks_Ranked"] = df["OBV_Value"].rank(ascending = False)  # Rank the stocks by their OBV_Values
df.sort_values("OBV_Value", inplace = True, ascending = False)  # Sort the ranked stocks
df.to_csv("C:/Users/User/Desktop/Side Projects/stockMarketPredict/Stocks/OBV_Ranked.csv", index = False)  # Save the dataframe to a csv without the index column