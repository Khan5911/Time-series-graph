# import emoji
#
# print(emoji.emojize("I love reading books:books:"))
# print(emoji.emojize("Some people have a very sensitive heart:red_heart:, please be kind with them.:hibiscus:"))

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('AAPL',
                      start=start_date,
                      end=end_date,
                      progress=False)
print(data.head())

import plotly.express as px
figure = px.line(data, x = data.index, y = "Close")
figure.show()

