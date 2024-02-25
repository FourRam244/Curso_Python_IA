"""
Blucle For
-Se utliza cunado conocemos las veces que el bucle va a iterar
Sintaxis:

for <var> in range (v1,vf,step):
    <cuerpo del bucle>
else:
    <nada que iterar>
<fin bucle>

"""
#for vuelta in range(5,10,2):
    #print(f"{vuelta} Bienveniedo al Cruso de Python")
#print("Fin bucle")

"""
Imprimir una lista con numeros pares(1,10)
Las listas se pueden crear de dos formas:
Ejemplo:
pares = list()
impares = []
"""
# lista_pares=list()#Constructor
# lista_impares=list()
# for vuelta in range(1,11):
#     if vuelta %2 ==0:
#         lista_pares.append(vuelta)
#     else:
#         lista_impares.append(vuelta)

# print(f"Lista de pares {lista_pares}")  #Es necesario la f para imprimir las listas
# print(f"Lista de impares {lista_impares}") #la f de formato es para inyectar }

"""
Crear un programa que recorra una lista y cuando encuentre el primer numero 
impar detenga el blucle
Break. -Termina la ejecucion del bucle 
"""
# numeros =[2,4,1,6,8,9,10]
# for vuelta in numeros: #ingresa a la lista y cada valor lo guarda en vuelta
#     if vuelta %2 !=0:
#         print(f"El primer numero impar que encontro fue {vuelta}")
#         break #interrumpir la ejecucion del bucle
    
"""
#Excluye los impares
numeros=[1,2,3,4,5,6,7,8,9,10]
for vuelta in numeros:
    if vuelta %2 !=0:
        continue #salta el valor actual del bucle
    print(vuelta)
         
"""

"""
1.-Si encuentra el numero 0 debes inmprimir un mensaje indicando que se interrumpio el blucle
2.-si el bucle completa la interacion sin interrumpciones se imprime un mensaje
indicando que el bucle ha recorrido todos lo numeros sin interruipcion
NOTA: En Python, es posible utilizar la cláusula *else* junto con un ciclo *for*. La cláusula else en un ciclo 
for se ejecuta cuando el 
ciclo termina de iterar sobre todos los elementos del iterable, 
es decir, cuando el ciclo no se interrumpe por una declaración break.
"""
numeros=[1,2,3,0,5]

for numero in numeros:
    if numero==0:
        print("El numero es 0, El bucle se interrumpio")
        break #para salir del bucle 
    print(f"Procesando el numero {numero}")
else:
    print("El blucle a recorrido todos los numeros sin interrupcciones")
