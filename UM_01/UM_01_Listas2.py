"""
sciling
Es una tecnica que te permite extrar una porcion (o subconjunto) }
de una lista o una cadena

Slicing (rebanado): Permite acceder a una parte de los elementos 
 de una estructura

Exclusive= No se muestra
Inclusive = Se muestra
"""
mi_lista=[1,2,3,4,5,6,7,8,9,20,22,23]
valor_maximo=max(mi_lista)
valor_minimo=min(mi_lista)
sumar_valores=sum(mi_lista)
cadena=f"El valor maximo es {valor_maximo}\n El valor minimo {valor_minimo}'\n La suma de valores {sumar_valores}"
#print(cadena)

#Obetener los elementos desde el indice 2(Inclusivoe) hasta el 5(Exclusive)
sublista=mi_lista[2:5]
#print(sublista)

#Obtener los elementos desde el principio hasta el indice 4(Exclusive)
sublista=mi_lista[:4]
#print(sublista)
#sublista=mi_lista[3:] #desde la posicion 3 hasta el ultimo indice
# sublista=mi_lista[-3:] #al usar elementos engativos sustrae de derecha a izquierda
# print(sublista)


valores=["Python",20,20.90,True,["Armando","Luis"]]  #Puede haber listas con diferentes tipos de datos hasta una lista dentro de otra lista
print(valores[4])