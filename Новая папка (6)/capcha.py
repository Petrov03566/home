import random, string
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore

class Capcha(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        len = 5
        capcha = string.ascii_uppercase + string.digits
        rnd = ''.join(random.sample(capcha, len))
        self.lbl = QLabel(rnd)
        self.cap = QLineEdit()
        self.lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.btn_cap = QPushButton("Ввести капчу")
        self.btn_cap.clicked.connect(self.capch_def)
        self.lbl_timer = QLabel()
        self.lbl.setObjectName("capcha")
        
        self.setLayout(self.vbox)
        self.vbox.addWidget(self.lbl)
        self.vbox.addWidget(self.cap)
        self.vbox.addWidget(self.lbl_timer)
        self.vbox.addWidget(self.btn_cap)
        with open("style.css","r") as css:
            self.setStyleSheet(css.read())
        
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        
    def capch_def(self):
        len = 5
        capcha = string.ascii_uppercase + string.digits
        rnd = ''.join(random.sample(capcha, len))
        if self.cap.text() == self.lbl.text():
            self.close()
        else:
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.timer_def)
            self.seconds = 11
            self.btn_cap.blockSignals(True)
            self.lbl.setText(rnd)
            self.timer.start()
            
            
    def timer_def(self):
        self.seconds -= 1
        self.lbl_timer.setText(str(self.seconds))
        if self.seconds == 0:
            self.timer.stop()
            self.lbl_timer.setText("")
            self.btn_cap.blockSignals(False)
