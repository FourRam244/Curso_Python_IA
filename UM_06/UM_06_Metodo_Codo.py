import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
dataset= pd.read_csv("./UM_05/Archivos/Mall_Customers.csv")
X= dataset.iloc[:, [3,4]].values
wcss=[]
for i in range (1,11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

#Graficacion
# plt.plot(range(1,11), wcss)
# plt.title("El metodo del codo")
# plt.xlabel("Numero de Clusters") #El valor obtimo es de 5 (clusters)
# plt.ylabel("WCSS")
#plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans= kmeans.fit_predict(X)
#Graficacion
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0,1], s = 100, c= 'red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1,1], s = 100, c= 'blue', label='Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2,1], s = 100, c= 'green', label='Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3,1], s = 100, c= 'cyan', label='Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4,1], s = 100, c= 'magenta', label='Cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='yellow', label='Centroides')
plt.title('Clusteres de clientes')
plt.xlabel('Ingreso Anual')
plt.ylabel('Spending score ')
plt.legend()
plt.show()




#Con 4 clusters
kmeans = KMeans (n_clusters=4, init="k-means++", random_state=42)
y_kmeans= kmeans.fit_predict(X)
#Graficacion
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0,1], s = 100, c= 'red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1,1], s = 100, c= 'blue', label='Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2,1], s = 100, c= 'green', label='Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3,1], s = 100, c= 'cyan', label='Cluster 4')


plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c="yellow", label="Centroide")
plt.title("Clusteres de clientes")
plt.xlabel("Ingreso Anual")
plt.ylabel("Puntuacion de gasto")
plt.legend()
plt.show()



#Con 6 clusters
kmeans = KMeans (n_clusters=6, init="k-means++", random_state=42)
y_kmeans= kmeans.fit_predict(X)
#Graficacion
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0,1], s = 100, c= 'red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1,1], s = 100, c= 'blue', label='Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2,1], s = 100, c= 'green', label='Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3,1], s = 100, c= 'cyan', label='Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4,1], s = 100, c= 'orange', label='Cluster 5')
plt.scatter(X[y_kmeans == 5, 0], X[y_kmeans == 5,1], s = 100, c= 'purple', label='Cluster 6')


plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c="yellow", label="Centroide")
plt.title("Clusteres de clientes")
plt.xlabel("Ingreso Anual")
plt.ylabel("Puntuacion de gasto")
plt.legend()
plt.show()




