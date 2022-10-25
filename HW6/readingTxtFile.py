#What you need to do is to transform the file Mkt_data_test.txt
#to the format like in file in the screenshot
#
#Your steps to get there:
#1.Create a header line with following columns: Time;Bid\Ask;Price;Volume. NOTE NO SPACES
#2.Remove all of the timestamp lines, i.e ======== Data: .....
#3.Remove the 1900-01-01 from the timestamp but leave the time itself
#4.Get rid of all spaces and empty lines
#5.Replace 0 or 1 in the second position with Bid or Ask, Bid for 0, Ask for 1
#6.Save the header line and propely formatted lines to the COMMA-SEPARATED csv file named mktDataFormat.csv
#

import pandas as pd

newData = pd.DataFrame(columns = ['Time', 'Bid/Ask', 'Price', 'Volume'])  #make dataframe hold formatted data

for row in open('Mkt_data_test.txt', 'r'):  #open txt file and iterate through each row
    row = row.strip(' ')    #strip the extra spaces from outside of each row if they are there
    if len(row.split(';')) > 1:     #split the row by semicolons -- this will eliminate any of the bad lines with no data as well as separate the other data we need
        newRow = [c.strip(' ') for c in row.split(';')]     #Remove extra spaces on the outside of each individual entry if they exist
    else:
        continue
    t = newRow[0].split('1900-01-01 ')[-1]  #remove the date from timestamp
    t = t[3:-5] #remove unecessary digits -- this could have been designed to work regardless of the lenght of the timestamp input but for this particular assignment I made it easy because we knew the format
    newData = newData.append({'Time': t,
                              'Bid/Ask': 'Bid' if newRow[1] == '0' else 'Ask',
                              'Price': newRow[2],
                              'Volume': newRow[3].split('\n')[0]}, ignore_index = True)     #make a new row of dataframe with each element in the correct column

newData.to_csv('mktDataFormat.csv')     #save csv in correct format
