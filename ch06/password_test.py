import sys
import os
from datetime import datetime

from PySide6.QtWidgets import (
    QMainWindow, QWidget,
    QVBoxLayout,
    QLineEdit, QLabel, QPushButton,
    QApplication)
from PySide6.QtGui import *
from PySide6.QtCore import Qt, QTimer

class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.password = "1234"
        timer = QTimer()
        timer.setInterval(1000)

        timer.singleShot(900000, self.end)
        #timer.singleShot(5000, self.end)

        lm = QVBoxLayout()

        self.lb = QLabel("PassWord:")
        lm.addWidget(self.lb)

        self.le = QLineEdit()
        self.le.setValidator(QIntValidator(0, 1000))
        self.le.setEchoMode(QLineEdit.Password)
        lm.addWidget(self.le)
        self.le.textChanged.connect(self.check)

        self.btn = QPushButton('login')
        self.btn.setDisabled(True)
        lm.addWidget(self.btn)
        self.btn.clicked.connect(self.end)

        self.dp1 = QLabel('')
        lm.addWidget(self.dp1)

        dummy_container = QWidget()
        dummy_container.setLayout(lm)

        self.setCentralWidget(dummy_container)
        self.show()
    
    def check(self):
        tmp = str(self.le.text())
        print(tmp)
        print(self.password)
        if self.password == tmp:
            self.btn.setEnabled(True)
        else:
            self.btn.setDisabled(True)


    
    def end(self):
        self.close()

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
