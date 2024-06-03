import sys
import traceback

from PySide6.QtWidgets import (QApplication, QWidget,
                               QMainWindow,
                               QLabel,
                               QHBoxLayout)

from PySide6.QtCore import Qt

class DsLabel(QLabel):

    def __init__(self,text,color):
        super().__init__(text)
        self. setStyleSheet(f"background-color: {color}")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QHBoxLayout")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QHBoxLayout()

        colors = ['aliceblue','skyblue','lavender','deeppupple','deeppink']

        for i,c in enumerate(colors):
            lm.addWidget(DsLabel(str(i),c))

        dummy = QWidget()
        dummy.setLayout(lm)

        self.setCentralWidget(dummy)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
