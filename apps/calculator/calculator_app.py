from apps.calculator.ui import CalculatorUI


class CalculatorApp(CalculatorUI):
    def __init__(self):
        super().__init__()

        self.connect_buttons()

    def connect_buttons(self):
        for text, button in self.button_widgets.items():
            button.clicked.connect(
                lambda checked, value=text: self.on_button_click(value)
            )

    def on_button_click(self, value):
        current = self.display.text()

        if value == "=":
            try:
                result = str(eval(current))
                self.display.setText(result)
            except:
                self.display.setText("Error")

        else:
            self.display.setText(current + value)