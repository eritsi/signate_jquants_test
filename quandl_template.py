import quandl
import pandas as pd

quandl.ApiConfig.api_key="MY_TOKEN"
# free
# TSE/7203 for toyota
# price = quandl.get('WIKI/KO')
# price.to_csv('stock_price.csv')

# premium : just an example for free 
# https://www.quandl.com/data/XJPX-Japan-Exchange-Group-Prices/usage/export
price = quandl.get('XJPX/13060_UADJ')
price.to_csv('./quandl_data/stock_price.csv')
# https://www.quandl.com/databases/JCF/data
fin = quandl.get_table('RD/JFUND', paginate=True)
# fin = quandl.get_table('MER/F1', compnumber="39102", paginate=True)
fin.to_csv('./quandl_data/stock_fin.csv')