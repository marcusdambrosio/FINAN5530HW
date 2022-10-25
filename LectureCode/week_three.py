# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use('ggplot')

# oil = pd.read_csv('oilPrices.csv', index_col = 'Date', parse_dates=True)
# usd = pd.read_csv('usdPrices.csv', index_col = 'Date', parse_dates=True)
# print(oil.head())

# oil.plot()
# OR
# plt.plot(oil.index, oil.Price, 'b-.', label = 'Oil Price')
# plt.plot(usd.index, usd.Price, 'g', label = 'Oil Price')
# plt.legend()
# plt.show()

# join = oil.join(usd, rsuffix = '_usdRub', how = 'inner')
# join.plot()
# plt.show()


'''scatterplot'''
# x = [1,2,3,4,5]
# y = [1,5,9,16,25]
# plt.scatter(x,y)
# plt.show()

# data = pd.read_csv('sf_pe_salaries_2011.csv', index_col = 'Id')
# data['BasePay'] = data['BasePay'].replace('Not Provided', '0')
# data['BasePay'] = data['BasePay'].astype(float)
# data.dropna(axis = 0, inplace = True)
# # print(data.head())
# y = data['BasePay'].values
# ySorted = sorted(y)
# x = data.index/data.index.max()*100
# plt.scatter(x,ySorted)
# plt.show()

'''histogram'''
# spx = pd.read_csv('^spx_daily.csv', index_col='Date', parse_dates=True)
# spx = spx[['Close']].dropna(axis = 0)
# spx['pctChange'] = spx['Close'].pct_change()
# spx.drop('Close', axis = 1, inplace = True)
# val = spx.values[1:]
# plt.hist(val, 50)
# plt.axvline(np.mean(val), color = 'blue')
# plt.axvline(-3*np.std(val), color = 'blue')
# plt.axvline(3*np.std(val), color = 'blue')
# plt.axvline(-4*np.std(val), color = 'blue')
# plt.axvline(4*np.std(val), color = 'blue')
# plt.show()