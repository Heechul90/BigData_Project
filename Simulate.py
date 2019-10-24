import pandas as pd
import numpy as np
from random import *



# 데이터 불러오기
raw_CusInfo = pd.read_csv('Data/고객정보.csv',
                          encoding = 'euc-kr')

PilotProject = pd.DataFrame(columns = ['CustomNum',
                                       'FamilyNum',
                                       'Power'])


for Num in range(1, 101):

    CustomNum = 'A' + str(Num)

    if Num >= 100:
        FamilyNum = 9
        Power = uniform(0.490484, 0.696090)
        PilotProject = PilotProject.append(pd.DataFrame([[CustomNum, FamilyNum, Power]],
                                                        columns=['CustomNum', 'FamilyNum', 'Power']))

    elif Num >= 99:
        FamilyNum = 8
        Power = uniform(0.607767, 0.679965)
        PilotProject = PilotProject.append(pd.DataFrame([[CustomNum, FamilyNum, Power]],
                                                        columns=['CustomNum', 'FamilyNum', 'Power']))

    elif Num >= 97:
        FamilyNum = 7
        Power = uniform(0.511305, 0.565084)
        PilotProject = PilotProject.append(pd.DataFrame([[CustomNum, FamilyNum, Power]],
                                                        columns=['CustomNum', 'FamilyNum', 'Power']))

    elif Num >= 95:
        FamilyNum = 6
        Power = uniform(0.519145, 0.570670)
        PilotProject = PilotProject.append(pd.DataFrame([[CustomNum, FamilyNum, Power]],
                                                        columns=['CustomNum', 'FamilyNum', 'Power']))

    elif Num >= 90:
        FamilyNum = 5
        Power = uniform(0.466227, 0.520347)
        PilotProject = PilotProject.append(pd.DataFrame([[CustomNum, FamilyNum, Power]],
                                                        columns=['CustomNum', 'FamilyNum', 'Power']))

    elif Num >= 65:
        FamilyNum = 4
        Power = uniform(0.444917, 0.494666)
        PilotProject = PilotProject.append(pd.DataFrame([[CustomNum, FamilyNum, Power]],
                                                        columns=['CustomNum', 'FamilyNum', 'Power']))

    elif Num >= 42:
        FamilyNum = 3
        Power = uniform(0.422958, 0.469866)
        PilotProject = PilotProject.append(pd.DataFrame([[CustomNum, FamilyNum, Power]],
                                                        columns=['CustomNum', 'FamilyNum', 'Power']))

    elif Num >= 14:
        FamilyNum = 2
        Power = uniform(0.378854, 0.424387)
        PilotProject = PilotProject.append(pd.DataFrame([[CustomNum, FamilyNum, Power]],
                                                        columns=['CustomNum', 'FamilyNum', 'Power']))

    else:
        FamilyNum = 1
        Power = uniform(0.271300, 0.302311)
        PilotProject = PilotProject.append(pd.DataFrame([[CustomNum, FamilyNum, Power]],
                                                        columns=['CustomNum', 'FamilyNum', 'Power']))




PilotProject

