from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QGridLayout
)

from PyQt6.QtCore import Qt


class CalculatorUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.setFixedSize(320, 420)

        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.display.setStyleSheet("""
            font-size: 28px;
            padding: 15px;
            background-color: #1f1f1f;
            color: white;
            border-radius: 10px;
        """)

        self.main_layout.addWidget(self.display)

        # Grid botones
        self.grid = QGridLayout()

        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 0
        col = 0

        self.button_widgets = {}

        for text in self.buttons:
            button = QPushButton(text)

            button.setFixedSize(65, 65)

            button.setStyleSheet("""
                QPushButton {
                    background-color: #2d2d2d;
                    color: white;
                    font-size: 18px;
                    border-radius: 10px;
                }

                QPushButton:hover {
                    background-color: #444;
                }
            """)

            self.grid.addWidget(button, row, col)

            self.button_widgets[text] = button

            col += 1

            if col > 3:
                col = 0
                row += 1

        self.main_layout.addLayout(self.grid)

        self.setLayout(self.main_layout)

        self.setStyleSheet("""
            background-color: #181818;
        """)