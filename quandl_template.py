import quandl
import pandas as pd

quandl.ApiConfig.api_key="MY_TOKEN"
data=quandl.get('WIKI/KO')
data.to_csv('stock_price.csv')
