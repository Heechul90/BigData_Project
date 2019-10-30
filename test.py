import numpy as np
import pandas as pd


# 데이터 불러오기
raw_data = pd.read_csv('Data/merged_MeterHour.txt',
                       sep = ',')
raw_data.head()

data = raw_data.copy()

data.head()
data.dtypes
data['date_time'] = data['date_time'].astype(str)


dateDay = []
dateMonth = []


for i in range(len(data['date_time'])):
    dateDay.append(data['date_time'][i][:8])
    dateMonth.append(data['date_time'][i][:6])


data['dateDay'] = dateDay
data['dateMonth'] = dateMonth
data.head()

data.to_csv('Data/Watt.csv',
            encoding = 'euc-kr')

# 시계열 일자로
dataDay = data.pivot_table('elec',
                           index = 'dateDay',
                           aggfunc = 'sum')

dataDay.head()
dataDay.to_csv('Data/Watt(일).csv',
               encoding = 'euc-kr')


# 시계열 월로
dateMonth = data.pivot_table('elec',
                             index = 'dateMonth',
                             aggfunc = 'sum')

dateMonth.head()
dateMonth.to_csv('Data/Watt(월).csv',
                 encoding = 'euc-kr')



# 시계열 월로(mean)
dateMonth1 = data.pivot_table('elec',
                              index = 'dateMonth',
                              aggfunc = 'mean')

dateMonth1.head()
dateMonth1.to_csv('Data/Watt(월)mean.csv',
                  encoding = 'euc-kr')

