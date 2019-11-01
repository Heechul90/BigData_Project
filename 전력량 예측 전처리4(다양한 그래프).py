import numpy as np
import pandas as pd



# 데이터 불러오기
data = pd.read_csv('Data/Watt(년,월,일).csv',
                   index_col =0,
                   encoding = 'euc-kr')
data.head()

# 도메인하고 조인.
domain = pd.read_csv('Data/domain.csv')
domain.head()

data = pd.merge(data, domain, on = 'mac', how = 'right')
data.head()

##### 그래프 그리기
# 한글 사용하기
import platform
import matplotlib.pyplot as plt
import seaborn as sns

path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

plt.rcParams['axes.unicode_minus'] = False

# 가구원수별 월별 평균 전력량
FamilyMonth_mean = data.pivot_table('elec',
                                    index = 'family',
                                    columns = 'month',
                                    aggfunc = 'mean')
FamilyMonth_mean.head()

FamilyMonth_mean.to_csv('Data/Watt(가구원수별 월별 평균 전력량).csv',
                        encoding = 'euc-kr')




# 가구원수별 월별 전체 전력량
FamilyMonth_sum = data.pivot_table('elec',
                                   index = 'family',
                                   columns = 'month',
                                   aggfunc = 'sum')
FamilyMonth_sum.head()

FamilyMonth_sum.to_csv('Data/Watt(가구원수별 월별 전체 전력량).csv',
                        encoding = 'euc-kr')

# 월별 평균 전력량
Month_mean = data.pivot_table('elec',
                              index = 'month',
                              aggfunc = 'mean')
Month_mean.head()

Month_mean.to_csv('Data/Watt(월별 평균 전력량).csv',
                  encoding = 'euc-kr')


Month_mean.plot()

# 월별 전체 전력량
Month_sum = data.pivot_table('elec',
                             index = 'month',
                             aggfunc = 'sum')
Month_sum.head()

Month_sum.to_csv('Data/Watt(월별 전체 전력량).csv',
                 encoding = 'euc-kr')

Month_sum.plot(kind = 'bar')

# 가구원수별 평균 전력량
Family_mean = data.pivot_table('elec',
                               index = 'family',
                               aggfunc = 'mean')
Family_mean.head()

Family_mean.to_csv('Data/Watt(가구원수별 평균 전력량).csv',
                  encoding = 'euc-kr')

Family_mean.plot(kind = 'bar')


# 가구원수별 전체 전력량
Family_sum = data.pivot_table('elec',
                              index = 'family',
                              aggfunc = 'sum')
Family_sum.head()

Family_sum.to_csv('Data/Watt(가구원수별 전체 전력량).csv',
                  encoding = 'euc-kr')

Family_sum.plot(kind = 'bar')


# 유저별 평균 전력량
User_mean = data.pivot_table('elec',
                             index = 'user_id',
                             aggfunc = 'mean')
User_mean.head()

User_mean.to_csv('Data/Watt(유저별 평균 전력량).csv',
                 encoding = 'euc-kr')

User_mean.plot(kind = 'bar')

# 유저별 전체 전력량
User_sum = data.pivot_table('elec',
                            index = 'user_id',
                            aggfunc = 'sum')
User_sum.head()

User_sum.to_csv('Data/Watt(유저별 전체 전력량).csv',
                encoding = 'euc-kr')