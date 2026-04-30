from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox, QGraphicsDropShadowEffect
)

from PyQt6.QtCore import Qt
from config.settings import APP_NAME
from PyQt6.QtGui import QPixmap
from config.settings import APP_NAME, LOGO_PATH




class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setFixedSize(500, 600)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(60, 60, 60, 60)

        # Logo / Nombre
        logo = QLabel()
        pixmap = QPixmap(LOGO_PATH)

        pixmap = pixmap.scaled(
            180, 180,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setFixedHeight(130)

        # Nombre sistema
        title = QLabel(APP_NAME)
        title.setText(
            '<span style="color:#E67E22;">llama</span>'
            '<span style="color:white;">OS</span>'
        )
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 36px;
            font-weight: 700;
            color: #f5f5f5;
            letter-spacing: 2px;
        """)


        subtitle = QLabel("Iniciar sesión")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            font-size: 16px;
            color: #bbbbbb;
        """)

        # Usuario
        self.username = QLineEdit()
        self.username.setPlaceholderText("Usuario")

        # Contraseña
        self.password = QLineEdit()
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        # Botón
        login_btn = QPushButton("Ingresar")
        login_btn.clicked.connect(self.login)

        # Estilos Inputs / botón
        self.username.setStyleSheet(self.input_style())
        self.password.setStyleSheet(self.input_style())
        login_btn.setStyleSheet(self.button_style())

        # Agregar widgets
        layout.addStretch()
        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addSpacing(10)
        layout.addWidget(login_btn)
        layout.addStretch()

        self.setLayout(layout)

        # Fondo
        self.setStyleSheet("""
            background-color: #1e1e1e;
        """)

    def login(self):
        user = self.username.text()
        password = self.password.text()

        if user == "admin" and password == "1234":
            QMessageBox.information(self, "Acceso", "Bienvenido a llamaOS")
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas")

    def input_style(self):
        return """
            QLineEdit {
                padding: 12px;
                border: 2px solid #333;
                border-radius: 10px;
                background-color: #2b2b2b;
                color: white;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 2px solid #E67E22;
            }
        """

    def button_style(self):
        return """
            QPushButton {
                padding: 12px;
                border: none;
                border-radius: 10px;
                background-color: #E67E22;
                color: white;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #d35400;
            }
        """
