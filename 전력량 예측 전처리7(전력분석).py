import numpy as np
import pandas as pd
import seaborn as sns

# 선형 회귀
from keras.models import Sequential  # 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

import numpy as np                # 필요한 라이브러리를 불러옵니다.
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

if type(tf.contrib) != type(tf):  # warning 출력 안하기
    tf.contrib._warning = None


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
dataset = pd.read_csv('Data/dataset2(watt).csv',
                      index_col = 0,
                      encoding = 'euc-kr')

data = dataset.copy()

# 1. 데이터 확인하기
data.dtypes
data.columns
data.head()
data.describe()


# 2. 다중선형회귀분석
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls\_prediction\_std

