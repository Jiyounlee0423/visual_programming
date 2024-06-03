import sys

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QApplication)
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())