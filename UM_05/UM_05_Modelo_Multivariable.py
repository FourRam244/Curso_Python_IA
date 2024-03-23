import pandas as pd
import numpy as np
from scipy.spatial import distance


np.random.seed(1)
dc_listing=pd.read_csv("./UM_05/Archivos/dc_airbnb.csv")
#ordenar aleatoriamente el data set
dc_listing=dc_listing.loc[np.random.permutation(len(dc_listing))]
#Limpieza
stripped_commas= dc_listing["price"].str.replace(",","")
stripped_dollars= stripped_commas.str.replace("$","")
dc_listing["price"]=stripped_dollars.astype("float") #Volver a convertir a float
print(dc_listing.info())

#Eliminar varias columnas categoricas
drop_columns=["room_type","city","state","latitude","longitude","zipcode","host_acceptance_rate","host_listings_count","host_response_rate"]
dc_listing=dc_listing.drop(drop_columns,axis=1)
#print(dc_listing.isnull().sum()) #saber que columnas tiene mas data vacias
#Borrar las columnas que tienen mucha data vacia
dc_listing=dc_listing.drop(["cleaning_fee","security_deposit"],axis=1) #borrado vertical
dc_listing= dc_listing.dropna(axis=0) #borrado horizontal
print(dc_listing.isnull().sum()) #saber que columnas tiene mas data vacias
print(dc_listing)

#Normalizacion de valores
first_transform= dc_listing["maximum_nights"]- dc_listing["maximum_nights"].mean()
#obtener la columnas normalizadas
normalized_col= first_transform / first_transform.std()  #std te da la desviacion estandar
print(f"Columnas normalizadas: \n{normalized_col}")
# normalized_col= first_transform / dc_listing["maximum_nights"].std()  //Forma simplificada

#Normalizar todas las columnas
normalized_listings = (dc_listing - dc_listing.mean()) / (dc_listing.std())
normalized_listings["price"]=dc_listing["price"]
print(normalized_listings.head(3))

first_listing = normalized_listings.iloc[0][["accommodates","bathrooms"]]
fifth_listing = normalized_listings.iloc[4][["accommodates","bathrooms"]]
#Calcular la distancia euclidia entre la primera y la quinta fila
first_fifth_distance = distance.euclidean(first_listing,fifth_listing)
print(f"La distancia euclidea: {first_fifth_distance}")
