"""
Trabajando con fechas
from datetime import datetime
fecha_actual=datetime.now()
print(fecha_actual)
"""

"""
Tipos de datos en python (Primitivos)
1- Numericos 
-int
-float
2.- Cadenas
-str
3.-Logicos
-bool
4.- Estructuras de Datos
-Listas
-Tuplas
-Diccionarios
-Conjuntos (set)
"""

"""
PEP8="Propuesta de mejora en python"
"""

#Snake_case
    #Malo
    #x=5
    #y="hola"




#print(type(nombre_curso)) #str
#print(type(str(precio_curso))) #float a str
#print(type(int(estado_curso))) #bool a int
#print(int(precio_curso))



"""
Conversion de datos (cast)
-int
-str
-float
-bool

"""
#print(type(nombre_curso)) #str
#print(type(str(precio_curso))) #float a str
#print(type(int(estado_curso))) #bool a int
#print(int(precio_curso))


"""
Formato de cadena
"""
nombre_curso="Python" #str
profesor_curso="Armando"
precio_curso= 1299.99999 #float
horas_curso=66 #int
estado_curso=True #bool
participantes=["Victor", "Jair", "Luis","Armando"] #list

cadena=nombre_curso + profesor_curso #concatena al ser str
total= precio_curso + horas_curso
#cadena2=nombre_curso + precio_curso  #Error al concatenar al no ser del mismo tipo
cadena2=nombre_curso + str(precio_curso) #al convertir precio_curso a str ya concatena
cadena3=f"Este es el nombre del curso {nombre_curso} y su precio {round(precio_curso,3)} y su profesor es {profesor_curso}  y el primer alumno matriculado es {participantes[0]}" #otra forma de concatener cadenas con varibles
#round(precio_curso,3) funcion para poder redondear a 3 decimales
print(cadena3)
