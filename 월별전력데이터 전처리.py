import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 데이터 불러오기
raw_data = pd.read_csv('Data/용도별_전력사용량_20191018094502.csv',
                       encoding = 'euc-kr')
raw_data

data = raw_data.copy()

data.head()
data = data.drop([0, 1, 2])
data.head()
data.rename(columns = {'월별(1)': '월'},
            inplace = True)
data.head()
data['월'][3][:1]

for i in range(3, 15):
    if i < 12:
        data['월'][i] = data['월'][i][:1]
    else:
        data['월'][i] = data['월'][i][:2]
data

data.set_index('월', inplace = True)
data.head()
data.dtypes
data = data.astype(int)

data['mean'] = (data[['2011', '2012', '2013', '2014', '2015', '2016', '2017']].mean(axis = 1)).round(2)
data['std'] = (data[['2011', '2012', '2013', '2014', '2015', '2016', '2017']].std(axis = 1)).round(2)
data['var'] = (data[['2011', '2012', '2013', '2014', '2015', '2016', '2017']].var(axis = 1)).round(2)
data['min'] = (data[['2011', '2012', '2013', '2014', '2015', '2016', '2017']].min(axis = 1)).round(2)
data['max'] = (data[['2011', '2012', '2013', '2014', '2015', '2016', '2017']].max(axis = 1)).round(2)

data.to_csv('Data/2011-2017 가정용 월별 전력량.csv',
            encoding = 'euc-kr')

data = pd.read_csv('Data/2011-2017 가정용 월별 전력량.csv',
                   index_col= 0,
                   encoding = 'euc-kr')
data
data.sort_values(by = 'mean', ascending = True)

data['평균대비증가율'] = data['mean'] / 1820.57

data.sort_values(by = 'std', ascending = True)
data['표준편차대비증가율'] = data['std'] / 56.65
data

data.to_csv('Data/2011-2017 가정용 월별 전력량2.csv',
            encoding = 'euc-kr')
