import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset= pd.read_csv("./UM_05/Archivos/Social_Network_Ads.csv")
X = dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
X_train , X_test, y_train, y_test= train_test_split(X,y,test_size=0.25, random_state=0)
#print(X_train)

#Estandarizacion por medio de la libreria SKLearn
sc= StandardScaler()
X_train= sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)
print(X_train)