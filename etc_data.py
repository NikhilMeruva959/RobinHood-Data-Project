from numpy.core.fromnumeric import size
from pandas.core.series import Series
import robin_stocks.robinhood as r
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Login -> SMS Verification
r.login("*********","*******")

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
        etc[i] = etc[i].astype(str)
        etc[i] = etc[i][0:9]
        xBeginAt.append(etc[i])
    else:
        #switching to floats so pyplot can read the numbers
        etc[i] = etc[i].astype(float)
        if(i == "open_price"):
            yOpenPoints.append(etc[i])
        if(i == "close_price"):
            yClosePoints.append(etc[i])
        if(i == "high_price"):
            yHighPoints.append(etc[i])
        if(i == "low_price"):
            yLowPoints.append(etc[i])

#Converting panda.core.series.series into string
#for i in range(len(xBeginAt)):
#    xBeginAt[i].to_string()
#    xBeginAt[i] = xBeginAt[i][0:9]


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

plt.title("ETC Price", size=25)
plt.xlabel("2021 July", size=15)
plt.ylabel('USD$', size=15)
plt.grid(True)

plt.plot(xBeginAt, yOpenPoints[0], marker= 'o', markersize=10, label='Open Price')
plt.plot(xBeginAt, yClosePoints[0], marker= 'o', markersize=10, label='Close Price')
plt.plot(xBeginAt, yHighPoints[0], marker= 'o', markersize=10, label ='High Price')
plt.plot(xBeginAt, yLowPoints[0], marker= 'o', markersize=10, label = 'Low Price')

# here we add the vertical line
#plt.axvline(xDateAxis[1], color='yellow',linestyle='--',linewidth=1)

# here we add the horizontal line
#plt.axhline(yLowPoints[0][1], color='purple',linestyle='--',linewidth=1)

#legend
plt.legend(loc='lower right',prop={'size':15})

plt.show()

#Old way to Plot
#tsla['close_price'].plot(legend=True,figsize=(15,5))
#tsla['high_price'].plot(legend=True,figsize=(15,5))
#tsla['low_price'].plot(legend=True,figsize=(15,5))
#tsla['open_price'].plot(legend=True,figsize=(15,5))


