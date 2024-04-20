import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('./UM_05/Archivos/Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:,-1].values
lin_reg= LinearRegression()
lin_reg.fit(X,y)
poly_reg=  PolynomialFeatures(degree=4)
X_poly= poly_reg.fit_transform(X)
lin_reg_2= LinearRegression()
lin_reg_2.fit(X_poly,y)
print(X_poly)
#Graficamos
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Regresion Lineal')
plt.xlabel('Position Level')
plt.ylabel('Salario')
plt.show()


#Graficamos
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Regresion Polinomial')
plt.xlabel('Position Level')
plt.ylabel('Salario')
plt.show()