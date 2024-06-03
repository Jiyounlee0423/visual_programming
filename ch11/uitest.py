import sys
from PySide6.QtWidgets import (QMainWindow, QApplication)

from outputfile import Ui_MainWindow 

class MW(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())