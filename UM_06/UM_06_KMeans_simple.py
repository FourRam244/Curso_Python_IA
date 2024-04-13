import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

dataset= pd.read_csv("./UM_05/Archivos/Position_Salaries.csv")
X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values
#Aqui el vector se debe de redimensaionar a 2 dimensiones por que la formula para 
#escalar carcteristicas necesita como parametro 
y = y.reshape(len(y),1)

sc_x = StandardScaler()
sc_y = StandardScaler()
X = sc_x.fit_transform(X)
y = sc_y.fit_transform(y)
print(X)

#Maquina de vector soporte SVR
regressor = SVR(kernel='rbf')
regressor.fit(X,y)
sc_y.inverse_transform(regressor.predict(sc_X.transform([6.5]).reshape(1, -1)))
plt.scatter(sc_x.inverse_transform(X), sc_y.inverse_transform(y), color="red")
plt.plot(sc_x.inverse_transform(X), sc_y.inverse_transform(regressor.predict(X)), color="blue")
plt.title("Estimado en Salario")
plt.xlabel("Nivel de la posicion")
plt.ylabel("Salario")
plt.show()