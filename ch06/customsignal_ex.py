import sys, os

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QApplication, QVBoxLayout)
from PySide6.QtCore import Qt, Signal, QObject, QSize
from PySide6.QtGui import QPixmap, QKeyEvent

class MW(QMainWindow):
    change_pixmap = Signal(int)
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.fstr = os.path.dirname(os.path.abspath(__file__))

        self.setGeometry(100, 100, 200, 300)
        self.setWindowTitle("Custom Signals Ex")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        self.idx = 0

        self.change_pixmap.connect(self.change_pixmap_handler)

        lm = QVBoxLayout()

        info_label = QLabel("<p>Press <i>+</i> key or <i>-</i> key to change image</p>")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lm.addWidget(info_label)

        self.img_label = QLabel()
        pixmap = QPixmap(f"{self.fstr}/img/0.png")
        self.img_label.setPixmap(pixmap.scaled(QSize(180,250),
                                               Qt.AspectRatioMode.KeepAspectRatio,
                                               Qt.TransformationMode.SmoothTransformation
                                               ))
        self.img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lm.addWidget(self.img_label)

        container = QWidget()
        container.setLayout(lm)

        self.setCentralWidget(container)

    def keyPressEvent(self, event: QKeyEvent):
        print(event.key())

        if event.key() == Qt.Key.Key_Plus:
            self.change_pixmap.emit(1)
        elif event.key() == Qt.Key.Key_Minus:
            self.change_pixmap.emit(-1)

        return super().KeyPressedEvent(event)
    
    def change_pixmap_handler(self, offset):
        self.idx = (self.idx + offset) % 10
        if self.idx <0 :
            self.idx = 9
        print(self.idx)
        pixmap = QPixmap(f"{self.fstr}/img/{self.idx}.png")
        self.img_label.setPixmap(pixmap.scaled(
            QSize(180,250),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())    
