import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
raw_data = pd.read_csv('Final_project/Data/HomeC.csv',
                       encoding = 'utf-8')
raw_data

data = raw_data.copy()

# 데이터 정보 보기
data.head()
data.columns
data.describe()
data.dtypes

# time 컬럼 object타입을 date타입으로 바꾸기
data.time = pd.to_datetime(data.time)
data.dtypes
data.tail()
data = data.drop(503910, 0)
data.tail()

# time_index 만들기
len(data)
time_index = pd.date_range('2016-01-01 05:00', periods = 503910, freq = 'min')
time_index = pd.DatetimeIndex(time_index)
data = data.set_index(time_index)
data.head()
del data['time']

# 중복된 날짜가 있는지 확인
data.index.is_unique

# 월별로 그래프 그리기
data_permonth = data.resample('M').sum()
data_permonth.columns
plt.figure(figsize = (20, 10))
sns.lineplot(data = data_permonth.filter(items = ['use [kW]',
                                                  'gen [kW]',
                                                  'House overall [kW]',
                                                  'Dishwasher [kW]',
                                                  'Furnace 1 [kW]',
                                                  'Furnace 2 [kW]',
                                                  'Home office [kW]',
                                                  'Fridge [kW]',
                                                  'Wine cellar [kW]',
                                                  'Garage door [kW]',
                                                  'Kitchen 12 [kW]',
                                                  'Kitchen 14 [kW]',
                                                  'Kitchen 38 [kW]',
                                                  'Barn [kW]',
                                                  'Well [kW]',
                                                  'Microwave [kW]',
                                                  'Living room [kW]',
                                                  'Solar [kW]']), dashes = False)

