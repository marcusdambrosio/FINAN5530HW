# Enters the Test.
# - Oh ye brethren, behold, for I have arrived
# Crowd is awed in silence. Test draws his sword( not a real one, one of those envelope things)
# - Alas, the last of my kin is facing you. The fight will be swift and merciless.
# * Dramatic Pause*
# Test becomes stentorian:
# - Do as I say and the higher gods of Finance 6520 may spare you.
# Test disappears in the cloud of white smoke leaving the below instruction.
# In this exercise you will be required to calculated the inflation-adjusted values for SP500
# 1. Download "Consumer Price Index for All Urban Consumers: All Items" from Fred from 7/15/1989 to 7/15/2018'
# 2. Normailze the original value to inflation-adjusted value, i.e. dollar today = 1$, dollar 10 years would buy 1.25 times as much
# 3. Load the "^spx_d_reind.csv"
# 4. Calculate the inflation-adjusted values of SPX for a given date(that will be monthly)
# 5. Calculate the daily pct change of inflation adjusted SPX for each month
# 6. Plot both adjusted and unadjusted results, name them accordingly
# 7. Plot the pct change values on the histogram with 25 bins
# 8. Upload this file along with two generated images

'''imports'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import pandas_datareader.data as web

'''constants'''
startDate = '1989-07-15'
endDate = '2018-07-15'

'''pull data'''
# CPI = web.DataReader('CPIAUCSL', 'fred', startDate, endDate)
# CPI.to_csv('CPI.csv')

'''normalize'''
CPI = pd.read_csv('CPI.csv', index_col='DATE', parse_dates=True)
CPI['IA'] = CPI.iloc[-1,-1] / CPI['CPIAUCSL']

'''read spx file and keep only relevant dates'''
SPX = pd.read_csv('^spx_d_reind.csv', index_col='Date', parse_dates=True)
SPX = SPX.loc[CPI.index]

'''calculate new columns'''
SPX['SPX IA'] = SPX['Close'] * CPI['IA']
SPX['IA Pct Change'] = SPX['SPX IA'].pct_change()

'''join for consolidation'''
joined = SPX.join(CPI, how = 'inner')
joined = joined[['CPIAUCSL', 'IA', 'Close', 'SPX IA', 'IA Pct Change']]

'''plot'''
joined[['Close', 'SPX IA']].plot()
plt.savefig('5530_test2_plot')
plt.show()

plt.hist(joined['IA Pct Change'], bins = 25)
plt.title('SPX Inflation Adjusted')
plt.xlabel('Pct Change')
plt.ylabel('Number of Occurrences')
plt.savefig('5530_test2_histogram')
plt.show()
