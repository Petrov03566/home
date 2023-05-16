from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        lbl = QLabel("Успешный вход")
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        vbox.addWidget(lbl)