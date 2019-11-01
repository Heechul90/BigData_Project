import numpy as np
import pandas as pd


# 데이터 불러오기
watt_data = pd.read_csv('Data/Watt(시계열 일별 전체 전력량).csv',
                        encoding = 'euc-kr')
watt_data.head()
watt_data.tail()

len(watt_data)


weather_data = pd.read_csv('Data/2014-2018 시간별 기상데이터1.csv',
                           encoding = 'euc-kr')
weather_data.head()
weather_data.tail()

len(weather_data)

dataset = weather_data
dataset['elec'] = watt_data['elec']
dataset['date'] = watt_data['yearmonthday']
del dataset['year']
del dataset['month']
del dataset['day']
dataset.head()
dataset = dataset.set_index('date')

dataset.to_csv('Data/dataset.csv',
               encoding = 'euc-kr')