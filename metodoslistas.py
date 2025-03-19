# MÉTODOS EN LISTAS

lista = [1, 2, 3, 4, 2, 2]

# count(x)	Cuenta cuántas veces aparece x en la lista
print(lista.count(2))  # 3

# len(lista)	Retorna la cantidad de elementos en la lista
print(len(lista))  # 6

# append(x)	Agrega x al final de la lista
lista.append(5)
print(lista)  # [1, 2, 3, 4, 2, 2, 5]

# remove(x)	Elimina la primera aparición de x
lista.remove(2)
print(lista)  # [1, 3, 4, 2, 2, 5]

# sort()	Ordena los elementos de menor a mayor
lista.sort()
print(lista)  # [1, 2, 2, 2, 3, 4, 5]

# reverse()	Invierte el orden de la lista
lista.reverse()
print(lista)  # [5, 4, 3, 2, 2, 2, 1]
