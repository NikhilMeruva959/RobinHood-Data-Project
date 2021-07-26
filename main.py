from numpy.core.fromnumeric import size
from pandas.core.series import Series
import robin_stocks.robinhood as r
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Login -> SMS Verification
r.login("*****************","*****************")

#Crypto Holdings
my_stocks = r.build_holdings()
my_crypto = r.get_all_crypto_orders()
print()
print('crypto holding')
print()
print(my_crypto)
print("\n")
print('stock holding')
print("\n")
print(my_stocks)
print("\n")

#printing readable table for my_stocks
df = pd.DataFrame(my_stocks)
df = df.T
df['ticker'] = df.index
df = df.reset_index(drop=True)
cols = df.columns.drop(['id','type','name','pe_ratio','ticker'])
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
print()
print(df)
print()

#getting Tesla historical data
tsla_data = r.stocks.get_stock_historicals("TSLA", interval = "day", span='week',bounds='regular')
tsla = pd.DataFrame(tsla_data)
print(tsla)
print()

#printing readable table for my_cryptos
etc_data = r.crypto.get_crypto_historicals("ETC", interval= "hour", span= "week", bounds='24_7')
etc = pd.DataFrame(etc_data)
print(etc)
print()

#putting diff price in each array
xBeginAt = []
yOpenPoints = []
yClosePoints = []
yHighPoints = []
yLowPoints = []

column_list = ["begins_at", "open_price", "close_price", "high_price", "low_price"]
for i in column_list:
    if(i=="begins_at"):
        xBeginAt.append(tsla[i])
    else:
        #switching to floats so pyplot can read the numbers
        tsla[i] = tsla[i].astype(float)
        if(i == "open_price"):
            yOpenPoints.append(tsla[i])
        if(i == "close_price"):
            yClosePoints.append(tsla[i])
        if(i == "high_price"):
            yHighPoints.append(tsla[i])
        if(i == "low_price"):
            yLowPoints.append(tsla[i])

#Converting panda.core.series.series into string
#for i in range(len(xBeginAt)):
#    xBeginAt[i].to_string()
#    xBeginAt[i] = xBeginAt[i][0:9]

xDateAxis = [15, 16, 19, 20, 21]

#printing Values in terminal
print(yOpenPoints)
print()
print(yClosePoints)
print()
print(type(yHighPoints[0][1]))
print()
print(yLowPoints)
print()
print(xBeginAt)
print(type(xBeginAt[0]))

plt.title("TSLA Stock Price", size=25)
plt.xticks(xDateAxis, ('2021-07-15', '2021-07-16', '2021-07-19','2021-07-20', '2021-07-21'), rotation=45)
plt.xlabel("2021 July", size=15)
plt.ylabel('USD$', size=15)
plt.grid(True)

plt.plot(xDateAxis, yOpenPoints[0], marker= 'o', markersize=10, label='Open Price')
plt.plot(xDateAxis, yClosePoints[0], marker= 'o', markersize=10, label='Close Price')
plt.plot(xDateAxis, yHighPoints[0], marker= 'o', markersize=10, label ='High Price')
plt.plot(xDateAxis, yLowPoints[0], marker= 'o', markersize=10, label = 'Low Price')

# here we add the vertical line
plt.axvline(xDateAxis[1], color='yellow',linestyle='--',linewidth=1)

# here we add the horizontal line
plt.axhline(yLowPoints[0][1], color='purple',linestyle='--',linewidth=1)

#legend
plt.legend(loc='lower right',prop={'size':15})

plt.show()

#Old way to Plot
#tsla['close_price'].plot(legend=True,figsize=(15,5))
#tsla['high_price'].plot(legend=True,figsize=(15,5))
#tsla['low_price'].plot(legend=True,figsize=(15,5))
#tsla['open_price'].plot(legend=True,figsize=(15,5))


