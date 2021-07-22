import quandl
import pandas as pd

quandl.ApiConfig.api_key="MY_TOKEN"
# https://www.quandl.com/databases/WIKIP/data
# price = quandl.get('WIKI/KO')
# price.to_csv('./quandl_data/stock_price.csv')

# free but the data stops at the end of 2017
# https://www.quandl.com/data/TSE-Tokyo-Stock-Exchange/documentation
# TSE/7203 for toyota
price = quandl.get('TSE/7974')
price.to_csv('./quandl_data/stock_price.csv')

# premium : just an example for free 
# https://www.quandl.com/data/XJPX-Japan-Exchange-Group-Prices/usage/export
# price = quandl.get('XJPX/13060_UADJ')
# price.to_csv('./quandl_data/stock_price.csv')
# https://www.quandl.com/databases/MF1/data
# fin = quandl.get_table('MER/F1', compnumber="39102", paginate=True)

# https://www.quandl.com/databases/JCF/data
fin = quandl.get_table('RD/JFUND', paginate=True)
fin.to_csv('./quandl_data/stock_fin.csv')