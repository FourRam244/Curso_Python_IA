#import datetime as now
from datetime import datetime, timedelta
fecha_actual=datetime.now()
# print(f"La fecha del sistema es {fecha_actual}")
# print(type(fecha_actual))
# print(f"El Año {fecha_actual.year}")
# print(f"El Mes {fecha_actual.month}")
# print(f"El Dia {fecha_actual.day}")
# print(f"La hora {fecha_actual.hour}")
# print(f"Los minutos {fecha_actual.minute}")
# print(f"Los segundos {fecha_actual.second}")

"""
Operaciones entre fechas
"""

# nueva_fecha=fecha_actual+timedelta(days=7)
# print(f"La nueva fecha es {nueva_fecha}")

#Conversion de Fechas
cadena_fechas="2023-08-25"
#strptime convierte de String a fecha

fecha_desde_cadena=datetime.strptime(cadena_fechas,"%Y-%m-%d")
#print(type(fecha_desde_cadena))
print(f"La fecha actual es {fecha_desde_cadena}")

#strftime para formatear un objeto datetime como una cadena de texto 
fecha_dt=datetime(2022,3,1,12,30,0)
fechas_str=fecha_dt.strftime("%Y-%m-%d %H:%M:%S")
print(fechas_str)
print(type(fechas_str))


"""
Calcular los dias que existen entre dos fechas
"""
fecha1=datetime(2022,5,10)
fecha2=datetime(2022,3,15)
diferncia_entre_fechas=fecha1-fecha2
print(f"Diferencia entre dias {diferncia_entre_fechas.days}")
diferncia_entre_años=diferncia_entre_fechas.days//365
diferncia_entre_meses=(diferncia_entre_fechas.days)%365//30
print(f"Diferencia entre año {diferncia_entre_años}")
print(f"Diferencia entre meses {diferncia_entre_meses}")


#creando nuestra propia funcion
fecha_actual=datetime.now()
numero_mes=fecha_actual.month
#print(numero_mes)
def nombre_mes(numero):
    match numero:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"    
        case 3:
            return "Marzo"
        case _:
            return "Opcion invalida"    
print(nombre_mes(numero_mes))

#usando el modulo calendar te lo devuelve en ingles
import calendar
numero=mes=3
nombre_mes=calendar.month_name[numero_mes]
print(f"El nombre del mes es {nombre_mes}")
#usando el modulo calendar te lo devuelve en español
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'es_MX')
nombre_mes = calendar.month_name[numero_mes]
print(f"nombre del mes con calendar: {nombre_mes}")