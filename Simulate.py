import pandas as pd
import numpy as np
from random import *



# 데이터 불러오기
raw_CusInfo = pd.read_csv('Data/고객정보.csv',
                          encoding = 'euc-kr')

raw_CusInfo

cusinfo = raw_CusInfo.copy()
cusinfo.dtypes
cusinfo['구성원수'][96]

power = []

for i in range(10):

    for j in cusinfo['구성원수']:

        if cusinfo['구성원수'][j] == 1:
            power1 = uniform(0.271300, 0.302311)
            power.append(power1)

        if cusinfo['구성원수'][j] == 2:
            power1 = uniform(0.271300, 0.302311)
            power.append(power1)

        if cusinfo['구성원수'][j] == 3:
            power1 = uniform(0.271300, 0.302311)
            power.append(power1)

        if cusinfo['구성원수'][j] == 4:
            power1 = uniform(0.271300, 0.302311)
            power.append(power1)

        if cusinfo['구성원수'][j] == 5:
            power1 = uniform(0.271300, 0.302311)
            power.append(power1)

        if cusinfo['구성원수'][j] == 6:
            power1 = uniform(0.271300, 0.302311)
            power.append(power1)

        if cusinfo['구성원수'][j] == 7:
            power1 = uniform(0.271300, 0.302311)
            power.append(power1)

        if cusinfo['구성원수'][j] == 8:
            power1 = uniform(0.271300, 0.302311)
            power.append(power1)

        if cusinfo['구성원수'][j] == 9:
            power1 = uniform(0.271300, 0.302311)
            power.append(power1)

power