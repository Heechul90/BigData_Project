import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 데이터 불러오기
raw_data = pd.Series.from_csv('Data/Watt(시계열 일별 전체 전력량).csv',
                              header = 0,
                              encoding = 'euc-kr',
                              parse_dates = True)

# raw_data1 = pd.read_csv('Data/Watt(시계열 일별 전체 전력량).csv',
# #                               encoding = 'euc-kr')
# #
# # raw_data1.describe()

data = raw_data.copy()
data.head()
data.dtypes

data = data.iloc[0:1461,]
data.tail()

data = data[:].astype(np.float)
data.tail()

data.plot()
plt.show()


from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(data)
plot_pacf(data)
plt.show()


from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults

model = ARIMA(data, order = (1, 1, 0))
model_fit = model.fit(trend = 'nc', full_output = True, disp = 1)
print(model_fit.summary())

model_fit.plot_predict()


fore = model_fit.forecast(steps = 1)
print(fore)

# 2018년 1월 1일 전력량 763473.4587

