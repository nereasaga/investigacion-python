import random

def adivinanza_numeros():
    print("🎮 ¡Bienvenido al Juego de Adivinanza! 🎮")
    print("Tienes que adivinar un número entre 1 y 50.")
    print("¡Solo tienes 7 intentos!\n")
    
    numero_secreto = random.randint(1, 50)
    intentos = 0
    acertado = False
    historial_intentos = []

    while intentos < 7 and not acertado:
        # Bucle para validar entrada numérica
        while True:
            try:
                guess = int(input(f"Intento {intentos + 1}: Ingresa un número (1-50): "))
                if 1 <= guess <= 50:
                    break
                else:
                    print("❌ El número debe estar entre 1 y 50.")
            except ValueError:
                print("❌ Ingresa un número entero válido.")
        
        historial_intentos.append(guess)
        intentos += 1
        
        # Lógica de adivinanza
        if guess == numero_secreto:
            acertado = True
            print(f"\n🎉 ¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        elif guess < numero_secreto:
            print("⬆️ ¡El número es más alto!")
        else:
            print("⬇️ ¡El número es más bajo!")
        
        # Pista después de 3 intentos fallidos
        if intentos == 3 and not acertado:
            print(f"\n💡 Pista: El número termina con {numero_secreto % 10}.")
    
    # Mostrar resultados finales
    if not acertado:
        print(f"\n❌ ¡Se acabaron los intentos! El número era {numero_secreto}.")
    
    print("\n📊 Historial de intentos:")
    for i, num in enumerate(historial_intentos, 1):
        print(f"  Intento {i}: {num}")

# --- Ejecutar el juego ---
if __name__ == "__main__":
    adivinanza_numeros()