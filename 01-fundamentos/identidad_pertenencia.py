# Operadores de Identidad
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

print(lista1 is lista2)  # True (lista1 y lista2 apuntan al mismo objeto)
print(lista1 is lista3)  # False (lista1 y lista3 son objetos diferentes aunque tienen los mismos valores)

# Operadores de Pertenencia
frutas = ["manzana", "naranja", "uva"]

# Comprobamos si 'manzana' está en la lista
print("manzana" in frutas)  # True

# Comprobamos si 'pera' no está en la lista
print("pera" not in frutas)  # True
