import pandas as pd
import numpy as np



# 데이터 불러오기

raw_data = pd.read_csv('Data/20191031095811.csv',
                       encoding = 'euc-kr')
raw_data.head()
raw_data.tail()

data = raw_data.copy()
data.head()
data.columns
data.rename(columns = {'일시': '일시',
                       '평균기온(°C)': '',
                       '최저기온(°C)': '',
                       '최고기온(°C)': '',
                       '일강수량(mm)': '',
                       '최대 풍속(m/s)': '',
                       '평균 풍속(m/s)': '',
                       '최다풍향(16방위)': '',
                       '평균 이슬점온도(°C)': '',
                       '평균 상대습도(%)': '',
                       '평균 현지기압(hPa)': '',
                       '평균 해면기압(hPa)': '',
                       '합계 일조시간(hr)': '',
                       '합계 일사량(MJ/m2)': '',
                       '일 최심적설(cm)': '',
                       '평균 전운량(1/10)': '',
                       '평균 중하층운량(1/10)': '',
                       '평균 지면온도(°C)': ''},
            inplace = True)
data.head()
data.dtypes

year = []
month = []
day = []

for i in range(len(data['일시'])):
    year.append(data['일시'].loc[i][:4])
    month.append(data['일시'].loc[i][5:7])
    day.append(data['일시'].loc[i][8:])

year
month
day

data['year'] = year
data['month'] = month
data['day'] = day
data.head()

del data['일시']
data.head()
data.columns
data = pd.DataFrame(data, columns = ['year', 'month', 'day',
                                     '평균기온(°C)', '최저기온(°C)', '최고기온(°C)', '일강수량(mm)', '최대 풍속(m/s)',
                                     '평균 풍속(m/s)', '최다풍향(16방위)', '평균 이슬점온도(°C)', '평균 상대습도(%)',
                                     '평균 현지기압(hPa)', '평균 해면기압(hPa)', '합계 일조시간(hr)', '합계 일사량(MJ/m2)',
                                     '일 최심적설(cm)', '평균 전운량(1/10)', '평균 중하층운량(1/10)', '평균 지면온도(°C)'])
data.head()
data.columns
data.dtypes
data['year'].unique()
data['month'].unique()
data['day'].unique()

data['평균기온(°C)'].unique()          # 평균으로


data['최저기온(°C)'].unique()   # 평균으로```


data['최고기온(°C)'].unique()  # 평균으로


data['일강수량(mm)'].unique()      # 0값으로
data['일강수량(mm)'] = data['일강수량(mm)'].fillna(0)


data['최대 풍속(m/s)'].unique()    # 평균으로


data['평균 풍속(m/s)'].unique()     # 평균으로


data['최다풍향(16방위)'].unique()      # 평균으로
data['최다풍향(16방위)'].fillna(data['최다풍향(16방위)'].mean(), inplace = True)


data['평균 이슬점온도(°C)'].unique()


data['평균 상대습도(%)'].unique()      # 평균으로
data['평균 상대습도(%)'].fillna(data['평균 상대습도(%)'].mean(), inplace = True)


data['평균 현지기압(hPa)'].unique()


data['평균 해면기압(hPa)'].unique()


data['합계 일조시간(hr)'].unique()


data['합계 일사량(MJ/m2)'].unique()


data['일 최심적설(cm)'].unique()      # 0으로
data['일 최심적설(cm)'].fillna(0, inplace = True)


data['평균 전운량(1/10)'].unique()


data['평균 중하층운량(1/10)'].unique()      # 평균으로
data['평균 중하층운량(1/10)'].fillna(data['평균 중하층운량(1/10)'].mean(), inplace = True)


data['평균 지면온도(°C)'].unique()


data.to_csv('Data/2014-2018 시간별 기상데이터1.csv',
            index = False,
            encoding = 'euc-kr')
