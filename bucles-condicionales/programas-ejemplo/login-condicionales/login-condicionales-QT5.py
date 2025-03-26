import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QComboBox,
    QCheckBox, QPushButton, QVBoxLayout, QWidget, QMessageBox, QGridLayout
)
from PyQt5.QtGui import QFont

# --- Datos del sistema ---
usuarios_registrados = {"ana": "1234"}
roles = ["admin", "editor", "invitado"]
permisos_por_rol = {
    "admin": ["editar", "leer", "eliminar"],
    "editor": ["editar", "leer"],
    "invitado": ["leer"]
}
ips_permitidas = ["192.168.1.50", "192.168.1.100", "10.0.0.1"]

class VentanaAutenticacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Autenticación con PyQt")
        self.setGeometry(100, 100, 400, 350)
        
        # Widget central y layout
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout = QGridLayout()
        widget_central.setLayout(layout)
        
        # --- Componentes ---
        # Usuario
        self.label_usuario = QLabel("Usuario:")
        self.entry_usuario = QLineEdit()
        layout.addWidget(self.label_usuario, 0, 0)
        layout.addWidget(self.entry_usuario, 0, 1)
        
        # Contraseña
        self.label_contraseña = QLabel("Contraseña:")
        self.entry_contraseña = QLineEdit()
        self.entry_contraseña.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_contraseña, 1, 0)
        layout.addWidget(self.entry_contraseña, 1, 1)
        
        # Rol
        self.label_rol = QLabel("Rol:")
        self.combo_rol = QComboBox()
        self.combo_rol.addItems(roles)
        layout.addWidget(self.label_rol, 2, 0)
        layout.addWidget(self.combo_rol, 2, 1)
        
        # IP
        self.label_ip = QLabel("IP:")
        self.entry_ip = QLineEdit("192.168.1.100")
        layout.addWidget(self.label_ip, 3, 0)
        layout.addWidget(self.entry_ip, 3, 1)
        
        # Permisos
        self.label_permisos = QLabel("Permisos:")
        layout.addWidget(self.label_permisos, 4, 0)
        self.checkbox_editar = QCheckBox("Editar")
        self.checkbox_leer = QCheckBox("Leer")
        self.checkbox_eliminar = QCheckBox("Eliminar")
        layout.addWidget(self.checkbox_editar, 4, 1)
        layout.addWidget(self.checkbox_leer, 5, 1)
        layout.addWidget(self.checkbox_eliminar, 6, 1)
        
        # Acción
        self.label_accion = QLabel("Acción:")
        self.combo_accion = QComboBox()
        self.combo_accion.addItems(["editar", "eliminar", "leer"])
        layout.addWidget(self.label_accion, 7, 0)
        layout.addWidget(self.combo_accion, 7, 1)
        
        # Sistema Activo
        self.checkbox_sistema = QCheckBox("Sistema Activo")
        self.checkbox_sistema.setChecked(True)
        layout.addWidget(self.checkbox_sistema, 8, 0, 1, 2)
        
        # Botón
        self.btn_autenticar = QPushButton("Autenticar")
        self.btn_autenticar.clicked.connect(self.autenticar)
        layout.addWidget(self.btn_autenticar, 9, 0, 1, 2)
        
        # Estilo (QSS)
        self.setStyleSheet("""
            QLabel { font-weight: bold; }
            QLineEdit, QComboBox, QCheckBox { padding: 5px; }
            QPushButton { background-color: #4CAF50; color: white; padding: 10px; }
        """)

    def autenticar(self):
        usuario = self.entry_usuario.text()
        contraseña = self.entry_contraseña.text()
        rol = self.combo_rol.currentText()
        ip = self.entry_ip.text()
        accion = self.combo_accion.currentText()
        sistema_activo = self.checkbox_sistema.isChecked()
        
        # 1. Verificar credenciales
        if usuario not in usuarios_registrados or usuarios_registrados[usuario] != contraseña:
            QMessageBox.critical(self, "Error", "❌ Credenciales incorrectas.")
            return
        
        # 2. Verificar IP
        if ip not in ips_permitidas:
            QMessageBox.critical(self, "Error", f"🚫 IP {ip} bloqueada.")
            return
        
        # 3. Verificar permisos seleccionados
        permisos_seleccionados = []
        if self.checkbox_editar.isChecked():
            permisos_seleccionados.append("editar")
        if self.checkbox_leer.isChecked():
            permisos_seleccionados.append("leer")
        if self.checkbox_eliminar.isChecked():
            permisos_seleccionados.append("eliminar")
        
        permisos_esperados = permisos_por_rol[rol]
        if not all(p in permisos_esperados for p in permisos_seleccionados):
            QMessageBox.critical(self, "Error", "❌ Permisos no autorizados.")
            return
        
        # 4. Coincidencia de patrones para acciones (match-case)
        match accion:
            case "editar" if "editar" in permisos_esperados:
                QMessageBox.information(self, "Éxito", "📝 Edición permitida.")
            case "eliminar" if rol == "admin":
                QMessageBox.information(self, "Éxito", "🗑️ Eliminación permitida.")
            case "leer" if "leer" in permisos_esperados:
                QMessageBox.information(self, "Éxito", "📊 Lectura permitida.")
            case _:
                QMessageBox.critical(self, "Error", "❌ Acción no permitida.")
        
        # 5. Verificar estado del sistema
        if not sistema_activo:
            QMessageBox.warning(self, "Advertencia", "⚠️ Sistema en mantenimiento.")

# --- Ejecución ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaAutenticacion()
    ventana.show()
    sys.exit(app.exec_())