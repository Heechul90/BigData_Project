import numpy as np
import pandas as pd

data = pd.read_csv('Data/2014-2018 시간별 기상데이터1.csv',
                   encoding = 'euc-kr')

data.columns
tem_mean = data.pivot_table('평균기온(°C)',
                            index = 'year',
                            aggfunc = 'mean')

tem_mean['증감율'] = (tem_mean['평균기온(°C)'] / 13.498082)
tem_mean