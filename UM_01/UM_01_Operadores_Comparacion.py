"""
Operadores de comparacion:
Igualdad: ==
Desigualda: !=
Mayorque: > 
Menorque: <=

Mayor o igual que: >=
Menor o igual que: <=

and: Devuleve True si ambas expresiones son verdaderas
or: Devuelve True si al menos una de las expresiones es verdadera
not: Niega la expresion booleana; devulve false si la expresion es verdadera y viceversa (Negacion Unitaria)
"""

edad=18
licencia_conducir=True
manejar= not edad>=18 and licencia_conducir==True
print(manejar)