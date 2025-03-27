#MODIFICAR ELEMENTOS DE COLECCIONES

### lista
mi_lista = [1, 2, 3, 4, 5]
mi_lista[2] = 10 # Cambia el tercer elemento (índice 2) a 10
print(mi_lista) # Output: [1, 2, 10, 4, 5]

# intervalos
mi_lista[1:3] = [20, 30] #cambia los valores desde el indice 1 al 3 (no incluido)
print(mi_lista) #output: [1, 20, 30, 4, 5]


### tupla
#LAS TUPLAS NO SE PUEDEN MODIFICAR ,
# cualquiera de estas sentencias enviará un error
# mi_tupla[0] = 10
# mi_tupla.append(4)
# del mi_tupla[0]


### set
#Los sets en Python no permiten la modificación directa de elementos individuales. 
# Si necesitas "modificar" un elemento, debes eliminar el elemento antiguo y agregar el nuevo, 
# para ello podemos usar los métodos remove() y add()
mi_set = {1, 2, 3}
mi_set.remove(2) #elimina el elemento a cambiar

mi_set.add(20) #agrega el nuevo valor.
print(mi_set) #{1, 3, 20}


### diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30}
mi_diccionario["edad"] = 35 # Cambia el valor de la clave "edad" a 35
print(mi_diccionario) # Output: {'nombre': 'Juan', 'edad': 35}
