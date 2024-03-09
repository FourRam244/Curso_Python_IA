"""
Operador ternario
-Es un operador condicional que toma tres operando y se utiliza
para evaluar una expresion booleana

Sintaxis
resultado_verdadero if condicion else resultado_falso
"""
edad=20
mensaje="Mayor de edad" if edad >= 18 else "Menor de edad"
#print(mensaje)

numero=8
resultado = "Numero es par "if numero %2==0 else "Numero impar"

#print(resultado)

#Ternario anidado
calificacion=60
resultado="Aprobo" if calificacion >= 70 else ("Recuperacion" if 60 <= calificacion < 70 else "Reprobado")

#en funcion
def es_par(numero):
    return True if numero %2==0 else False
#numero_evaluar=3
#print(es_par(numero_evaluar))


lista_numeros=[1,2,3,4,5]

resultado= "Hay numeros pares " if any(num %2 ==0 for num in lista_numeros) else "No hay numeros pares"
print(resultado)
