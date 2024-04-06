import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dc_startups= pd.read_csv("./UM_05/Archivos/50_Startups.csv")
dc_startups.info()
#aplicar tranformacion a estado para volverlo 
X = dc_startups.iloc[:, :-1].values
y= dc_startups.iloc[:,-1].values

ct=ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [3])], remainder="passthrough")
X= np.array(ct.fit_transform(X))


X_train , X_test, y_train, y_test= train_test_split(X,y,test_size=0.2, random_state=0)
regressor=LinearRegression()
regressor.fit(X_train,y_train)

y_pred =  regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

#Supestos de distribucion de gastos
print("Ganancia final al año (prediccion):",regressor.predict([[1,0,0, 160000, 130000, 300000]]))

print("Coeficiente de regrecion:",regressor.coef_)
print("Intercepción del regresor:",regressor.intercept_)



