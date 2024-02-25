"""
Listas
Las listas son Mutables 
Estructura mutable: Puede ser 
modificable en su contenido, es decir, se pueden agregar, editar(sustituir) 
o eliminar elementos.
"""
#formas para inicializar listas
participantes_curso=[] 
participantes_curso=list() #Constructor
participantes_curso=["Juan","Pedro","Maria","Rosa","Armando"]
participantes_curso.append("Carlos")#Añade elemento al final de la lista
participantes_curso.insert(1,"Gloria")#Añade un elemento en la posicion indicada
#print(participantes_curso[0]) #Mostrar un elemento de la por su indice 
participantes_curso[0]="Arturo" #remplazar por indice

participantes_curso.pop(0) 
participantes_curso.remove("Armando")

size=len(participantes_curso) #cantidad de elementos de la lista

#participantes_curso.sort()#ordena de manera ascendente
participantes_curso.sort(reverse=True)#ordena de manera descendente
#print(f"La cantidad de elementos de la lista es {size}")

print(participantes_curso)

"""
Tuplas
Las Tuplas son inmutables
"""
# valores=(12,34,56)
# #valores[0]=200
# informacion_persona=("Juan",25,"Masculino")

# """
# """
# #participantes_curso=["Juan","Pedro","Maria","Rosa","Armando"]
# informacion_persona=("Juan",25,"Masculino") #tupla
# datos_persona=list(informacion_persona) #cast list ---- tuple
# datos_persona.append("DF 2034") #añadi el nuevo elemento
# informacion_persona=tuple(datos_persona) #cast---- tuple
# print(informacion_persona)
