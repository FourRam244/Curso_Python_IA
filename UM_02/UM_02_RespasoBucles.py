"""
Crear un programa que ingrese 3 notas de un alumno y calcule
su promedio general y me indique si el alumno aprobo o no el curso
"""
# suma=0
# contador=0
# for nota in range(3):
#     notas=float(input(f"Ingrese la nota:{nota}: "))
#     suma+=notas #Acumulando notas
#     contador+=1 #contando notas
# promedio=suma/contador
# 15
# if promedio >=10.5:
#     print("El alumno aprobo el curso")
# else:
#     print("El alumno desaprobo el curso")

def calcular_notas():
    try:
        lista_notas=list()
        for nota in range(3):
            notas=float(input(f"Ingrese la nota:{nota}: "))
            lista_notas.append(notas)
        suma_notas=sum(lista_notas)
        promedio=suma_notas/3
        mensaje="Aprobo el curso" if promedio  >= 10.5 else "No aprobo el curso"
        return mensaje
    except Exception as err:   #Exception captura el error y lo guarda en la variable err
        print(f"Ocurrio un error {err}")
    else: 
        print("Todo correctamente")
        pass
    finally:
        print("Cerrando todos  los objetos")
        pass #cuando no tienes bloque de condigo que poner
calcular_notas()

"""
Una excepción es un evento que ocurre durante la ejecución de un programa y que 
interrumpe el flujo normal de ejecución debido
 a algún tipo de error o condición inesperada.

 Básicamente, pass no hace nada y se utiliza para evitar errores de sintaxis cuando 
 la sintaxis de Python requiere que haya alguna declaración. Es como el { } en Java
"""