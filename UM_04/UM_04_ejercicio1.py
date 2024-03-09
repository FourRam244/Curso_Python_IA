"""
El objetivo de este proyecto es crear un programa en Python que simule un carrito de compras. El carrito debe permitir 
al usuario agregar productos, ver el contenido actual del carrito y realizar el pago. La información de los
productos estará almacenada en un archivo CSV.

Estructura del Archivo CSV:

1.-El archivo CSV contendrá información sobre los productos disponibles para comprar.
Cada fila del archivo representará un producto y contendrá al menos los siguientes campos: "ID", "Nombre", "Precio".
Puedes agregar más campos según sea necesario (por ejemplo, "Stock", "Descripción", etc.).
2.Funcionalidades del Carrito:
-Agregar Producto al Carrito: El programa debe permitir al usuario agregar productos al carrito indicando el
 ID del producto y la cantidad deseada.
-Ver Contenido del Carrito: El usuario puede ver el contenido actual del carrito, incluyendo los productos, 
cantidades y el total a pagar.
-Realizar Pago: Una vez que el usuario ha terminado de agregar productos al carrito, debe poder realizar el pago. 
Esto deberá mostrar el total a pagar y restar la cantidad de productos comprados del stock.

Requisitos Adicionales:
=========================
-Debes manejar situaciones donde el usuario intenta agregar una cantidad mayor que la disponible en el stock.
-El programa debe proporcionar retroalimentación adecuada al usuario en cada operación realizada.(usar excepciones)
"""
import csv

def Menu():
    try:
        carrito = []
        with open("./UM_04/Archivos/productos.csv", mode='r', newline='') as file:
            leer = csv.DictReader(file)
            productos = list(leer)

        while True:
            print("\n--- MENU ---")
            print("1.-Agregar Producto al Carrito")
            print("2.-Ver Contenido del Carrito")
            print("3.-Ver Todos los Productos")
            print("4.-Realizar Pago")
            print("5.-Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                id_producto = input("Ingrese el ID del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                agregar_producto(carrito, id_producto, cantidad, productos)
            elif opcion == '2':
                ver_contenido(carrito)
            elif opcion == '3':
                ver_productos(productos)
            elif opcion == '4':
                realizar_pago(carrito, productos)
            elif opcion == '5':
                print("Gracias por utilizar el carrito de compras.")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    except Exception as err:
        print(f"El error es: {err}")

def agregar_producto(carrito, id_producto, cantidad, productos):
    try:
        for producto in productos:
            if producto["ID"] == id_producto:
                stock_disponible = int(producto["Stock"])
                if cantidad > stock_disponible:
                    raise ValueError("La cantidad deseada supera el stock disponible.")
                
                producto_en_carrito = {
                    'ID': producto["ID"],
                    'Nombre': producto["Nombre"],
                    'Precio': float(producto["Precio"]),
                    'Cantidad': cantidad
                }
                carrito.append(producto_en_carrito)
                print(f"Producto '{producto['Nombre']}' agregado al carrito.")
                return
        raise ValueError("El ID del producto no existe.")
    except ValueError as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"Error inesperado: {err}")

def ver_contenido(carrito):
    try:
        if carrito:
            print("Contenido del carrito:")
            for producto in carrito:
                print(f"ID: {producto['ID']}, Nombre: {producto['Nombre']}, Cantidad: {producto['Cantidad']}")
            total = sum(producto['Precio'] * producto['Cantidad'] for producto in carrito)
            print(f"Total a pagar: {total}")
        else:
            print("El carrito está vacío.")
    except Exception as err:
        print(f"El error es: {err}")

def ver_productos(productos):
    try:
        print("Todos los productos disponibles:")
        for producto in productos:
            print(f"ID: {producto['ID']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")
    except Exception as err:
        print(f"El error es: {err}")

def realizar_pago(carrito, productos):
    if carrito:
        total = sum(producto["Precio"] * producto["Cantidad"] for producto in carrito)
        print(f"Total a pagar: {total}")
        confirmacion = input("¿Desea realizar el pago? (S/N): ")
        if confirmacion.upper() == 'S':
            try:
                with open("./UM_04/Archivos/productos.csv", mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=productos[0].keys())
                    writer.writeheader()
                    for producto in productos:
                        for producto_en_carrito in carrito:
                            if producto["ID"] == producto_en_carrito["ID"]:
                                producto["Stock"] = str(int(producto["Stock"]) - producto_en_carrito["Cantidad"])
                        writer.writerow(producto)
                print("Pago realizado. Gracias por su compra.")
                carrito.clear()
            except Exception as err:
                print(f"Error al actualizar el archivo CSV: {err}")
        else:
            print("Pago cancelado.")
    else:
        print("El carrito está vacío.")

Menu()
