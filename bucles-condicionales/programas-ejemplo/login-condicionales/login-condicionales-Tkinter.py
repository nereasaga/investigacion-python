import tkinter as tk
from tkinter import messagebox

# --- Variables del sistema ---
usuarios_registrados = {"ana": "1234"}
roles = ["admin", "editor", "invitado"]
permisos_por_rol = {
    "admin": ["editar", "leer", "eliminar"],
    "editor": ["editar", "leer"],
    "invitado": ["leer"]
}
ips_permitidas = ["192.168.1.50", "192.168.1.100", "10.0.0.1"]

# --- Función de autenticación ---
def autenticar():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    rol = combo_rol.get()
    ip = entry_ip.get()
    
    # 1. Verificar credenciales (if-else + operadores lógicos)
    if usuario not in usuarios_registrados or usuarios_registrados[usuario] != contraseña:
        messagebox.showerror("Error", "❌ Credenciales incorrectas.")
        return
    
    # 2. Verificar rol y permisos (if-elif-else + operador in)
    if rol not in roles:
        messagebox.showerror("Error", "❌ Rol no válido.")
        return
    
    # 3. Verificar IP (operador in)
    if ip not in ips_permitidas:
        messagebox.showerror("Error", f"🚫 IP {ip} bloqueada.")
        return
    
    # 4. Verificar permisos seleccionados (operadores lógicos)
    permisos_seleccionados = [var.get() for var in checkboxes_permisos.values() if var.get()]
    permisos_esperados = permisos_por_rol[rol]
    
    if not all(permiso in permisos_esperados for permiso in permisos_seleccionados):
        messagebox.showerror("Error", "❌ Permisos no autorizados para este rol.")
        return
    
    # 5. Coincidencia de patrones (match-case para acciones)
    accion = combo_accion.get()
    match accion:
        case "editar" if "editar" in permisos_esperados:
            messagebox.showinfo("Éxito", "📝 Edición permitida.")
        case "eliminar" if rol == "admin":
            messagebox.showinfo("Éxito", "🗑️ Eliminación permitida.")
        case "leer" if "leer" in permisos_esperados:
            messagebox.showinfo("Éxito", "📊 Lectura permitida.")
        case _:
            messagebox.showerror("Error", "❌ Acción no permitida.")
    
    # 6. Sistema activo (truthy/falsy)
    if not sistema_activo.get():
        messagebox.showwarning("Advertencia", "⚠️ Sistema en mantenimiento.")

# --- Configuración de la interfaz ---
root = tk.Tk()
root.title("Sistema de Autenticación")
root.geometry("400x400")

# Frame principal
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Campos de entrada
tk.Label(frame, text="Usuario:").grid(row=0, column=0)
entry_usuario = tk.Entry(frame)
entry_usuario.grid(row=0, column=1)

tk.Label(frame, text="Contraseña:").grid(row=1, column=0)
entry_contraseña = tk.Entry(frame, show="*")
entry_contraseña.grid(row=1, column=1)

tk.Label(frame, text="Rol:").grid(row=2, column=0)
combo_rol = tk.StringVar(value="editor")
rol_menu = tk.OptionMenu(frame, combo_rol, *roles)
rol_menu.grid(row=2, column=1)

tk.Label(frame, text="IP:").grid(row=3, column=0)
entry_ip = tk.Entry(frame)
entry_ip.insert(0, "192.168.1.100")
entry_ip.grid(row=3, column=1)

# Permisos (Checkbuttons)
tk.Label(frame, text="Permisos:").grid(row=4, column=0)
checkboxes_permisos = {}
for i, permiso in enumerate(["editar", "leer", "eliminar"]):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame, text=permiso, variable=var)
    chk.grid(row=4, column=1 + i)
    checkboxes_permisos[permiso] = var

# Acciones (Combobox)
tk.Label(frame, text="Acción:").grid(row=5, column=0)
combo_accion = tk.StringVar(value="leer")
accion_menu = tk.OptionMenu(frame, combo_accion, "editar", "eliminar", "leer")
accion_menu.grid(row=5, column=1)

# Sistema activo (Checkbutton)
sistema_activo = tk.BooleanVar(value=True)
chk_sistema = tk.Checkbutton(frame, text="Sistema Activo", variable=sistema_activo)
chk_sistema.grid(row=6, column=0, columnspan=2)

# Botón de autenticar
btn_autenticar = tk.Button(frame, text="Autenticar", command=autenticar)
btn_autenticar.grid(row=7, column=0, columnspan=2, pady=10)

# --- Ejecutar la aplicación ---
root.mainloop()