import pandas as pd
import numpy as np


# 데이터 불러오기
raw_data = pd.read_csv('Data/연도별 월평균 전력소비량 추이(2010년~2014년, 합동자료).csv',
                       encoding = 'euc-kr')
raw_data

data = raw_data.copy()
data.dtypes
data = data.drop(9)
data = data.astype(int)

del data['평균']
del data['최대-최소 차이']
del data['관측수']

data.set_index('가구 구성원수', inplace = True)
data = data.unstack()
data.head()
data = pd.DataFrame(data)
data.columns
data.rename(columns = {0 : '전력량'},
            inplace = True)

data.head()

data.sort_values(by = '전력량', ascending = True)
data['전력량 증가 비율'] = data['전력량'] / 193
data['전력량'].mean()
data['전력량'].std()
data['전력량'].var()
data['1월']


data.to_csv('Data/연도별 월평균 전력소비량 추이(2010년~2014년, 합동자료)2.csv',
            encoding = 'euc-kr')