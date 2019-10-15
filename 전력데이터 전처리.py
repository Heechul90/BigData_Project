import pandas as pd
import numpy as np



# 데이터 불러오기

raw_data = pd.read_csv('Data/주택용_월별_124시_전력소비계수_20191015114623.csv',
                       encoding = 'euc-kr')
raw_data.head()
raw_data.tail()

data = raw_data.copy()
data.head()

data.set_index('시간대별', inplace = True)
data.index.names = ['시간대']

data.columns = [data.columns.map(lambda x:x[:4]), data.iloc[0]]
data = data.iloc[1:]
data.columns.names = ['년도', '월']

data = data.astype('int')
data = data.unstack('시간대')
data.head()



data.to_csv('Data/2014-2018 월별 시간대 평균 전력량.csv',
            header = True,
            encoding = 'euc-kr')

raw_data = pd.read_csv('Data/2014-2018 월별 시간대 평균 전력량.csv',
                       encoding = 'euc-kr')

raw_data
data = raw_data.copy()
data.head()
data.columns = ['년도', '월', '시간대', '전력량']
data.head()

data['년도'].unique()
data['월'].unique()
data['시간대'].unique()
data.head()

data[data['시간대'].isin(['시간대별'])]

for i in range(len(data['시간대'])):
    if data['시간대'].loc[i] == '시간대별':
        data = data.drop(i, 0)

data['시간대'].unique()

data.to_csv('Data/2014-2018 월별 시간대 평균 전력량1.csv',
            header = True,
            encoding = 'euc-kr')

raw_data = pd.read_csv('Data/2014-2018 월별 시간대 평균 전력량1.csv',
                       encoding = 'euc-kr')
del raw_data['Unnamed: 0']
raw_data

data = raw_data.copy()
data.head()

data.set_index(['년도', '월', '시간대'])
