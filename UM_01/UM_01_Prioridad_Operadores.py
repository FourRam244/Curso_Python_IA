"""
Parentesis:
()

Exponente:
**

Negacion unaria:
-x ,+x

Multiplicacion, Division, Modulo
*./,%

Suma,Resta
+,-

Concatenacion de cadenas:
+

#resultado_1= 2 + 3 * 4
#print(resultado_1) #14

resultado_1= (2 + 3) * 4
print(resultado_1) #20

resultado_3=2+4*4**2-(8//2)
print(resultado_3)

"""
""""
Prioridad operadores logicos
1.-not
2.-and
3.-or


a=True
b=False
c=True
resultado0=a or b and not c
#resultado=True or False and False
print(resultado0) #True

Explicación:

a = True
b = False
c = True

resultado = a or b and not c

1. Se ejecuta not c

resultado = a or b and False

2. Se ejecuta b and False

resultado = a or False

3. Se ejecuta a or False

resultado = True
"""



