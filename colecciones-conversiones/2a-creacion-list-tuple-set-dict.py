#CREACIÖN DE COLECCIONES
# Uso de list, tuple, set, dict  en la creación

### list
mi_lista1= ['1', '2', '3', '4', '5']
mi_lista2 = list("12345") #debe ser un string , si 12345 (sin comillas) da error porque es un solo valor y no lo puede iterar.
mi_lista3 = list(str(12345))#str convierte el numero en string
print(mi_lista1) # Salida ['1', '2', '3', '4', '5']
print(mi_lista2) # Salida ['1', '2', '3', '4', '5']
print(mi_lista3) # Salida ['1', '2', '3', '4', '5']


### tuple
mi_tupla = (1, 2, 3, "hola", 5.0)
print(mi_tupla) # Output: (1, 2, 3, 'hola', 5.0)

mi_tupla2 = tuple([1, 2, 3])
print(mi_tupla2) # Output: (1, 2, 3)


### set
mi_set = {1, 2, 3, 4, 5}
print(mi_set) # Output: {1, 2, 3, 4, 5}
 
mi_set2 = set([1, 2, 3, 4, 5])
print(mi_set2) # Output: {1, 2, 3, 4, 5}

mi_set3 = set("hola")
print(mi_set3) # Output: {'h', 'o', 'l', 'a'}- El orden puede cambiar


### dict
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario) # Output: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

#  a-parejas clave=valor
mi_diccionario2 = dict(nombre="Juan", edad=30, ciudad="Madrid")
print(mi_diccionario2) # Output: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

#  b-lista de tuplas
mi_diccionario3 = dict([("nombre", "Juan"), ("edad", 30), ("ciudad", "Madrid")])
print(mi_diccionario3) # Output: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

#  c-Un iterable de objetos con dos elementos, donde cada elemento es iterable
iterable_de_claves_y_valores = [['nombre', 'Juan'], ['edad', 30], ['ciudad', 'Madrid']]
mi_diccionario4= dict(iterable_de_claves_y_valores)
print(mi_diccionario4) # Output: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
