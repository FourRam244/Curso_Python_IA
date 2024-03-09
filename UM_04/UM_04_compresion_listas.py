"""
Lista por comprensión. Permite construir listas de una manera más compacta y legible, reduciendo la 
cantidad de código necesario en comparación con los enfoques tradicionales como usar bucles for.

Sintaxis: 

[expresion for elemento in iterable if condicion]


"expresion" es el valor que se va a incluir en la lista.

"elemento" es una variable que representa cada elemento del iterable.

"iterable" es una secuencia de elementos sobre la cual iteramos, como una lista, una tupla, un conjunto, o cualquier otro objeto iterable.

"condicion" es una expresión opcional que filtra los elementos del iterable.

"""

#Crear una lista de los cuadrados de los primeros 5 numeros
lista=list()
for x in range(1,6):
    valor=x**2
    lista.append(valor)
#print(lista)
    
"""
Forma de compresion
"""   
cuadrados=[x**2 for x in range(1,6)]
#print(cuadrados)

#Crear una lista de los cuadrados de los numeros para entre 1 y 10 
lista_valores=list()
for x in range (1,11):
    valor=x**2
    if valor % 2 ==0:
        lista_valores.append(valor)

#print(lista_valores)
"""
Forma de compresion
"""   
solo_pares=[x**2 for x in range(1,11) if x %2==0]
print(solo_pares)
