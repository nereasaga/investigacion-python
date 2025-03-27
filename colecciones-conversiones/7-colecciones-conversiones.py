# CONVERSIONES ENTRE COLECCIONES
# convertir lista a tupla y lista a set
lista = [1, 2, 3, 1]
tupla = tuple(lista) #convierte lista a tupla
set_numeros = set(lista) #convierte lista a set
print(tupla)  # Salida: (1, 2, 3, 1)
print(set_numeros) # Salida: {1, 2, 3}

# convertir tupla a lista
tupla_pares = ((1, 2), (3, 4), ("a", "b"), ("Hola", 10))
mi_lista = list(tupla_pares) #convierte tupla a lista
print(mi_lista) # Salida: [(1, 2), (3, 4), ('a', 'b'), ('Hola', 10)]

# convertir lista a diccionario
## convertir lista a diccionario
mi_lista2 =[("a",1),("b",2),("c",3)]
mi_diccionario1= dict(mi_lista2)
print(mi_diccionario1) 

## convertir 2 listas a 1 diccionario
# Uso de la función zip()

claves = ["mono", "cerdo", "tigre", "mapache","vaca","lobo"] 
valores = ["🐵","🐷","🐯","🦝","🐮","🐺"]

mi_diccionario2 = dict(zip(claves, valores))  
print(mi_diccionario2) # Salida: {'mono': '🐵', 'cerdo': '🐷', 'tigre': '🐯', 'mapache': '🦝', 'vaca': '🐮', 'lobo': '🐺'}