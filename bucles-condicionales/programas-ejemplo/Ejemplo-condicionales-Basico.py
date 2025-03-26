def mostrar_condicionales():
    print("🌟 ¡Bienvenido a la App de Condicionales! 🌟")
    print("Responde las preguntas y observa cómo funcionan los condicionales.\n")
    
    # Pregunta 1: if-else básico
    print("Pregunta 1: ¿Eres mayor de edad?")
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("✅ Eres mayor de edad. ¡Tienes libertad!\n")
    else:
        print("❌ Eres menor de edad. ¡Respeta la ley!\n")
    
    # Pregunta 2: elif para múltiples condiciones
    print("Pregunta 2: ¿Qué nota sacaste?")
    nota = int(input("Ingresa tu nota (0-100): "))
    if nota >= 90:
        print("🥇 ¡Excelente! Eres un genio.")
    elif 75 <= nota < 90:
        print("🥈 ¡Muy bien! Sigue así.")
    elif 60 <= nota < 75:
        print("🥉 ¡Bien! Puedes mejorar.")
    else:
        print("❌ Necesitas estudiar más.\n")
    
    # Pregunta 3: Operador ternario
    print("Pregunta 3: ¿Te gusta Python?")
    respuesta = input("(si/no): ").lower()
    mensaje = "¡Python te ama! 🐍" if respuesta == "si" else "¿Por qué? 😢"
    print(mensaje + "\n")
    
    # Pregunta 4: match-case (Python 3.10+)
    print("Pregunta 4: ¿Qué acción quieres realizar?")
    print("1. Saludar\n2. Despedirte\n3. Salir")
    opcion = input("Elige (1/2/3): ")
    match opcion:
        case "1":
            print("Hola, ¿cómo estás? 😊")
        case "2":
            print("¡Hasta luego! 🖖")
        case "3":
            print("Saliendo... 🚪")
        case _:
            print("Opción inválida. ❌\n")
    
    # Pregunta 5: Operadores lógicos (and/or/not)
    print("Pregunta 5: ¿Eres estudiante y tienes menos de 25 años?")
    es_estudiante = input("¿Eres estudiante? (si/no): ").lower() == "si"
    edad = int(input("Ingresa tu edad: "))
    if es_estudiante and edad < 25:
        print("✅ ¡Tienes descuento juvenil!")
    elif es_estudiante or edad < 25:
        print("📌 Solo cumples una condición.")
    else:
        print("❌ No aplicas a ningún beneficio.\n")
    
    # Pregunta 6: Verificación de membresía (in)
    print("Pregunta 6: ¿Qué fruta prefieres?")
    fruta = input("Elige entre manzana, plátano o uva: ").lower()
    frutas_validas = ["manzana", "plátano", "uva"]
    if fruta in frutas_validas:
        print(f"🍎 ¡{fruta.capitalize()} es una excelente elección!")
    else:
        print("❌ Fruta no disponible.\n")
    
    # Pregunta 7: Truthy/falsy
    print("Pregunta 7: ¿Tienes hermanos?")
    respuesta = input("(Escribe algo o deja vacío): ").strip()
    if respuesta:  # Si no está vacío → Truthy
        print("✅ ¡Tienes hermanos!")
    else:
        print("❌ No tienes hermanos o no respondiste.\n")
    
    print("¡Gracias por participar! 🎉")

# --- Ejecutar la app ---
if __name__ == "__main__":
    mostrar_condicionales()