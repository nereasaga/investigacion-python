# 1. Sentencia if básica 

edad = 18
if edad >= 18:
    print("Eres mayor de edad.")

# ----------------------------------------- #

# 2. if-else 

temperatura = 30
if temperatura > 25:
    print("Hace calor.")
else:
    print("Hace frío.")

# ----------------------------------------- #

# 3. if-elif-else

nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("Reprobado")

# ----------------------------------------- #

# 4. Operador ternario 

mensaje = "Aprobado" if nota >= 60 else "Reprobado"

# ----------------------------------------- #

# 5. match-case (Patrón estructural, Python 3.10+) 

color = "rojo"
match color:
    case "rojo":
        print("Color rojo")
    case "azul":
        print("Color azul")
    case _:
        print("Otro color")

# ----------------------------------------- #

# 6. Condiciones compuestas con operadores lógicos ( and / or /not )

    # AND

edad = 20
dinero = 50
if edad >= 18 and dinero >= 30:
    print("Puedes comprar la entrada.")

    # OR

temperatura = 35

if temperatura < 10 or temperatura > 30:
    print("La temperatura está fuera del rango óptimo.")
else:
    print("Temperatura adecuada.")

    # NOT

usuarios_conectados = []

if not usuarios_conectados:
    print("No hay usuarios conectados.")
else:
    print(f"Hay {len(usuarios_conectados)} usuarios.")

# ----------------------------------------- #

# 7. Valores "truthy" y "falsy" 

lista = []
if not lista:  # Equivale a: if lista == []
    print("La lista está vacía.")


# ----------------------------------------- #

# 8. Comprobación de elementos

letra = "a"
if letra in "hola":
    print("La letra 'a' está en 'hola'.")

# ----------------------------------------- #

# 9. elif con múltiples condiciones

puntuacion = 85
if puntuacion >= 90:
    print("Excelente")
elif 80 <= puntuacion < 90:
    print("Muy bien")
elif 70 <= puntuacion < 80:
    print("Bien")
else:
    print("Mejorable")

# ----------------------------------------- #

