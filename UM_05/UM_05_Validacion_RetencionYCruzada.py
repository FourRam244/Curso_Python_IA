import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
dc_listing= pd.read_csv("./UM_05/Archivos/dc_airbnb_normalized.csv")
#Se puede aplicar el barajeo aleatorio con random permutation
split_one = dc_listing.iloc[0:1862].copy()
split_two = dc_listing.iloc[1862:].copy()

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn = KNeighborsRegressor()
knn.fit(train_one[['accommodates']], train_one['price'])
test_one['predicted_price'] = knn.predict(test_one[['accommodates']])

iteration_one_mse = mean_squared_error(test_one['price'], test_one['predicted_price'])
iteration_one_rmse = iteration_one_mse ** (1/2)


knn = KNeighborsRegressor()
knn.fit(train_two[['accommodates']], train_two['price'])
test_two['predicted_price'] = knn.predict(test_two[['accommodates']])

iteration_two_mse = mean_squared_error(test_two['price'], test_two['predicted_price'])
iteration_two_rmse = iteration_two_mse ** (1/2)

print(iteration_one_rmse)
print(iteration_two_rmse)
rmse_mean = (iteration_one_rmse + iteration_two_rmse) / 2
print(rmse_mean)


#Validacion K-Fold
dc_listing.loc[dc_listing.index[0:734], "fold"] = 1
dc_listing.loc[dc_listing.index[734:1468], "fold"] = 2
dc_listing.loc[dc_listing.index[1468:2202], "fold"] = 3
dc_listing.loc[dc_listing.index[2202:2936], "fold"] = 4
dc_listing.loc[dc_listing.index[2936:3671], "fold"] = 5

print(dc_listing['fold'].value_counts())
print("Num of missing values: ",dc_listing['fold'].isnull().sum())

train_one = dc_listing[dc_listing["fold"] != 5].copy()
test_one = dc_listing[dc_listing["fold"] == 5].copy()
train_two = dc_listing[dc_listing["fold"] != 4].copy()
test_two = dc_listing[dc_listing["fold"] == 4].copy()
train_three = dc_listing[dc_listing["fold"] != 3].copy()
test_three = dc_listing[dc_listing["fold"] == 3].copy()
train_four = dc_listing[dc_listing["fold"] != 2].copy()
test_four = dc_listing[dc_listing["fold"] == 2].copy()
train_five = dc_listing[dc_listing["fold"] != 1].copy()
test_five = dc_listing[dc_listing["fold"] == 1].copy()

knn = KNeighborsRegressor()
knn.fit(train_one[['accommodates']], train_one['price'])
test_one['predicted_price'] = knn.predict(test_one[['accommodates']])

iteration_one_mse = mean_squared_error(test_one['price'], test_one['predicted_price'])
iteration_one_rmse = iteration_one_mse ** (1/2)
print(iteration_one_rmse)

knn = KNeighborsRegressor()
knn.fit(train_two[['accommodates']], train_two['price'])
test_two['predicted_price'] = knn.predict(test_two[['accommodates']])

iteration_two_mse = mean_squared_error(test_two['price'], test_two['predicted_price'])
iteration_two_rmse = iteration_two_mse ** (1/2)
print(iteration_two_rmse)

knn = KNeighborsRegressor()
knn.fit(train_three[['accommodates']], train_three['price'])
test_three['predicted_price'] = knn.predict(test_three[['accommodates']])

iteration_three_mse = mean_squared_error(test_three['price'], test_three['predicted_price'])
iteration_three_rmse = iteration_three_mse ** (1/2)
print(iteration_three_rmse)

#encontrar una forma de desarrollar los modelos de los 5 pliegues en un bucle for 
# Crear un array para almacenar los conjuntos de entrenamiento y prueba
data_sets = []

# Iterar sobre los diferentes valores de "fold"
for fold_value in range(1, 6):
    # Crear los conjuntos de entrenamiento y prueba para el valor de "fold" actual
    train_set = dc_listing[dc_listing["fold"] != fold_value].copy()
    test_set = dc_listing[dc_listing["fold"] == fold_value].copy()
    
    # Agregar los conjuntos a data_sets
    data_sets.append((train_set, test_set))

# Lista para almacenar los RMSE de cada iteración
rmse_list = []

for i in range(1, 6):
    # Crear el modelo KNN
    knn = KNeighborsRegressor()
    
    # Seleccionar los conjuntos de entrenamiento y prueba correspondientes
    train_set, test_set = data_sets[i-1]
    
    # Entrenar el modelo con el conjunto de entrenamiento actual
    knn.fit(train_set[["accommodates"]], train_set["price"])
    
    # Predecir los precios en el conjunto de prueba
    test_set["predicted_price"] = knn.predict(test_set[["accommodates"]])
    
    # Calcular el RMSE de la iteración actual
    iteration_mse = mean_squared_error(test_set["price"], test_set["predicted_price"])
    iteration_rmse = iteration_mse ** (1/2)
    
    # Agregar el RMSE a la lista
    rmse_list.append(iteration_rmse)
    
    # Imprimir el RMSE de la iteración actual
    print(f"Iteration {i} RMSE: {iteration_rmse}")