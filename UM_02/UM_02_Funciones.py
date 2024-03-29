"""
Funciones definidas por el usuario (DUF)
-Es  un bloque de codigo que se puede reutilizar y 
permite recibir parametros(Argumentos).
Retorna uno o varios valores

Nota: Cuando una función regresa varios valores, los regresa en una tupla. 
Esta se puede desempaquetar en varias variables.
"""
def mensaje_bienvenida(nom=None): #None "que no sea mandatorio"
    #Contenido de la funcion
    mensaje=f"Bienvenido al curso {nom} de Python con IA"
    return mensaje
#print(mensaje_bienvenida())

def obtener_resultado():
    resultado1=42
    resultado2="Hola mundo"
    resultado3=[1,2,3]
    return resultado1,resultado2,resultado3

valor1,valor2,valor3=obtener_resultado()
#print(f"Los valores obtenidos {valor1} {valor2} {valor3[2]}")

"""
Funciones Recursivas
-Es una funcion que se llama asi misma durante su ejecucion
-Funcion que me permite hallar el factorial de un numero
5(5!)
5!=5*4*3*2*1=120
"""

def factorial (n):
     try:
         #Caso base: factorial de 0 o 1 es 1
         if n==0 or n==1:
             return 1
         else:
             #Caso recursivo n"=n*(n-1)!
             return n*factorial(n-1)
     except Exception as err:
         print(f"ocurrio un error {err}")
# #Ejemplo de uso 

# resultado=factorial(5)
# print(f"El factorial de 5 es {resultado}")

"""
Funciones Lambda

Son pequeñas funciones que generalamente se define en una linea
"""

def cuadrado(num):
    resultado= num**2
    return resultado
#Forma reducida de lo anterior con lambda
cuadrado= lambda num:num**2
numero=4
#print (f"El cuadrado de un numero es: {cuadrado(numero)}")


def sumar(n1,n2):
    resultado=n1+n2
    return resultado
#Forma reducida de lo anterior con lambda
suma_lan=lambda n1,n2:n1+n2


def par_impar(num):
    if num%2==0:
        resultado=f"El numero {num} es par"
    else:
        resultado=f"El numero es impar"
        return resultado
    
resultaado = lambda num:num%2==0