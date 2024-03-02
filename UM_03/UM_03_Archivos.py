"""
Aperturar el archivo en CSV
Y Trabajar solo con los precios mayores o iguales a 140

import csv
#Abrir el archivo i guardarlo en el buffer de memoria "file"  "r" es para solo lectura
con=0
listavalores=list()
with open("./UM_03/Archivos/productos_Marzo2024.csv", "r") as file:
    reader=csv.reader(file)
    for row in reader:
        if con>=1:
            if int(row[2])>=140:
                print(f"{con} {row}")
                listavalores.append([row[0],row[1],row[2]])
        con+=1

for indixe, valor in enumerate(listavalores):
    print(f"{indixe} {valor}")

"""
import csv
def generar_archivo():
    try:
        data_to_write=[["Codigo", "Producto","Stock"],
                       ["A100","XYZ",200],
                       ["A200","MNO",300],
                       ["A400","LXO",210],
                       ]
        with open("./UM_03/Archivos/Archivo_Generate_Marzo03.csv","w",newline="") as file:
            writer=csv.writer(file)
            writer.writerows(data_to_write)
    except Exception as err:
        print(f"Error del archivo {err}")
    else:
        print("Se genero el archivo correctamente")
    finally:
        file.close()
generar_archivo()

