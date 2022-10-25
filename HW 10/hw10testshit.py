import pandas as pd
import numpy as np

from WOE import data_vars
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
from sklearn.metrics import classification_report
import sklearn.metrics
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import seaborn as sns

def printOutTheCoefficients(params, rows, coeffecients,intercept):
    tParams = params[np.newaxis].T
    tCoeffs = coeffecients.T
    total = np.concatenate([tParams,(np.ones(len(tParams))*intercept)[np.newaxis].T, tCoeffs, rows],axis=1)
    totalDF = pd.DataFrame(data=total, columns = ['Parameter','Intercept', 'Coefficient', 'Row 1', 'Row 2', 'Row 3','Row 4', 'Row 5'])
    totalDF.to_excel("modelOutput.xlsx")
    print(totalDF)
    print('\nThe actual model calculations are performed in the spreadsheet submitted with this code.')

#load the data from the dataset
data = pd.read_csv('adultIncome_proc.csv')
data.dropna(axis=0, inplace = True)
#drop obviously correlated values
numericalCorrs = data.corr()
'''using factorize() we can represent the categorical data numerically and then evaluate these correlations as well'''
categoricalData = data[[c for c in data.columns if c not in numericalCorrs.columns]].apply(lambda x: x.factorize()[0])
joined = data[numericalCorrs.columns].join(categoricalData, how = 'inner')
correlations = joined.corr()
sns.heatmap(correlations)
plt.show()
print('Looking at the correlation heatmap, we see that none off the correlations (aside from the diagonal) are above 0.5 so nothing must be removed')

#reduce Marial Status to four  categories -- Married, Separated, Never Married, Widowed
# print(data['Martial-status'].unique())
marital = data['Martial-status'].tolist()
for i, status in enumerate(marital):
    marital[i] = status.strip()
    if status.strip() == 'Divorced':
        marital[i] = 'Separated'
    elif status.split('-')[0].strip() == 'Married':
        marital[i] = 'Married'
data['Martial-status'] = marital

#map countries to born in United States or not
bornUS = []
for native in data['Native Country']:
    bornUS.append('Yes') if native.strip() == 'United-States' else bornUS.append('No')
data['Born in US'] = bornUS

#determine if any fields are correlated with each other
numericalCorrs = data.corr()
categoricalData = data[[c for c in data.columns if c not in numericalCorrs.columns]].apply(lambda x: x.factorize()[0])
joined = data[numericalCorrs.columns].join(categoricalData, how = 'inner')
correlations = joined.corr()
sns.heatmap(correlations)
plt.show()
print('\nWe see that the new "Born in US" field is very correlated with "Native Country". This obviously makes sense because one was created from the other.\n'
      'The "Native Country" field will be dropped.')
data.drop('Native Country', axis = 1, inplace = True)
#find statistically significant or unreasonable variables using WOE file
finalIV , IV = data_vars(data, data['income-80k+'])
print(IV)
print('\nAs seen from the IV table: Degree, Marital Status, and Occupation are all statistically significant while Born in US, Race, and type of employment are much less important.')
print('It might be worth removing some of the less important variables before training to increase model performance.')
#dummy encode all of the non-quantitative values
categoricalVariables = ['Race','Sex', 'type-of-employment', 'occupation', 'Martial-status', 'Degree', 'Born in US']
for var in categoricalVariables:
    data[var] = data[var].astype('category').cat.codes
#drop dummyfied variables
print('\nDummyfied variables already replaced in last step')
#create table with base quantitative values and with dummy values
print('\nI am not really sure what what this means by create a table... Does this mean just recombining the dummy and original quantitative variables?\n'
      'If so, it is already done.')
#separate for resutls and input sets
X, y = data.drop('income-80k+', axis = 1), data['income-80k+']
#split between sets
XTrain, XTest, yTrain, yTest = train_test_split(X,y, test_size = .25)
#run logistic regresstion
model = LogisticRegression(max_iter = 500)
model.fit(XTrain, yTrain)
yPred = model.predict(XTest)
#print classification report
print('\n', 'CLASSIFICATION REPORT\n', classification_report(yTest, yPred))
#print resuls using printOutCoefficients method to excel and run 5 different rows through the model in excel
params = XTest.columns
rows = XTest.iloc[:5, :].values.T

printOutTheCoefficients(params, rows, model.coef_, model.intercept_)