from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem
)


class TaskManagerUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Manager")
        self.setFixedSize(700, 450)

        self.init_ui()

    def init_ui(self):

        self.layout = QVBoxLayout()

        title = QLabel("Administrador de tareas")

        title.setStyleSheet("""
            color: white;
            font-size: 20px;
            font-weight: bold;
        """)

        self.layout.addWidget(title)

        # TABLE

        self.table = QTableWidget()

        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels([
            "PID",
            "Proceso",
            "Estado"
        ])

        self.layout.addWidget(self.table)

        # BUTTON

        self.kill_button = QPushButton("Finalizar proceso")

        self.kill_button.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 8px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #C0392B;
            }
        """)

        self.layout.addWidget(self.kill_button)

        self.setLayout(self.layout)

        self.setStyleSheet("""
            background-color: #181818;
            color: white;
        """)