# gui/desktop/desktop_window.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
from config.settings import APP_NAME


class DesktopWindow(QWidget):
    def __init__(self, username):
        super().__init__()

        self.username = username

        self.setWindowTitle(APP_NAME)
        self.showMaximized()

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # =========================
        # Área central (escritorio)
        # =========================
        desktop_area = QLabel(f"Bienvenido {self.username}")
        desktop_area.setAlignment(Qt.AlignmentFlag.AlignCenter)

        desktop_area.setStyleSheet("""
            font-size: 24px;
            color: white;
        """)

        # =========================
        # Barra inferior (taskbar)
        # =========================
        taskbar = QHBoxLayout()
        taskbar.setContentsMargins(10, 10, 10, 10)
        taskbar.setSpacing(20)

        taskbar_container = QWidget()
        taskbar_container.setLayout(taskbar)

        taskbar_container.setStyleSheet("""
            background-color: #111;
            border-top: 1px solid #222;
        """)

        # Ejemplo botón (luego apps)
        app_label = QLabel("🧮 Calculadora")
        app_label.setStyleSheet("color: white;")

        taskbar.addWidget(app_label)
        taskbar.addStretch()

        # =========================
        # Agregar al layout principal
        # =========================
        main_layout.addWidget(desktop_area)
        main_layout.addWidget(taskbar_container)

        self.setLayout(main_layout)

        # Fondo
        self.setStyleSheet("""
            background-color: #1e1e1e;
        """)
