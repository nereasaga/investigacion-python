# Comparaciones básicas
igual_que = 5 == 6  # False, porque 5 no es igual a 6
distinto_de = 5 != 6  # True, porque 5 es diferente de 6
mayor_que = 5 > 6  # False, porque 5 no es mayor que 6
menor_que = 5 < 6  # True, porque 5 es menor que 6
mayor_o_igual = 5 >= 6  # False, porque 5 no es mayor ni igual que 6
menor_o_igual = 5 <= 6  # True, porque 5 es menor o igual que 6

# Imprimir resultados de las comparaciones básicas
print("5 == 6:", igual_que)
print("5 != 6:", distinto_de)
print("5 > 6:", mayor_que)
print("5 < 6:", menor_que)
print("5 >= 6:", mayor_o_igual)
print("5 <= 6:", menor_o_igual)

# Otra forma de comparación con diferentes variables
n1 = 10
n2 = 15

print("n1 > n2:", n1 > n2)  # False, porque 10 no es mayor que 15
print("n1 < n2:", n1 < n2)  # True, porque 10 es menor que 15
print("n1 <= 10:", n1 <= 10)  # True, porque n1 es igual a 10
print("n1 >= 10:", n1 >= 10)  # True, porque n1 es igual a 10
print("n2 == 15:", n2 == 15)  # True, porque n2 es igual a 15

# Comparación con cálculos combinados
a = 5
b = 10
c = 20

comparacion = a + b < c  # Compara si 5 + 10 es menor que 20
print("a + b < c:", comparacion)  # True, porque 15 < 20

# Comparar contraseñas
contraseña_almacenada = "peñascal"
contraseña_escrita = "penascal"  # Contraseña escrita incorrecta

# Comparar las contraseñas (sin tener en cuenta el caso)
print("Contraseñas iguales:", contraseña_almacenada == contraseña_escrita)  # False

# Comparación con cadenas
texto1 = "Python"
texto2 = "python"

# Comparar cadenas de texto (case-sensitive)
print("texto1 == texto2:", texto1 == texto2)  # False, porque 'P' y 'p' son diferentes

# Convertir ambas cadenas a minúsculas antes de comparar
print("texto1.lower() == texto2.lower():", texto1.lower() == texto2.lower())  # True, porque convierte todo a minúsculas

# Comparación con listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]  # Lista con el mismo contenido que lista1
lista3 = lista1  # Lista3 es una referencia a lista1

# Comparar listas (contenido)
print("lista1 == lista2:", lista1 == lista2)  # True, porque el contenido es igual

# Comparar listas (ubicación en memoria)
print("lista1 is lista2:", lista1 is lista2)  # False, porque son listas diferentes en memoria
print("lista1 is lista3:", lista1 is lista3)  # True, porque lista3 es la misma referencia que lista1
