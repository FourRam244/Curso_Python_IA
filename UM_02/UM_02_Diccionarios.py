"""
Diccionarios 
-Almacenar datos en formato clave-valor
(key - value)
Estructura de datos
"""
mi_diccionario={}
mi_diccionario=dict()

mi_diccionario={
    "nombre":"Juan","edad":30,"ciudad":"california"
}

print(mi_diccionario["ciudad"])
print(mi_diccionario["nombre"])
print(mi_diccionario["edad"])

mi_diccionario["sexo"]="M" #Como insertar nueva clave y valor
mi_diccionario["ciudad"]="Washington" #Si ya esta la clave, remplaza el valor
del mi_diccionario["sexo"] #elimina la clave con "del"

#"get" busca un valor por su clave, si no encuentra el valor me devuelve el mensaje predeterminado
#lo que pusimos depues de ","
valor = mi_diccionario.get("altura","No existe valor") #get te captura el valor de la clave del diccionario

print(f"El valor del diccionario es {valor}")

#La funcion item te devuelve primero las claves que las guardamos en k,
# y el segundo son los valores que los guardamos en v
# for k ,v in mi_diccionario.items():  
#     print(f"La clave {k} y los valores {v}")

# print(mi_diccionario.keys()) #Muestras solo las claves
# print(mi_diccionario.values()) #muestra solo los valores

usuarios=[
    {"nombre":"Juan","edad":30,"ciudad":"california"},
    {"nombre":"Pedro","edad":20,"ciudad":"Las vegas"},
    {"nombre":"Manuel","edad":35,"ciudad":"california"},
    {"nombre":"Gustavo","edad":22,"ciudad":"california"},
    {"nombre":"Percy","edad":19,"ciudad":"Miami"},
    {"nombre":"Andrea","edad":31,"ciudad":"california"}
]
size=len(usuarios)
# print(f"La cantidad de registros de mi lista es {size}")
# print(usuarios[4]["nombre"])
def buscar_usuario_nombre(nom):
    try:
        #nombre_bus=input("Ingrese el nombre a buscar ")
        for data in usuarios:
            if nom in data["nombre"]:
                print(f"Usuario encontrado {data}")
                break
        else:
            print("Usuario no ubicado")
    except Exception as err:
        print("Ocurrio un error consulte la web en 24 hr")

buscar_usuario_nombre("Juan")