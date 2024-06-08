import sys
from PySide6.QtWidgets import (QApplication, QDialog, QMainWindow, 
                               QPushButton, QLabel, QDialogButtonBox,
                               QVBoxLayout)

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog Ex.")

        button = QPushButton("Press it for a Dialog")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)
        dlg = QDialog(self)
        dlg.setWindowTitle("QDialog Title")
        
        dlg = CustomDlg(self)
        if dlg.exec():
            print('ok')
        else:
            print("cancle")

class CustomDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Hello, QDialog')

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(buttons)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        message = QLabel('Is something ok?')

        self.layout = QVBoxLayout()
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    app.exec()