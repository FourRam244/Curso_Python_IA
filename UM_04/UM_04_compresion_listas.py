"""
(List Compresion)
-Es una manera maas compacta de crear listas en comparacion con los blucles tradionales
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
