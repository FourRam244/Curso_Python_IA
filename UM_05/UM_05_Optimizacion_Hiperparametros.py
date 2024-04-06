import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
train_df = pd.read_csv("./UM_05/Archivos/dc_airbnb_train.csv")
test_df = pd.read_csv("./UM_05/Archivos/dc_airbnb_test.csv")
features = ["accommodates", "bedrooms","bathrooms","number_of_reviews"]
hyper_params=range(1,21)
mse_values= list()

for hp in hyper_params:
    knn= KNeighborsRegressor(n_neighbors=hp, algorithm="brute")
    knn.fit(train_df[features],train_df["price"])
    predictions= knn.predict(test_df[features])
    mse=mean_squared_error(test_df["price"],predictions)
    mse_values.append(mse)
print(mse_values)

best_k= hyper_params[np.argmin(mse_values)]
print("k optimo",best_k)
print("minimo mse:", np.min(mse_values))

plt.plot(mse_values,"or")
plt.plot(mse_values)
plt.xlabel("K")
plt.ylabel("MSE")
plt.show()
