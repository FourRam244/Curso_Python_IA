"""
assert .- Es una palabra clave reservada para realizar afirmaciones
o comprobaciones 
de condiciones

Sintaxis:
assert expresion, mensaje_de_error

"""
try:
    edad=int(input("Ingrese la edad "))
    assert edad>=0, "Error: La edad no puede ser negativa"
    print(f"edad ingresada es correcta {edad}")
except (ValueError,AssertionError) as err:
    print(f"Error producido {err}")


# import keyword #Modulo
# print(keyword.kwlist) Lista de palabras reservadas