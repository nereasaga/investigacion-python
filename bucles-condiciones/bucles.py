# 1. for sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

# ----------------------------------------- #

# 2. for sobre una cadena de texto
palabra = "Python"
for letra in palabra:
    print(letra)

# ----------------------------------------- #

# 3. for sobre un diccionario
datos = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

    # Recorrer claves
for clave in datos:
    print(clave)

    # Recorrer valores
for valor in datos.values():
    print(valor)

    # Recorrer clave-valor
for clave, valor in datos.items():
    print(f"{clave}: {valor}")

# ----------------------------------------- #

# 4. for sobre una tupla
colores = ("rojo", "verde", "azul")
for color in colores:
    print(f"El color es {color}")

# ----------------------------------------- #

#5. for con range() (números secuenciales del 0 al 4)
for numero in range(5):
    print(f"secuencial {numero}")

    # Definiendo inicio y fin. Empieza en 2, termina en 5 (no incluye 6)

for numero in range(2, 5):
    print(numero)

    #  Definiendo paso. De 1 a 9 con saltos de 2 en 2

for numero in range(0, 10, 2):
    print(numero)

# ----------------------------------------- #

#6. for con enumerate()Para acceder al índice y al valor de una lista al mismo tiempo.
nombres = ["Ana", "Carlos", "Elena"]

for indice, nombre in enumerate(nombres):
    print(f"Índice {indice}: {nombre}")

# ----------------------------------------- #

# 7. for con zip() (recorrer varias listas a la vez)

nombres = ["Ana", "Carlos", "Elena"]
edades = [25, 30, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")

# 8. for dentro de otro for (bucles anidados)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ") # Aquí, el parámetro end=" " asegura que después de imprimir elemento, se añade un espacio en lugar de un salto de línea.  Por defecto, el valor de end es un salto de línea ("\n"),
    print()  # Salto de línea entre filas

# 9. for con break y continue
numeros = [1, 2, 3, 4, 5, 6]

for num in numeros:
    if num == 3:
        print("me salto el 3")
        continue  # Salta el número 3
    if num == 5:
        print("me paro en el 5 y no pinto el 6")
        break  # Detiene el bucle en el 5
    print(num)

# 10. for con List Comprehension (sintaxis compacta)
    
    # Cuadrados de los números del 0 al 4
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

    # Números pares entre 0 y 9
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

