import pandas_datareader.data as web
import datetime as dt
import pandas as pd
import sys
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelpad'] = 16
#pick any date after January of 2010
#let's pretend that you had $1000 dollars to invest at that date
#how much would it be today if you have invested back then and sold in on 1st of April 2019
#remotely download the SPX index from your date to 1st of April 2019
#load the FTSE from the file, and select values from your date  to 1st of April 2019
#normalize the return of each index for "Close" column so you can calculate your total return at any given date
#"invest" $1000 dollars on your date and make sure that you show your total gain/loss at every date
#plot both "investments" in SPX and FTSE on the same graph with names of "US Returns" and "EUR Returns" respectively.


startDate = "2012-02-01"
endDate = "2019-04-01"
SPX = web.DataReader('sp500', 'fred', startDate, endDate)
SPX.to_csv('SPX.csv')

SPX = pd.read_csv('SPX.csv', index_col = 'DATE', parse_dates=True)
SPX.rename({'sp500':'Close'}, axis = 1, inplace=True)
FTSE = pd.read_csv('^ftm_d.csv', index_col = 'Date', parse_dates=True)
FTSE = FTSE.loc[startDate:endDate, :]



SPX['US Relative Return'] = SPX['Close']/SPX.loc[startDate, 'Close']
SPX['US Return'] = SPX['US Relative Return'] * 1000
SPX.drop('Close', axis = 1, inplace = True)

FTSE['EUR Relative Return'] = FTSE['Close']/FTSE.loc[startDate, 'Close']
FTSE['EUR Return'] = FTSE['EUR Relative Return'] * 1000
FTSE = FTSE[['EUR Relative Return', 'EUR Return']]

master = SPX.join(FTSE, how = 'inner')
master.dropna(axis = 0, inplace = True)

fig, ax = plt.subplots(figsize=(28,16))
ax.set_xlabel('Date')
ax.set_ylabel('Value of $1000 Investment')

ax_ = ax.twinx()
ax_.set_ylabel('Relative Return')

ax.set_ylim(master['US Return'].min()*(.9), master['US Return'].max()*1.1)
ax_.set_ylim(master['US Relative Return'].min()*(.9), master['US Relative Return'].max()*1.1)

ax.plot(master.index, master['US Return'], label = 'US')
ax.plot(master.index, master['EUR Return'], label = 'EUR')
ax.legend()

plt.savefig('Plot.png')
plt.show()