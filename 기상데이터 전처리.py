import pandas as pd
import numpy as np



# 데이터 불러오기

raw_data = pd.read_csv('Data/2014-2018 시간별 기상데이터.csv',
                       encoding = 'euc-kr')
raw_data.head()
raw_data.tail()

data = raw_data.copy()
data.head()
data.columns
data.rename(columns = {'일시': 'date',
                       '평균기온(°C)': 'temp',
                       '최저기온(°C)': 'lowest temp',
                       '최고기온(°C)': 'highest temp',
                       '일강수량(mm)': 'rainfall',
                       '평균 풍속(m/s)': 'wind speed',
                       '평균 이슬점온도(°C)': 'dew point',
                       '평균 상대습도(%)': 'humidity',
                       '합계 일조 시간(hr)': 'sunshine',
                       '일 최심적설(cm)': 'snowfall'},
            inplace = True)
data.head()

year = []
month = []
day = []

for i in range(len(data['date'])):
    year.append(data['date'].loc[i][:4])
    month.append(data['date'].loc[i][5:7])
    day.append(data['date'].loc[i][8:])

year
month
day

data['year'] = year
data['month'] = month
data['day'] = day
data.head()

del data['date']
data.head()
data.columns
data = pd.DataFrame(data, columns = ['year', 'month', 'day',
                                     'temp', 'lowest temp', 'highest temp',
                                     'rainfall', 'wind speed', 'dew point',
                                     'humidity', 'sunshine', 'snowfall'])
data.head()
data.columns
data['year'].unique()
data['month'].unique()
data['day'].unique()

data['temp'].unique()          # 평균으로
data['temp'].fillna(data['temp'].mean(), inplace = True)

data['lowest temp'].unique()   # 평균으로```
data['lowest temp'].fillna(data['lowest temp'].mean(), inplace = True)

data['highest temp'].unique()  # 평균으로
data['highest temp'].fillna(data['highest temp'].mean(), inplace = True)

data['rainfall'].unique()      # 0값으로
data['rainfall'] = data['rainfall'].fillna(0)

data['wind speed'].unique()    # 평균으로
data['wind speed'].fillna(data['wind speed'].mean(), inplace = True)

data['dew point'].unique()     # 평균으로
data['dew point'].fillna(data['dew point'].mean(), inplace = True)

data['humidity'].unique()      # 평균으로
data['humidity'].fillna(data['humidity'].mean(), inplace = True)

data['sunshine'].unique()      # 평균으로
data['sunshine'].fillna(data['sunshine'].mean(), inplace = True)

data['snowfall'].unique()      # 0값으로
data['snowfall'] = data['snowfall'].fillna(0)

data.to_csv('Data/2014-2018 시간별 기상데이터1.csv',
            index = False,
            encoding = 'euc-kr')
