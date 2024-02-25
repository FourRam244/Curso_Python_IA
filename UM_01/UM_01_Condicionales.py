# edad_persona=int(input("Ingrese la edad: "))
# if edad_persona >= 18:
#     #bloque True
#     print("La persona es mayor de edad")
# else:
#     #bloque flase
#     print("La persona es menor de edad")


"""
Area
=============
[S]istemas=2%
[M]arketing=3%
[C]ontabilidad=4%
0
"""

# area=input("Ingrese el area en el que labora: ")
# if area.lower()=="s":
#      bon=0.02
# elif area.lower()=="m":
#      bon=0.03
# elif area.lower()=="c":
#      bon=0.04
# else:
#     bon=0
# print(f"La bonificacion optenida es {bon}")

# frase="El Gran Elefante Blanco"
# print(frase.lower())


# nota=float(input("Ingrese la nota obtenida: "))
# if nota>=10.5:
#     print("El alumno aprobo el curso")
# else:
#     susti=float(input("Ingresa el sustitutorio: "))
#     prome=(susti+nota)/2
#     if prome>=10.5:
#         print("El alumno aprobo en el sustitutorio")
#     else:
#         print(f"El alumno debe llevar el curso nuevamente {prome}")

"""
Producto  calcular el descuento hacia un producto
=========================================
0 - 5= 0
6 - 20 = 0.02
21 - 50 = 0.03
>50 = 0.05
"""
precio=float(input("Ingrese el precio del producto: "))
if precio>=0 and precio <= 5:
    desc=0
elif precio>=6 and precio <= 20:
    desc=0.02
elif precio>=21 and precio <= 50:
    desc=0.03
else: 
    desc=0.05
print(f"El descuento obtenido es: {desc}")