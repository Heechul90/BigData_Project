import numpy as np
import pandas as pd
import seaborn as sns


# 데이터 불러오기
dataset = pd.read_csv('Data/dataset(watt).csv',
                      index_col = 0,
                      encoding = 'euc-kr')

dataset.head()
data = dataset.copy()


data.dtypes
data1 = data.corr()


mask[np.tril_indices_from(mask)]  = False
mask = np.array(data1)
sns.heatmap(data1, mask = mask, vmax=.8, square=True, annot=True)

