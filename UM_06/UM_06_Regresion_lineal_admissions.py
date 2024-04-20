import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

admissions = pd.read_csv('./UM_05/Archivos/admission.csv')
print(admissions)
model = LogisticRegression(class_weight="balanced")
admissions.info()
model.fit(admissions[["gpa"]],admissions["admit"])

labels=model.predict(admissions[["gpa"]])
admissions["predicted_label"]=labels
print(admissions["predicted_label"].value_counts)
print(admissions.head())

#matriz de confusion
confussion_mtx= confusion_matrix(admissions["admit"],admissions["predicted_label"])
print(confussion_mtx)
accuracy=accuracy_score(admissions["admit"], admissions["predicted_label"])

print("AcCuracy",accuracy)



#Multivariable con todas las columnas
model.fit(admissions[["gpa","gre","rank"]],admissions["admit"])

labels=model.predict(admissions[["gpa","gre","rank"]])
admissions["predicted_label"]=labels
print(admissions["predicted_label"].value_counts)
print(admissions.head())

#matriz de confusion
confussion_mtx= confusion_matrix(admissions["admit"],admissions["predicted_label"])
print(confussion_mtx)
accuracy=accuracy_score(admissions["admit"], admissions["predicted_label"])

print("AcCuracy",accuracy)
