# FUNCIONES EN PYTHON

# Definición de una función simple
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Jon"))  # Hola, Jon!

# FUNCIONES CON ARGUMENTOS POR DEFECTO
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))    # 9 
print(potencia(3, 3)) # 27

# FUNCIONES LAMBDA (ANÓNIMAS)
doble = lambda x: x * 2
print(doble(4))  # 8

# map(): Aplica una función a cada elemento de una lista
numeros = [1, 2, 3]
print(list(map(lambda x: x**2, numeros)))  # [1, 4, 9]

# filter(): Filtra elementos de una lista
numeros = [1, 2, 3]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2]

# reduce(): Reduce la lista a un solo valor
from functools import reduce
numeros = [1, 2, 3]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # 6

# enumerate(): Obtiene índices y valores de una lista
for i, valor in enumerate(["a", "b", "c"]):
    print(i, valor)  # (0, 'a'), (1, 'b'), (2, 'c')

# zip(): Une listas en tuplas
nombres = ["Ane", "Jon"]
edades = [25, 30]
print(list(zip(nombres, edades)))  # [('Ane', 25), ('Jon', 30)]

# *args: Varios argumentos como tupla
def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3, 4))  # 10

# **kwargs: Argumentos nombrados como diccionario
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ane", edad=30)  
# nombre: Ane
# edad: 25

# return: Retorno de valores en funciones
def cuadrado(n):
    return n**2

resultado = cuadrado(4)
print(resultado)  # 16
print(cuadrado(4))

# Funciones con un parametro por defecto
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}!")

# Llamadas a la función
saludar("Ane")             # Usa el valor por defecto de "mensaje"
saludar("Jon", "Hello") # Sobrescribe el valor por defecto


# Funciones con parámetros con valores por defecto
def crear_usuario(nombre="Invitado", edad=18, pais="España"):
    print(f"Nombre: {nombre}, Edad: {edad}, País: {pais}")

# Llamadas a la función
crear_usuario()                           # Usa todos los valores por defecto
crear_usuario("Lucía")                    # Cambia solo el nombre
crear_usuario("Mikel", 25)               # Cambia nombre y edad
crear_usuario("Elena", 30, "México")      # Cambia todos los valores