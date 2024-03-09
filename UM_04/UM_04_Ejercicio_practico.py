"""
Crea un programa para automaatizar la planilla de sueldos de una empresa
con las siguientes caracteristicas
1.- Se debe tener algunos empleados yaa registrados en diccionarios (3)
2.- Se debe tener la posibilidad de poder ingresar nuevos empleados
3.- Se debe poder calcular la suma de sueldos y se de be de obtener el promedio de ese mes
4.- Posibilidad de visualizarlo
5.- Utilizar excepciones y funciones

"""
trabajadores = [
    {"codigo":"Trab_01","ht":40},#0
    {"codigo":"Trab_02","ht":46},#1
    {"codigo":"Trab_03","ht":50},#2
]
pago_hora=20

def registro_empleado(codpar,htpar):
    try:
        nuevo_empleado={
            "codigo":codpar,
            "ht":htpar
        }
        trabajadores.append(nuevo_empleado)
    except Exception as err:
        return f"Ocurrio un error {err}"
    else:
        return"Empleado agregado con exito!!"
def listar_empleado():
    try:
        global pago_hora
        sum_horas=0
        for index,empleado in enumerate(trabajadores):
            total_pago=trabajadores[index]["ht"]*pago_hora
            sum_horas+=total_pago
        return f"La suma total de la planilla es {sum_horas} y el promedio {sum_horas/len(trabajadores)}"
    except Exception as err:
        return f"Ocurrio un error {err}"
    
while True:
    codigo=input("Ingrese el codigo: ")
    ht=int(input("Ingrese las horas trabajadas: "))
    registro_empleado(codigo,ht)
    resp=input("¿Desea continuar?: ")
    if resp =="n":
        break

print(listar_empleado())
