import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dc_listing = pd.read_csv("./UM_05/Archivos/dc_airbnb.csv")
#print(dc_listing)

#Funciones para leer los data frame
#print(dc_listing.iloc[0])
"""
Obtener información sobre sus columnas y tipos de datos
Te dará detalles sobre el número de filas, el nombre de las columnas,
 los tipos de datos de las columnas y el uso de memoria
"""
#dc_listing.info()
"""
Obtener un resumen estadístico de las columnas numéricas
Esto incluirá estadísticas como el recuento, la media, la desviación estándar, 
los valores mínimos, los percentiles y los valores máximos para las columnas numéricas.
"""
#dc_listing.describe()
#Generar historgrama
dc_listing.hist(bins=30, figsize=(20,20), color="r")
# Ajusta el diseño y la apariencia del histograma

#plt.show()


our_acc_vvalue = 3 
firts_living_space_value= dc_listing.iloc[0]["accommodates"]
first_distance=np.abs(firts_living_space_value - our_acc_vvalue) #calcular el valor absoluto
print(first_distance)

new_listing=3
dc_listing["distance"]= dc_listing["accommodates"].apply(lambda x: np.abs(x-new_listing))
print(dc_listing["distance"].value_counts())


"""
borrar un columna especifica
"""
#dc_listing.drop(["distance"],axis=1)
#Semilla de aleatoriedad
np.random.seed(1)
#Reordena alaetoriamente todas las filas del data set
dc_listing = dc_listing.loc[np.random.permutation(len(dc_listing))]
dc_listing= dc_listing.sort_values("distance") #ordena de manera ascendente por distancia
print(dc_listing.iloc[0:10]["price"]) #imprimir las primeras 10 filas
"Realizar limpieza"
stripped_commas= dc_listing["price"].str.replace(",","")
stripped_dollars= stripped_commas.str.replace("$","")
dc_listing["price"]=stripped_dollars.astype("float") #Volver a convertir a float
mean_price= dc_listing.iloc[0:5]["price"].mean()  #Calcular la media de precio
print(f"Precio de renta sugerido para una habitacion de 3 acomodados: ${mean_price}") #precio de renta sugerido para una habitacion de 3 acomodados