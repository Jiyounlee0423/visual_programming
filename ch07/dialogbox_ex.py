import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication,
                               QMainWindow, QPushButton, QWidget)

class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDialog Example')
        button = QPushButton('Press me for a dialog!', self)
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        self.show()

    def button_clicked(self, s):
        print("click", s)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    app.exec()