import pandas as pd
import numpy as np
from scipy.spatial import distance
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

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
#print(f"Columnas normalizadas: \n{normalized_col}")
# normalized_col= first_transform / dc_listing["maximum_nights"].std()  //Forma simplificada

#Normalizar todas las columnas
normalized_listings = (dc_listing - dc_listing.mean()) / (dc_listing.std())
normalized_listings["price"]=dc_listing["price"]
#print(normalized_listings.head(3))

first_listing = normalized_listings.iloc[0][["accommodates","bathrooms"]]
fifth_listing = normalized_listings.iloc[4][["accommodates","bathrooms"]]
#Calcular la distancia euclidia entre la primera y la quinta fila
first_fifth_distance = distance.euclidean(first_listing,fifth_listing)
#print(f"La distancia euclidea: {first_fifth_distance}")

knn= KNeighborsRegressor(algorithm="brute")  #busqueda por fuerza bruta
#Definir conjunto de entrenamiento y testeo
train_df= normalized_listings.iloc[0:2792]
test_df= normalized_listings.iloc[2792:]
#Caracteristicas de entrenamiento
train_features=train_df[["accommodates","bathrooms"]]
train_target=train_df["price"] #objetivo
knn.fit(train_features, train_target)  #entrenar

#prediciones
predicctions= knn.predict(test_df[["accommodates","bathrooms"]]) #de todos los accommodates y baños
#print(predicctions)


train_columns=["accommodates","bathrooms"]
knn= KNeighborsRegressor(n_neighbors=5,algorithm="brute",metric="euclidean")  #5 vecinos, busqueda por bruto y metrica euclideana
knn.fit(train_df[train_columns],train_df["price"]) #Entrenamiento
predicctions=knn.predict(test_df[train_columns])

two_features_mse= mean_squared_error(test_df["price"],predicctions) #error cuadratico medio
two_features_rmse=two_features_mse**(1/2) #Raiz del error cuadratico medio
print(f"Raiz del error cuadratico medio: {two_features_rmse}")



train_columns=["accommodates","bathrooms","bedrooms","number_of_reviews"]
knn= KNeighborsRegressor(n_neighbors=5,algorithm="brute",metric="euclidean")  #5 vecinos, busqueda por bruto y metrica euclideana
knn.fit(train_df[train_columns],train_df["price"]) #Entrenamiento
predicctions=knn.predict(test_df[train_columns])

four_features_mse= mean_squared_error(test_df["price"],predicctions) #error cuadratico medio
four_features_rmse=four_features_mse**(1/2) #Raiz del error cuadratico medio
print(f"Raiz del error cuadratico medio: {four_features_rmse}")


train_columns=["accommodates","bathrooms","bedrooms"]
knn= KNeighborsRegressor(n_neighbors=5,algorithm="brute",metric="euclidean")  #5 vecinos, busqueda por bruto y metrica euclideana
knn.fit(train_df[train_columns],train_df["price"]) #Entrenamiento
predicctions=knn.predict(test_df[train_columns])

three_features_mse= mean_squared_error(test_df["price"],predicctions) #error cuadratico medio
three_features_rmse=three_features_mse**(1/2) #Raiz del error cuadratico medio
print(f"Raiz del error cuadratico medio bedrooms: {three_features_rmse}")


train_columns=["accommodates","bathrooms","number_of_reviews"]
knn= KNeighborsRegressor(n_neighbors=5,algorithm="brute",metric="euclidean")  #5 vecinos, busqueda por bruto y metrica euclideana
knn.fit(train_df[train_columns],train_df["price"]) #Entrenamiento
predicctions=knn.predict(test_df[train_columns])

three2_features_mse= mean_squared_error(test_df["price"],predicctions) #error cuadratico medio
three2_features_rmse=three2_features_mse**(1/2) #Raiz del error cuadratico medio
print(f"Raiz del error cuadratico medio number_of_reviews: {three2_features_rmse}")

#------------------------------------------------
knn= KNeighborsRegressor(n_neighbors=5,algorithm="brute")#5 vecinos, busqueda por bruto
features= train_df.columns.tolist()
features.remove("price")

knn.fit(train_df[features],train_df["price"])#Entrenamiento
all_features_predictions= knn.predict(test_df[features])
all_features_mse= mean_squared_error(test_df["price"],all_features_predictions)
all_features_rmse=all_features_mse**(1/2)
print(f"Raiz del error cuadratico medio: {all_features_mse}")
print(f"Raiz del error cuadratico medio: {all_features_rmse}")