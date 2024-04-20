import pandas as pd
import numpy as np

data = pd.read_csv('./UM_05/Archivos/AmesHousing.csv')

train = data[0:1460]
test = data[1460:]
numerical_train = train.select_dtypes(include=['int','float'])
numerical_train = numerical_train.drop(['PID', 'Year Built', 'Year Remod/Add', 'Garage Yr Blt', 'Mo Sold', 'Yr Sold'], axis=1)

null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series == 0]
print(full_cols_series)

#Eliminacion de los OLS
features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area', 'Gr Liv Area', 'Overall Qual']

X = train[features]
X['bias'] = 1
X = X[['bias']+features]
y = train['SalePrice']

first_term= np.linalg.inv(np.dot(np.transpose(X),X))
second_term= np.dot(np.transpose(X),y)
ols_estimation= np.dot(first_term,second_term)
print("Cuadrados minimos ordinarios:")
print(ols_estimation)

#Caracteristicas de procesamiento y transformacion
train_null_counts = train.isnull().sum()
print(train_null_counts)
df_no_mv = train[train_null_counts[train_null_counts == 0].index]
print(df_no_mv)