# MÉTODOS EN LISTAS

lista = [1, 2, 3, 4, 2, 2]

# index(x)	Devuelve el índice de la primera aparición de x
print(lista.index(2))  # 1

# count(x)	Cuenta cuántas veces aparece x en la lista
print(lista.count(2))  # 3

# len(lista)	Retorna la cantidad de elementos en la lista
print(len(lista))  # 6

# append(x)	Agrega x al final de la lista
lista.append(5)
print(lista)  # [1, 2, 3, 4, 2, 2, 5]

# insert(i, x)	Inserta x en la posición i
lista.insert(1, 2)
print(lista)  # [1, 2, 2, 3, 4, 2, 2, 5]

# remove(x)	Elimina la primera aparición de x
lista.remove(2)
print(lista)  # [1, 2, 3, 4, 2, 2, 5]

# sort()	Ordena los elementos de menor a mayor
lista.sort()
print(lista)  # [1, 2, 2, 2, 3, 4, 5]


# reverse()	Invierte el orden de la lista
lista.reverse()
print(lista)  # [5, 4, 3, 2, 2, 2, 1]

print(lista[::-1])  # [1, 2, 2, 2, 3, 4, 5] (porque se ha invertido 2 veces)

# slice(start, stop, step)	Extrae un rango de la lista

# Crear un objeto slice(start, stop, step)
s = slice(1, 5, 2)
print(lista[s])  # [4, 2]


lista2 = [10, 20, 30, 40, 50, 60]

print(lista2[1:5:2])  # [20, 40] (Equivalente al ejemplo anterior)
print(lista2[:3])     # [10, 20, 30] (Desde el inicio hasta índice 3)
print(lista2[2:])     # [30, 40, 50, 60] (Desde el índice 2 hasta el final)
print(lista2[::-1])   # [60, 50, 40, 30, 20, 10] (Lista invertida)

# slice con strings

texto = "Estoy usando Python"

print(texto[0:6])   # 'Estoy ' (Primeros 6 caracteres)
print(texto[-6:])   # 'Python' (Últimos 6 caracteres)
print(texto[::-1])  # 'nohtyP gnisua yotsE' (Invertir el texto)
