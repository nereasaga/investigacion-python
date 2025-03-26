# Usando format()
nombre = "Ana"
edad = 25
mensaje1 = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje1)

# Usando f-strings (recomendado desde Python 3.6)
mensaje2 = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje2)

# Formatear números
pi = 3.141592653589793
print(f"Valor de pi con 2 decimales: {pi:.2f}")  # 3.14
print(f"Valor de pi con 4 decimales: {pi:.4f}")  # 3.1416

# Formatear con alineaciones
print(f"|{'Centro':^10}|")  # Centrado
print(f"|{'Izquierda':<10}|")  # Alineado a la izquierda
print(f"|{'Derecha':>10}|")  # Alineado a la derecha
