import numpy as np
import csv

file = open('testFile.csv', 'r')


companyDict = {}

for line in file:
    if 'Amount' in line:
        continue
    company, moneyIn, moneyOut = line.split(',')
    company = company.strip(' ')
    if 'Utes' in company:
        company = 'Utes'
    moneyIn = float(moneyIn.strip(' '))
    moneyOut = float(moneyOut.strip(' '))
    companyDict[company] = companyDict[company] + (moneyIn - np.abs(moneyOut)) \
        if company in companyDict.keys() else (moneyIn - np.abs(moneyOut))

print(companyDict)
file.close()

