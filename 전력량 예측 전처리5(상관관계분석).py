import numpy as np
import pandas as pd
import seaborn as sns

# 한글 사용하기
import platform
import matplotlib.pyplot as plt

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



# 데이터 불러오기
dataset = pd.read_csv('Data/dataset.csv',
                      index_col = 0,
                      encoding = 'euc-kr')

dataset.head()
data = dataset.copy()


data.dtypes
data1 = data.corr()


mask = np.array(data1)
mask[np.tril_indices_from(mask)]  = False
sns.heatmap(data1, mask = mask, vmax=.8, square=True, annot=True)



data.columns

del data['일강수량(mm)']
del data['최대 풍속(m/s)']
del data['평균 풍속(m/s)']
del data['최다풍향(16방위)']
del data['평균 상대습도(%)']
del data['합계 일조시간(hr)']
del data['일 최심적설(cm)']
del data['평균 전운량(1/10)']
del data['평균 중하층운량(1/10)']

data.columns
data.head()


data.to_csv('Data/dataset2.csv',
            encoding = 'euc-kr')
