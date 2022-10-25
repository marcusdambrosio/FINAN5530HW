import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import pandas_datareader as web

ticker = 'MSFT'
startDate = '2018-11-18'
endDate = '2019-11-18'

data = web.DataReader(ticker, 'yahoo', startDate, endDate)
dataClose = data[['Close']]
#dataClose.plot()
# plt.show()
dataClose['pct'] = dataClose['Close'].pct_change()
# print(dataClose)
#dataClose['pct'].plot()
# plt.show()

histMean = dataClose['pct'].mean()
histStd = dataClose['pct'].std()
print(histMean, histStd)

todayPrice = dataClose['Close'][-1]
print(todayPrice)

timePoints = 41
scenarios = 10000
simulatedCurves = []

for scenario in range(0, scenarios):
    simulatedPrices = [todayPrice]
    monteCarloMoves = np.random.normal(histMean, histStd, timePoints)
    for move in monteCarloMoves:
        previousDayPrice = simulatedPrices[-1]
        simulatedPrices.append(previousDayPrice*(1+move))
    simulatedCurves.append(simulatedPrices)
    days = list(range(0, timePoints+1))
    # plt.plot(days,simulatedPrices)

percentile = np.percentile(simulatedCurves, 55, axis = 0)
plt.plot(days, percentile, 'r--')
dfTest = web.DataReader(ticker, 'yahoo', endDate, '2020-01-18')
dfTestPrices = dfTest.Close.values
plt.plot(days, dfTestPrices)
plt.show()