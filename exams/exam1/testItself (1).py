#********DRUMROLL****************
#This is your first test exercise.
#***DRUMROLL ABRUPTLY ENDS*******
#This is what you have to do:
#1.Open the testFile.csv
#2.Process each line so you create dictionary where key is name of the company and value is a net balance
#2.a.   First column of each row is a name of the company
#2.a.a. Utes company has different types of spelling, so you need to put all of them under the same key
#2.b.   Second column is payments in
#2.c.   Third column is payments out. Note that they can be negatives as well.
#       Hint: Absolute value could be derived by using abs( number )
#2.d.   Your net balance is sum(payments in - payments out)
#3. Print resulting dictionary
#4. Upload the printed result along with this file

utesNames = ["Utes"
,"Utes LLC"
,"LLC Utes"
,"Utes Limited Liability Corp"
,"Utes Co." ]

import numpy as np

file = open('testFile.csv', 'r')
companyDict = {}
for line in file:
    if 'Amount' in line:
        continue
    company, moneyIn, moneyOut = line.split(',')
    company = company.strip(' ')
    if company in utesNames:
        company = 'Utes'
    moneyIn = float(moneyIn.strip(' '))
    moneyOut = float(moneyOut.strip(' '))
    companyDict[company] = companyDict[company] + (moneyIn - np.abs(moneyOut)) \
        if company in companyDict.keys() else (moneyIn - np.abs(moneyOut))

print(companyDict)
file.close()



