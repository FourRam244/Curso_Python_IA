"""
Caracteristicas Python
*************************
1.-Software Libre
2.-Comunidad Colaborativa (Escalable)
3.-Modulos, Bibliotecas (Repositorios)
4.-Multiplataforma (py) -Interprete
5.-Frameworks Poderosos (Django-Flask)
(Pandas, Nompy, Maatplotlib, Seaborn, TensorFlow)
6.-Portable
7.-Interpretado
8.-Mulrtiparadigma

Un modulo es un archivo que contiene codigo de python incluyendo variables
funciones, y clases que pueden ser reutilizados en otros programas

"""
import math
# print(f"El valor de pi es: {math.pi}")
# print(f"El valor de la raiz cuadrada de 4 es: {math.sqrt(4)}")
# print(f"El coceno de pi/4 es: {math.cos(math.pi/4)}")
# print(f"X elevado a la potencia de Y es: {math.pow(2,3)}") #Calcula X elevado a Y
# print(f"El factorial de 5 es: {math.factorial(5)}")
# print(f"El numero de euler es: {math.e}")

"""
calcular seno, coseno u tangente de un angulo de radianes
math.sin(x)
math.cos(x)
math.tan(x)
calcular el logaritmo naturaal y logariitmo base 10
math.log(x)
math.log10(x)
Convertir angulo entre grados y radianes
math.radians(x)
math.degress(x)

"""
import statistics
# datos=[2.90, 10.5, 14.7, 23.7, 10.5]
# print(f"La media aritmetica es {statistics.mean(datos)}")
# print(f"La varianzaa es {statistics.variance(datos)}")
# print(f"La moda es: {statistics.mode(datos)}")
# print(f"La desviacion estadar es: {statistics.stdev(datos)}")

"""
mean: Caalcula la media
median: Calcula la mediana
mode: Calucla la moda
stdev: Calcula la desviacion estadar
variance: Calcula la varianza 
"""
import random
#Genera un numero aleatorio entre 1-10
# print(f"Numero generado es: {random.randint(1,10)}")
#Generar numero aleatorio de punto flotante entre 0-1
# print(f"Numero aleatorio con punto flotante: {random.random()}")
#Elegir un elemento de una lista
alumnos=["Jose", "Pedro","Rosa","Manuel"]
# print(f"Escoje al azar {random.choice(alumnos)}")
#Barajar una lista aleatoriamente
frutas=["Manzana","Naranja","Platano","Uva"]
barajado=random.sample(frutas,len(frutas))
# print(f"Lista Barajada {barajado}")
#Secuencia aleatoria de 5 numero de punto flotante
secuencia_aleatoria=[random.uniform(1,100) for _ in range(5)]
#genera un numero de punto flotante aleatorio entre a y b 
#print(f"La secuencia aleatoria es: {secuencia_aleatoria}")
#Iniciaalizar laa semilla con un numero especifico
random.seed(42)
numero_aleatorio1=random.random()
numero_aleatorio2=random.randint(1,100)
# print(numero_aleatorio1)
# print(numero_aleatorio2)
import sys
print(f"La version de python utilizada en este curso {sys.version}")
print(f"Obtener el path de los modulos {sys.path}")
sys.exit("Mensaje de error y codigo de salida")