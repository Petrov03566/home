import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from second import SecondWindow
from capcha import Capcha

        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200,200)
        vbox = QVBoxLayout()
        self.line_log = QLineEdit()
        self.line_pas = QLineEdit()
        lbl_log = QLabel("Логин")
        lbl_pas = QLabel("Пароль")
        
        btn_auth = QPushButton("Войти")
        btn_auth.clicked.connect(self.btn_click)
        
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        
        vbox.addWidget(lbl_log)
        vbox.addWidget(self.line_log)
        vbox.addWidget(lbl_pas)
        vbox.addWidget(self.line_pas)
        vbox.addWidget(btn_auth)
        with open("style.css","r") as css:
            self.setStyleSheet(css.read())
    
        
    def btn_click(self):
        if self.line_log.text() == "user" and self.line_pas.text() == "1234":
            self.second = SecondWindow()
            self.second.show()
        else:
            self.capcha = Capcha()
            self.capcha.show()
    

        

        

        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()