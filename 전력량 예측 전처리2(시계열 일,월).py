import numpy as np
import pandas as pd


# 데이터 불러오기
raw_data = pd.read_csv('Data/merged_MeterHour.log',
                       sep = ',')
raw_data.head()

data = raw_data.copy()

data.head()
data.dtypes
data['date'] = data['date'].astype(str)



Year = []
Month = []
Day = []


for i in range(len(data['date'])):
    Year.append(data['date'][i][:4])
    Month.append(data['date'][i][:6])
    Day.append(data['date'][i][:8])


data['year'] = Year
data['month'] = Month
data['day'] = Day
del data['date']
data.head()

data.to_csv('Data/Watt.csv',
            encoding = 'euc-kr')

domain = pd.read_csv('Data/domain.csv')
domain.head()

data1 = pd.merge(data, domain, on = 'mac', how = 'right')
data1.head()

data1.to_csv('Data/Watt1.csv',
             encoding = 'euc-kr')

# 시계열 일자로
data111 = data1.pivot_table('elec',
                           index = 'day',
                           columns = 'user_id',
                           aggfunc = 'sum')

data111.to_csv('Data/Watt2.csv',
               encoding = 'euc-kr')


# 시계열 일자로
dataDay = data.pivot_table('elec',
                           index = 'day',
                           aggfunc = 'sum')

dataDay.head()
dataDay.to_csv('Data/Watt(일).csv',
               encoding = 'euc-kr')


# 시계열 월로
dateMonth = data.pivot_table('elec',
                             index = 'month',
                             aggfunc = 'sum')

dateMonth.head()
dateMonth.to_csv('Data/Watt(월).csv',
                 encoding = 'euc-kr')



# 시계열 월로(평균)
dateMonth_mean = data.pivot_table('elec',
                                  index = 'month',
                                  aggfunc = 'mean')

dateMonth_mean.head()
dateMonth_mean.to_csv('Data/Watt(월-평균).csv',
                      encoding = 'euc-kr')


