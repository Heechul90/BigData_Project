import numpy as np
import pandas as pd


# 데이터 불러오기
watt_data = pd.read_csv('Data/Watt(일).csv',
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
dataset['watt'] = watt_data['elec']
dataset['date'] = watt_data['day']
del dataset['year']
del dataset['month']
del dataset['day']
dataset.head()
dataset = dataset.set_index('date')

dataset.to_csv('Data/dataset(watt).csv',
               encoding = 'euc-kr')