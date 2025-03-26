# --- Base de datos simulada ---
usuarios_registrados = {
    "ana": {"contraseña": "1234", "rol": "editor"},
    "admin": {"contraseña": "admin123", "rol": "admin"},
    "invitado": {"contraseña": "guest", "rol": "invitado"}
}

permisos_por_rol = {
    "admin": ["editar", "leer", "eliminar"],
    "editor": ["editar", "leer"],
    "invitado": ["leer"]
}

ips_permitidas = ["192.168.1.50", "192.168.1.100", "10.0.0.1"]
sistema_activado = True  # Sistema siempre activo (podría ser dinámico)

# --- Función principal ---
def sistema_autenticacion():
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        # 1. Ingreso de usuario y contraseña
        usuario = input("Ingrese su usuario: ").strip()
        contraseña = input("Ingrese su contraseña (visible en pantalla): ").strip()  # Usamos input normal

        # 2. Verificar credenciales
        if usuario in usuarios_registrados and usuarios_registrados[usuario]["contraseña"] == contraseña:
            print("\n✅ ¡Autenticación exitosa!")
            datos_usuario = usuarios_registrados[usuario]
            rol = datos_usuario["rol"]
            permisos = permisos_por_rol[rol]
            
            # 3. Verificar rol
            print(f"\n👤 Rol: {rol}")
            if rol == "admin":
                print("  ✅ Permisos: Todos (editar, leer, eliminar)")
            elif rol == "editor":
                print("  ✅ Permisos: editar, leer")
            else:
                print("  ✅ Permisos: solo lectura")
            
            # 4. Ingreso de IP
            ip_usuario = input("\nIngrese su IP: ").strip()
            if ip_usuario in ips_permitidas:
                print(f"  🌐 IP {ip_usuario} permitida.")
            else:
                print(f"  🚫 IP {ip_usuario} bloqueada. Contacte al administrador.")
                return  # Termina si la IP no es válida
            
            # 5. Selección de acción
            print("\nAcciones disponibles:")
            print("  1. Editar documento")
            print("  2. Eliminar usuario")
            print("  3. Ver informe")
            opcion = input("Seleccione una acción (1/2/3): ").strip()
            
            # Mapear opción a acción
            accion = ""
            if opcion == "1":
                accion = "editar_documento"
            elif opcion == "2":
                accion = "eliminar_usuario"
            elif opcion == "3":
                accion = "ver_informe"
            else:
                print("❌ Opción inválida.")
                return
            
            # 6. Coincidencia de patrones (match-case)
            print("\nResultado:")
            match accion:
                case "editar_documento" if "editar" in permisos:
                    print("  📝 Acción: editar documento permitida.")
                case "eliminar_usuario" if rol == "admin":
                    print("  🗑️ Acción: eliminar usuario permitida.")
                case "ver_informe" if "leer" in permisos:
                    print("  📊 Acción: ver informe permitida.")
                case _:
                    print("  ❌ Acción no autorizada.")
            
            # 7. Verificar estado del sistema
            if not sistema_activado:
                print("  ⚠️ Sistema en mantenimiento.")
            else:
                print("  🚀 Sistema operativo.")
            
            return  # Salir tras autenticación exitosa
        
        else:
            intentos += 1
            print(f"\n❌ Error: Credenciales incorrectas (intentos restantes: {max_intentos - intentos}).\n")
    
    print("❗ Máximo de intentos excedido. Bloqueando acceso...")

# --- Ejecutar el sistema ---
if __name__ == "__main__":
    sistema_autenticacion()