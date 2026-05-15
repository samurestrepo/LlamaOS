from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QPushButton,
    QLabel,
    QHBoxLayout
)


class FileExplorerUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Explorador de archivos")
        self.setFixedSize(600, 450)

        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout()

        # Header
        self.path_label = QLabel("Ruta actual")

        self.path_label.setStyleSheet("""
            color: white;
            font-size: 14px;
            font-weight: bold;
        """)

        self.main_layout.addWidget(self.path_label)

        # Lista archivos
        self.file_list = QListWidget()

        self.file_list.setStyleSheet("""
            QListWidget {
                background-color: #202020;
                color: white;
                border-radius: 10px;
                padding: 8px;
                font-size: 13px;
            }
        """)

        self.main_layout.addWidget(self.file_list)

        # Botones
        buttons_layout = QHBoxLayout()

        self.create_button = QPushButton("Crear archivo")
        self.delete_button = QPushButton("Eliminar archivo")

        for btn in [self.create_button, self.delete_button]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #E67E22;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 10px;
                    font-weight: bold;
                }

                QPushButton:hover {
                    background-color: #d35400;
                }
            """)

        buttons_layout.addWidget(self.create_button)
        buttons_layout.addWidget(self.delete_button)

        self.main_layout.addLayout(buttons_layout)

        self.setLayout(self.main_layout)

        self.setStyleSheet("""
            background-color: #181818;
        """)