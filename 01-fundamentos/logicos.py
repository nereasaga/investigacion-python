# Operador lógico AND (y) - devuelve True solo si ambos operandos son verdaderos
Resultado = True & True  # True, ambos son verdaderos
Resultado2 = False & True  # False, uno es falso
Resultado3 = True & False  # False, uno es falso
Resultado4 = False & False  # False, ambos son falsos

# Operador lógico OR (o) - devuelve True si al menos uno de los operandos es verdadero
Resultado5 = True | True  # True, al menos uno es verdadero
Resultado6 = False | True  # True, uno es verdadero
Resultado7 = True | False  # True, uno es verdadero
Resultado8 = False | False  # False, ninguno es verdadero

# Operador lógico NOT (no) - invierte el valor lógico del operando
Resultado9 = not True  # False, invierte True a False
Resultado10 = not False  # True, invierte False a True

# Ejemplo con condiciones numéricas
Resultado11 = not 2 > 49  # True, porque 2 no es mayor que 49, el not lo invierte
print("Resultado11:", Resultado11)  # Imprime True

# Ejemplo con edad
edad = 20

# AND: Verifica si la edad está entre 18 y 30 años
print(edad > 18 and edad < 30)  # True, porque 20 está en el rango 18 < 20 < 30

# OR: Verifica si la edad es mayor que 18 o menor que 30
print(edad > 18 or edad < 30)  # True, porque 20 es mayor que 18

# NOT: Verifica si la edad no es mayor que 17 (es decir, es mayor o igual a 18)
print(not (edad > 17))  # False, porque 20 es mayor que 17, el not lo invierte

# Ejemplo de acceso de usuario
usuario = "admin"
clave = "1234"

# Combinación de AND: Verifica si el usuario es 'admin' y la clave es '1234'
acceso = usuario == "admin" and clave == "1234"
print("Acceso permitido:", acceso)  # True, porque ambas condiciones son verdaderas

# Ejemplo de operadores lógicos combinados con otras condiciones
edad = 25
tiene_permiso = True

# Combinación de AND: Verifica si la edad es mayor o igual a 18 y tiene permiso
puede_conducir = edad >= 18 and tiene_permiso
print("Puede conducir:", puede_conducir)  # True, porque ambas condiciones son verdaderas

# Ejemplo adicional con operador OR
es_licenciado = False
tiene_experiencia = True

# Combinación de OR: Verifica si tiene licencia o experiencia
puede_trabajar = es_licenciado or tiene_experiencia
print("Puede trabajar:", puede_trabajar)  # True, porque tiene experiencia, aunque no tiene licencia
