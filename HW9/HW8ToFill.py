import pandas_datareader as web
import pandas as pd
from datetime import datetime
from sklearn import linear_model
from sklearn.metrics import r2_score
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
from matplotlib import style
style.use('ggplot')
import sys

#Through this excercise we will answer the question does difference in rates affects the FX rates
#Download "Overnight London Interbank Offered Rate (LIBOR), based on U.S. Dollar " from Jan 1 2010 to today from FRED
LIBOR_USD = web.DataReader('USDONTD156N', 'fred', '01-01-2010', datetime.today())


#Download "Overnight London Interbank Offered Rate (LIBOR), based on Euro  " from Jan 1 2010 to today from FRED
LIBOR_EURO = web.DataReader('EURONTD156N', 'fred', '01-01-2010', datetime.today())


#Download "U.S. / Euro Foreign Exchange Rate" from Jan 1 2010 to today from FRED
exchangeRate = web.DataReader('DEXUSEU', 'fred', '01-01-2010', datetime.today())


#Drop NaN from each dataframe, done via df.dropna()
for data in [LIBOR_EURO, LIBOR_USD, exchangeRate]:
    data.dropna(axis = 0, inplace = True)


#Bring them all together for common dates
joined = LIBOR_EURO.join([LIBOR_USD, exchangeRate], how = 'inner')


#Calculated the ABSOLUTE difference between EUR and USD rates
joined['rateDiff'] = abs( joined['EURONTD156N'] - joined['USDONTD156N'] )


#Calculate the per cent change for EUR FX rate and difference between USD & EUR rates
joined['rateDiffPctChange'] , joined['FXPctChange'] = joined['rateDiff'].pct_change(), joined['DEXUSEU'].pct_change()
joined = joined.iloc[1:, :]


#Regress whether change in difference in USD & EUR rates has effect on EUR FX rate
LR = linear_model.LinearRegression()
#I was getting infinite values so I will drop these too
joined = joined.replace([-np.inf, np.inf], np.nan)
joined.dropna(axis = 0, inplace = True)
X, y = joined[['rateDiffPctChange']], joined['FXPctChange']
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size = .25)
yPred = LR.fit(XTrain, yTrain).predict(XTest)


#Check your r2 score
r2 = r2_score(yTest, yPred)
print(f'The R2 score for Linear Regression is {round(r2, 5)}')


#Answer the question -- does change in rates affect the change in FX rates?
Xydata = X.join(y)
print(Xydata.corr())
print(f'The change in rates and change in FX rates only has a correlation of {round(Xydata.corr().iloc[0,1], 4)}')
print('Because the linear regression R2 and correlation between the two data '
      'are both so low, it is unlikely that the change in rates affects the change in FX rates.')
'''Because the linear regression R2 and correlation between the two data are both so low, it is unlikely 
that the change in rates affects the change in FX rates.'''

plt.scatter(XTest, yTest,color = 'g', label = 'Actual Data')
plt.scatter(XTest, yPred, color = 'r', label = 'Predicted')
plt.xlabel('Rate Change')
plt.ylabel('FX Change')
plt.legend()

plt.show()