import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from mysteryFunctions import *
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# from sklearn.model_selection import train_test_split
import pandas as pd

# def plotTheLine(inputParams, m, b):
#     result = []
#     for x in inputParams:
#         y = m*x + b
#         result.append(y)
#
#     return result
#
# Xs = list(range(-20, 20))

# Ys = mysteryFunctionOne(Xs)
# Ys = mysteryFunctionTwo(Xs)
# Ycalc = plotTheLine(Xs, 2, 3)
# Yreal = mysteryFunctionTwo(Xs)
# Yreal = mysteryFunctionSmall(Xs)
# Yreal = mysteryFunctionLarge(Xs)

# Xactual = np.array(Xs)
# Yactual = np.array(Yreal)
# denominator = Xactual.dot(Xactual) - Xactual.mean()*Xactual.sum()
# m = ( Xactual.dot(Yactual)-Yactual.mean()*Xactual.sum())/denominator
# b = ( Yactual.mean()*Xactual.dot(Xactual)-Xactual.dot(Yactual)*Xactual.mean())/denominator
# Ypred = plotTheLine(Xs, m, b)
#
# predDiff = Yactual - Ypred
# avgDiff = Yactual - np.mean(Ypred)
# R2 = 1 - (predDiff.dot(predDiff)/avgDiff.dot(avgDiff))
# print(f'm: {round(m,2)}, b: {round(b,2)}, R2: {round(R2,2)}')

# plt.plot(Xs,Ycalc, '--')
# plt.plot(Xs, Ypred, '--')
# plt.scatter(Xs, Yreal)
# plt.show()

# LR = LinearRegression()
# Xtrain = Xactual.reshape(-1, 1)
# Ytrain = Yactual.reshape(-1, 1)
#
#
# LR.fit(Xtrain,Ytrain)
# YpredBad = LR.predict(Xtrain) #Predicting on training data....? I'm assuming that this is for the sake of simplicity
# r2False = r2_score(Ytrain, YpredBad)
# print(f'The R2 for a linear regression model tested on training data is {round(r2False, 3)}')
#
#
# Xtrain, Xtest, Ytrain, Ytest = Xtrain[:-10], Xtrain[-10:], Ytrain[:-10], Ytrain[-10:]
# LR.fit(Xtrain, Ytrain)
# YpredGood = LR.predict(Xtest)
# r2True = r2_score(Ytest, YpredGood)
# print(f'The R2 for a linear regression model trained/tested on split data is {round(r2True, 3)}')
# print(f'Testing the model on training data results in an R2 inflation of {round(r2False - r2True, 3)}')

# def generateYs(inputParams, m, b):
#     result = []
#     for x in inputParams:
#         y = m*x + b
#         result.append(y)
#     return result

# oil = pd.read_csv('oilPrices.csv', index_col='Date', parse_dates=True)
# rub = pd.read_csv('usdPrices.csv', index_col='Date' , parse_dates=True)
#
# trainStartDate = pd.datetime(2014, 9, 1)
# trainEndDate = pd.datetime(2016, 7, 1)
#
# testStartDate = pd.datetime(2016, 7, 1)
# testEndDate = pd.datetime(2018, 8, 1)
#
# master = oil.join(rub, rsuffix = 'UsdRub', how ='inner')
# masterTrain = master[(master.index >= trainStartDate) & (master.index<trainEndDate)]
# masterTest = master[(master.index >= testStartDate) & (master.index<testEndDate)]
#
# XsTrain = masterTrain['Price'].values
# YsTrain = masterTrain['PriceUsdRub'].values
# XsTest = masterTest['Price'].values
# YsTest = masterTest['PriceUsdRub'].values
#
# Xtrain = XsTrain.reshape(-1, 1)
# Ytrain = YsTrain.reshape(-1, 1)
#
# Xtest = XsTest.reshape(-1, 1)
# Ytest = YsTest.reshape(-1, 1)

# LR = LinearRegression()
# LR.fit(Xtrain, Ytrain)
# Ypred = LR.predict(Xtest)
# r2 = r2_score(Ytest, Ypred)
# print(f'The R2 for a linear regression model is {round(r2, 3)}')

# Ycalculated = generateYs(Xs, LR.coef_[0][0], LR.intercept_[0])

#
# plt.scatter(XsTest,YsTest)
# plt.plot(Xtest,Ypred, 'b--')
# plt.show()
# plt.scatter(Xs, Ys)
# plt.plot(Xs, Ycalculated, 'b--')
# plt.show()