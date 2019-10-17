import pandas as pd
import numpy as np


# 데이터 불러오기
weather = pd.read_csv('Data/2014-2018 시간별 기상데이터1.csv',
                      encoding = 'euc-kr')
weather

energy = pd.read_csv('Data/2014-2018 월별 시간대 평균 전력량1.csv',
                      encoding = 'euc-kr')
energy

len(weather)
len(energy)
energy.describe()
# 전력량 최소 670, 최대 1387, 평균 999.925694

import random as rd
rd.randint(670, 1387)

wattage = []
for i in range(len(weather)):
    wattage.append(rd.randint(670, 1387))

len(wattage)

data = pd.DataFrame(weather)
data['wattage'] = wattage
data.head()

data.to_csv('Data/wattage.csv',
            index = False,
            encoding = 'euc-kr')
