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



# seed 값 설정
seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)


# 데이터 불러오기
dataset = pd.read_csv('Data/dataset2(watt).csv',
                      index_col = 0,
                      encoding = 'euc-kr')

dataset.head()
data = dataset.copy()


# 1. 데이터 확인하기
data.info()
data.head()

data = data.values
X = data[:,0:8]
Y = data[:,8]


# 학습셋 70%, 테스트셋 30% 설정
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                    test_size = 0.3,     # 테스트셋 30%
                                                    random_state = seed)



# 모델 설정하기
model = Sequential()
model.add(Dense(24, input_dim = 8, activation = 'relu'))
model.add(Dense(16, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(4, activation = 'relu'))
model.add(Dense(1))



# 모델 컴파일 하기
model.compile(loss = 'mean_squared_error',
              optimizer = 'adam')


# 모델 실행
model.fit(X_train, Y_train, epochs = 200, batch_size = 10)

print('\n Accuracy: %.4f' % (model.evaluate(X_train, Y_train)[1]))


# 예측 값과 실제 값의 비교
Y_prediction = model.predict(X_test).flatten()
for i in range(100):
    label = Y_test[i]
    prediction = Y_prediction[i]
    print("실제전력량: {:.3f}, 예상전력량: {:.3f}".format(label, prediction))
