import pandas_datareader.data as web
import datetime as date
import pandas as pd

startDate = "02-01-2014"
endDate = "02-01-2016"

#Step 1(10 points): Remotely Download "Treasury Constant Maturity Rate" from FRED
#(https://fred.stlouisfed.org/categories/115) from 02/01/2014 to 02/01/2016:
#6-Month
month6 = web.DataReader('DGS6MO', 'fred', startDate, endDate)
#1-Year
year1 = web.DataReader('DGS1', 'fred', startDate, endDate)
#5-Year
year5 = web.DataReader('DGS5', 'fred', startDate, endDate)
#10-Year
year10 = web.DataReader('DGS10', 'fred', startDate, endDate)

#Step 2( 5 points ): Determine the average and standard deviation for each of the maturities( maturity is 6-month, 1 year, etc.)
#Step 3( 5 points ): Select only those rows that have value more or less than avg +/- 1 std
#Step 4( 10 points ): Create a dataframe which has only those rows for which all of the maturities
#has value outside of avg +/- 1 std. Hint: think about joins for frames in step 3
#Step 5( 5 points): Save the generated dataframe as sigma.xlsx
#Please upload this filled file and sigma.xlsx



for i, timeframe in enumerate([month6, year1, year5, year10]):
    avg = timeframe.mean()[0]
    stDev = timeframe.std()[0]
    timeframe = pd.concat([timeframe[(timeframe[timeframe.columns[0]] > (avg+stDev))],
                           timeframe[(timeframe[timeframe.columns[0]] < (avg-stDev))]])

    if i == 0:
        df = timeframe
    else:
        df = df.join(timeframe, how = 'inner')

df.to_excel('sigma.xlsx')

