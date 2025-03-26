def menu():
    while True:
        print("\n🌟 Menú de Bucles en Python 🌟")
        print("1. Bucle For")
        print("2. Bucle While")
        print("3. Bucles Anidados")
        print("4. Control de Bucles (break/continue)")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("❌ Ingrese un número válido.")
            continue
        
        if opcion == 1:
            ejemplo_for()
        elif opcion == 2:
            ejemplo_while()
        elif opcion == 3:
            ejemplo_anidados()
        elif opcion == 4:
            ejemplo_control()
        elif opcion == 5:
            print("¡Gracias por usar la app! 😊")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

def ejemplo_for():
    print("\n--- Ejemplo de Bucle For ---")
    print("Imprimiendo números del 1 al 5:")
    for i in range(1, 6):
        print(f"Número: {i}")
    print("¡Fin del bucle!")

def ejemplo_while():
    print("\n--- Ejemplo de Bucle While ---")
    print("Contador descendente desde 5 hasta 1:")
    contador = 5
    while contador >= 1:
        print(f"Contador: {contador}")
        contador -= 1
    print("¡Tiempo terminado!")

def ejemplo_anidados():
    print("\n--- Ejemplo de Bucles Anidados ---")
    print("Tabla de multiplicar del 3:")
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i} x {j} = {i*j}")
        print("------")

def ejemplo_control():
    print("\n--- Ejemplo de Control de Bucles ---")
    print("Uso de 'break' y 'continue':")
    print("Números del 1 al 10, saltando el 5 y deteniéndose en 8:")
    for num in range(1, 11):
        if num == 5:
            print(f"  Saltando número {num}")
            continue
        elif num == 8:
            print(f"  Deteniendo en número {num}")
            break
        print(f"  Número: {num}")

# --- Ejecutar la app ---
if __name__ == "__main__":
    menu()