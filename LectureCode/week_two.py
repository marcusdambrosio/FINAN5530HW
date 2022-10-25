# import pandas as pd
#
# df = pd.read_csv('KODK.csv')
# # print(df)
# # print(df.index)
# # print(df.columns)
# df = pd.read_csv('KODK.csv', index_col = 'Date', parse_dates=True)
# # print(df)
# # print(df.head())
# # print(df.tail())
#
# # print(df.loc[df.index[0]])
# # print(df.iloc[0])
# # print(df.loc[df.index[0]].all() == df.iloc[0].all())
#
# # print(df[['Open', 'Close']].head())
# # df['DollarVolume'] = df['Volume']*df['Close']
#
# # df['ReturntoDate'] = (df['Close'] - df['Close'][0]) / df['Close'][0]
# df['PctChange'] = df['Close'].pct_change()
# # # df['PctChange']
# #
# # noOpenDF = df.drop('Open', axis = 1)
# # print(df.sort_values(by = 'PctChange'))
# # topFivePctDF = df[df['PctChange'] >= .05]
# # print(topFivePctDF)
#
# import datetime as dt
# import pandas_datareader as web
#
# startDate = '2018-08-10'
# endDate = dt.datetime.today()
# ticker = 'KODK'

# df = web.DataReader(ticker, 'yahoo', startDate, endDate)
# # print(df.head())
# # df.to_csv(f'{ticker}data.csv')
#
# # mgntDF = web.DataReader('MGNT', 'moex', startDate, endDate)
# # print(mgntDF.head())
# # mgntDF.to_csv('MGNTdata.csv')
# mgntDF = pd.read_csv('MGNTdata.csv', index_col='TRADEDATE', parse_dates=True)
# mgntDF = mgntDF[mgntDF['BOARDID'] == 'TQBR']
# mgntDF = mgntDF[['CLOSE']]
# # print(mgntDF)
# mgntDF['CLOSE'] /= 60
# # print(mgntDF.head())
#
# dfJoin = df.join(mgntDF, how = 'inner')
# # print(dfJoin)
#
# dfInflation = web.DataReader('CPIAUCSL', 'fred', startDate, endDate)
# print(dfInflation)