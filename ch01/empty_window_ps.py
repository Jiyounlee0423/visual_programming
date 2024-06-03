#basic_window.py
#import necessary modules
import sys

PYSIDE = True
try:
    import PySide6.QtCore
    from PySide6.QtWidgets import (QApplication, QWidget, QLabel)

except Exception as e:
    print(e)
    PYSIDE = False

PYQT = True
try:
    import PyQt6.QtCore
    from PyQt6.QtWidgets import (QApplication, QWidget, QLabel)

except Exception as e:
    print(e)
    PYQT = False

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200,100,400,200)
        self.setWindowTitle("Main Window in PyQt") 
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        hello_label = QLabel(self)
        hello_label.setText('Hello, World and Qt!')
        hello_label.move(150,90)

if __name__ == '__main__':

    if PYSIDE:
        print(PySide6.__version__)
        print(PySide6.QtCore.__version__)
    if PYQT:
        print(PyQt6.QtCore.qVersion())

    app = QApplication(sys.argv)   #01
    window = MW()                  #02
    sys.exit(app.exec())           #03
