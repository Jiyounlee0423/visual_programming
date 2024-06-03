import sys

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QApplication, QHBoxLayout)
from PySide6.QtCore import Qt

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Event Handling Ex")
        label = QLabel(
            """<p>Press the <b>ESC</b> key
            to quit this program.</p>""")
        self.setCentralWidget(label)
        self.show()

    def keyPressEvent(self, event):
        """Reimplement the key press event to close the
        window."""
        if event.key() == Qt.Key.Key_Escape:
            print("ESC key pressed!")
            self.close()
        elif event.key() == Qt.Key.Key_A:
            print("A key pressed!")
            self.sub_window = NEWMW()
            self.sub_window.show()

    

class NEWMW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(400,400,50,50)
        self.setWindowTitle("SubWindow!")
        lm = QHBoxLayout()
        self.label2 = QLabel("""<p>Press the <b>Q</b> key
            to quit this program.</p>""")
        lm.addWidget(self.label2)
        self.setLayout(lm)
        self.show() #sub window이므로, show가 필요할 때마다 명시적으로 호출할 예정임

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            print("Q Key Pressed!") 

            self.close()
           


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())