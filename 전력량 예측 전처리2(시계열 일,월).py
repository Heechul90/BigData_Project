import numpy as np
import pandas as pd


# 데이터 불러오기
raw_data = pd.read_csv('merged_MeterHour.log',
                       sep = ',')
raw_data.head()

data = raw_data.copy()


# 년, 년월, 년월일 컬럼 만들기
data.head()
data.dtypes
data['date'] = data['date'].astype(str)

Year = []
YearMonth = []
YearMonthDay = []

for i in range(len(data['date'])):
    Year.append(data['date'][i][:4])
    YearMonth.append(data['date'][i][:6])
    YearMonthDay.append(data['date'][i][:8])


data['year'] = Year
data['yearmonth'] = YearMonth
data['yearmonthday'] = YearMonthDay
del data['date']
data.head()

data = pd.DataFrame(data, columns = ['year', 'yearmonth', 'yearmonthday',
                                     'user_id', 'mac', 'elec'])

data.to_csv('Data/Watt(년,년월,년월일).csv',
            encoding = 'euc-kr')


# 년, 년월, 년월일 컬럼 만들기
data = raw_data.copy()
data.head()
data.dtypes
data['date'] = data['date'].astype(str)

Year = []
Month = []
Day = []

for i in range(len(data['date'])):
    Year.append(data['date'][i][:4])
    Month.append(data['date'][i][4:6])
    Day.append(data['date'][i][6:8])


data['year'] = Year
data['month'] = Month
data['day'] = Day
del data['date']
data.head()

data = pd.DataFrame(data, columns = ['year', 'month', 'day',
                                     'user_id', 'mac', 'elec'])


data.to_csv('Data/Watt(년,월,일).csv',
            encoding = 'euc-kr')

# 도메인하고 조인.
data = pd.read_csv('Data/Watt(년,년월,년월일).csv',
                   index_col = 0,
                   encoding = 'euc-kr')
data.head()

domain = pd.read_csv('Data/domain.csv')
domain.head()

data1 = pd.merge(data, domain, on = 'mac', how = 'right')
data1.head()

data1.to_csv('Data/Watt(도메인조인).csv',
             encoding = 'euc-kr')


# 유저별 일일 전력 소비량
data2 = data1.pivot_table('elec',
                          index = 'yearmonthday',
                          columns = 'user_id',
                          aggfunc = 'sum')

data2.to_csv('Data/Watt(user별 일일 전력소비량).csv',
             encoding = 'euc-kr')


# 시계열 일자로
dataDay = data1.pivot_table('elec',
                            index = 'yearmonthday',
                            aggfunc = 'sum')

dataDay.head()
dataDay.to_csv('Data/Watt(시계열 일별 전체 전력량).csv',
               encoding = 'euc-kr')


# 시계열 월로
dateMonth = data1.pivot_table('elec',
                              index = 'yearmonth',
                              aggfunc = 'sum')

dateMonth.head()
dateMonth.to_csv('Data/Watt(시계열 월별 전체 전력량).csv',
                 encoding = 'euc-kr')


# 시계열 월로(평균)
dateMonth_mean = data1.pivot_table('elec',
                                   index = 'yearmonth',
                                   aggfunc = 'mean')

dateMonth_mean.head()
dateMonth_mean.to_csv('Data/Watt(시계열 월별 평균 전력량).csv',
                      encoding = 'euc-kr')


