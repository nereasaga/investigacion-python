#ACCESO A DATOS DE ELEMENTOS DE COLECCIONES

### lista
## para  eliminar elementos hay que usar las funciones remove(), pop(), del o clear()
mi_lista = [1, 2, 3, 4, 5]
mi_lista.remove(3) # Elimina la primera aparición de 3
print(mi_lista) # Output: [1, 2, 4, 5]

elemento_eliminado = mi_lista.pop(1) # Elimina y devuelve el elemento en el índice 1
print(mi_lista) # Output: [1, 4, 5]
print(elemento_eliminado) #output: 2

del mi_lista[0] #elimina el elemento en el índice 0
print(mi_lista) #output: [4, 5]

mi_lista.clear() #Elimina todos los elementos de la lista
print(mi_lista) #output: []

### tupla
#LAS TUPLAS NO SE PUEDEN MODIFICAR ,
# no permite eliminar elementos


### set
# discard() , remove() o clear()
#para  eliminar elementos hay que usar las funciones remove(), discard(), pop() o clear()
mi_set = {1, 2, 3, 4, 5}
mi_set.remove(3) # Elimina 3 del conjunto (genera error si no existe)
print(mi_set) # Output: {1, 2, 4, 5}


mi_set.discard(5) # Elimina 5 del conjunto (no genera error si no existe)
print(mi_set) #output: {1, 2, 4}


elemento_eliminado = mi_set.pop() #elimina un elemento aleatorio del set y lo retorna.
print(mi_set)
print(elemento_eliminado)


mi_set.clear() #elimina todos los elementos del set.
print(mi_set) #output: set() 


### diccionario
## para  eliminar elementos hay que usar las funciones pop(), del o clear()
#Eliminar pares clave-valor
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
valor_eliminado = mi_diccionario.pop("edad") # Elimina y devuelve el valor asociado a la clave "edad"
print(mi_diccionario) # Output: {'nombre': 'Juan', 'ciudad': 'Madrid'}
print(valor_eliminado) #Output: 30


del mi_diccionario["nombre"] #elimina el par clave valor relacionado con la llave "nombre"
print(mi_diccionario) #output: {'ciudad': 'Madrid'}


mi_diccionario.clear() #elimina todos los pares clave valor del diccionario
print(mi_diccionario) #output: {}
