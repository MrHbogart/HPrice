import pandas as pd
import datetime
from HPrice import HPrice

#importing data downloaded from ducascopy.com
data = pd.read_csv("EURUSD_Candlestick_15_M_BID_05.07.2021-10.07.2021.csv")

#converting date format to python timedate format
date = []
for i in data['Gmt time']:
    date.append(datetime.datetime.strptime(i, '%d.%m.%Y %H:%M:%S.%f'))

data['date'] = date

data.drop(['Gmt time'], axis=1, inplace = True)

#change names of data columns
data.columns = ['open', 'high', 'low', 'close', 'volume', 'date']

print(data.head())
#importing main and creating an instance from CashData class

cd = HPrice.HPrice(data, 4).HPrice()

hp = HPrice.HPrice(data, 10).clear_HPrice()


# print(cd)

#here we want to plot data to check if it works correctly

import plotly.graph_objects as go

#plotting OHLC data
fig = go.Figure(data=go.Ohlc(x=data['date'],
                    open=data['open'],
                    high=data['high'],
                    low=data['low'],
                    close=data['close']))

#adding neowave cash data to OHLC chart to compare
# fig.add_trace(go.Scatter(
#     mode="markers+lines", x=cd["date"], y=cd["price"]
# ))

fig.add_trace(go.Scatter(
    mode="markers+lines", x=hp["date"], y=hp["price"]
))

fig.show()
