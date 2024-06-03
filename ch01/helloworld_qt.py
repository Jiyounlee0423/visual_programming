import sys
import PySide6.QtCore
from PySide6.QtWidgets import (QWidget, 
                               QApplication, 
                               QLabel)

class MW(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle('Mian Window in PyQt')
        #self.setup_main_wnd()

       # hello_label = QLabel(self)
       # hello_label.setText('Hello, World and Qt!')
        #hello_label.move(150, 90)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())



