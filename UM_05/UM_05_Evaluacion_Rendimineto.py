import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dc_listing=pd.read_csv("./UM_05/Archivos/dc_airbnb.csv")
stripped_commas= dc_listing["price"].str.replace(",","")
stripped_dollars= stripped_commas.str.replace("$","")
dc_listing["price"]=stripped_dollars.astype("float") #Volver a convertir a float
num_train=int(len(dc_listing)*0.75) #75%

print(f"Numero de filas {num_train}")

train_df= dc_listing.iloc[0:num_train]
test_df = dc_listing.iloc[num_train:]
#print(test_df)

#Funcion de prediccion
def predic_price(new_listing):
    temp_df = train_df.copy()
    temp_df["distance"]= temp_df["bathrooms"].apply(lambda x: np.absolute(x- new_listing))
    temp_df=temp_df.sort_values("distance")
    nearest_neighbors= temp_df[0:5]["price"] #Tomando 5 vecinos cercanos de los precios
    predic_price=nearest_neighbors.mean()
    return(predic_price)

test_df["predic_price"]= test_df["bathrooms"].apply(predic_price)
print(test_df)
#Calcular error medio absoluto (MAE)
test_df["error"]=np.absolute(test_df["predic_price"]-test_df["price"])
mae=test_df["error"].mean()
print(f"Error medio absoluto: {mae}")

#Error cuadratico medio (MSE)
test_df["squared_error"]= (test_df["predic_price"]-test_df["price"])**(2)
mse=test_df["squared_error"].mean()
print(f"Error Cuadratico Medio: {mse}")

#Raiz del error cuadratico medio
rmse=mse**(1/2)
print(f"Raiz del error cuadratico medio: {rmse}")

errors_one = pd.Series([5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,10])
errors_two = pd.Series([5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,1000])
mae_one=errors_one.sum()/len(errors_one)
rmse_one=np.sqrt((errors_one**2).sum()/len(errors_one))
print("MAE ONE {}".format(mae_one))
print("RMSE ONE {}".format(rmse_one))


mae_two=errors_two.sum()/len(errors_two)
rmse_two=np.sqrt((errors_two**2).sum()/len(errors_two))
print("MAE two {}".format(mae_two))
print("RMSE two {}".format(rmse_two))
