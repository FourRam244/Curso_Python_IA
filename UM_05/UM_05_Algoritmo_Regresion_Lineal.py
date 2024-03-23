"""
Modelo de Regresion
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dataset=pd.read_csv("./UM_05/Archivos/Salary_Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, -1].values

X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=1/3, random_state=0)  #variables independientes
print(X_train)
print(y_train)
regressor = LinearRegression()
regressor.fit(X_train,y_train) #Entrenar

y_predict= regressor.predict(X_test)
print(f"Predicciones: {y_predict}")

#Comparar predicciones vs valores originales Graficamente
plt.scatter(X_train,y_train,color="red")
plt.plot(X_train,regressor.predict(X_train),color="blue")
plt.title("Salario vs Experiencia (Entrenamiento conjunto)")
plt.xlabel("Años de experiencia")
plt.ylabel("Salario")
plt.show()


#Comparar predicciones vs valores originales Graficamente
plt.scatter(X_test,y_test,color="red")
plt.scatter(X_test,y_predict,color="green")
plt.plot(X_train,regressor.predict(X_train),color="blue")
plt.title("Salario vs Experiencia (Testeo conjunto)")
plt.xlabel("Años de experiencia")
plt.ylabel("Salario")
plt.show()

#prediccion simple
print(f"Salario predecible: {regressor.predict([[12]])}") #predecir salario de alguien con 12 años de experiencia
print(f"Coeficiente de regresion: {regressor.coef_}")
print(f"Coeficiente de y intercepto: {regressor.intercept_}")