#AGREGAR ELEMENTOS A COLECCIONES

# Agregar elementos:
## para  añadir elementos hay que usar las funciones append(), insert() o extend()
mi_lista = [1, 2, 3]
mi_lista.append(4) # Agrega 4 al final de la lista
print(mi_lista) # Output: [1, 2, 3, 4]
 
mi_lista.insert(1, 10) # Inserta 10 en el índice 1
print(mi_lista) # Output: [1, 10, 2, 3, 4]
 
mi_lista.extend([5, 6, 7]) #agrega varios elementos al final de la lista
print(mi_lista) #output: [1, 10, 2, 3, 4, 5, 6, 7]


### tupla
#LAS TUPLAS NO SE PUEDEN MODIFICAR ,
# Si es posible añadir elementos usando +
mi_tupla = (1, 2, 3)
nueva_tupla = mi_tupla + (4, 5)
print(nueva_tupla) # Output: (1, 2, 3, 4, 5)


### set
## para  añadir elementos hay que usar las funciones add() o update()
mi_set = {1, 2, 3}
mi_set.add(4) # Agrega 4 al conjunto
print(mi_set) # Output: {1, 2, 3, 4}


mi_set.update([4,5,6]) #agrega múltiples valores al set.
print(mi_set) #output: {1, 2, 3, 4, 5, 6}


### diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30}
mi_diccionario["ciudad"] = "Madrid" # Agrega el par clave-valor "ciudad": "Madrid"
print(mi_diccionario) # Output: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}