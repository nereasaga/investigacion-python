# CONVERSIONES ENTRE COLECCIONES

lista = [1, 2, 3]
tupla = tuple(lista) #convierte lista a tupla
set_numeros = set(lista) #convierte lista a set
print(tupla)  # Salida: (1, 2, 3)
print(set_numeros) # Salida: {1, 2, 3}

tupla_pares = ((1, 2), (3, 4), ("a", "b"), ("Hola", 10))
mi_lista = list(tupla_pares) #convierte tupla a lista
print(mi_lista) # Salida: [(1, 2), (3, 4), ('a', 'b'), ('Hola', 10)]
