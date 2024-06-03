import sys

from PySide6.QtWidgets import (
        QApplication, QMainWindow,
        QWidget, QPushButton, QLabel, QVBoxLayout,
        QLineEdit, QInputDialog)

class MW(QMainWindow):

    def __init__(self):
        super(MW, self).__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        layout = QVBoxLayout()

        self.l_buttons = ['getText', 'getMultilineText','getInt','getDouble']
        for idx, c_str in enumerate(self.l_buttons):
            self.button0 = QPushButton(c_str)
            self.button0.clicked.connect(self.slot00)
            layout.addWidget(self.button0)

        self.ret_label = QLabel()

        
        layout.addWidget(self.button0)
        layout.addWidget(self.ret_label)

        tmp = QWidget()
        tmp.setLayout(layout)

        self.setCentralWidget(tmp)

    def slot00(self):
        print(self.sender())

        sender = self.sender()

        tmp_str = sender.text()
        is_ok = False

        if tmp_str == self.l_buttons[0]:
            ret_value, is_ok = QInputDialog.getText(
                self,
                "Input Text",
                "Enter Your Text!",
                #QLineEdit.PasswordEchoOnEdit,
                #"default text!",
            )

        elif tmp_str == self.l_buttons[1]:
            ret_value, is_ok = QInputDialog.getMultiLineText(
                self,
                "InputMult-Line Text",
                "Enter Youy Multi-Line Text!",
            )

        elif tmp_str == self.l_buttons[2]:
            ret_value, is_ok = QInputDialog.getInt(
                self,
                "Input Integer",
                "Enter Yout Int Value!",
                0,
                0, 100,
                1,
            )
        elif tmp_str == self.l_buttons[3]:
            ret_value, is_ok = QInputDialog.getDouble(
                self,
                "Input Double",
                "Enter Yout Double Value!",
                0,
                0.0, 100.0,
                4,
            )

        if is_ok:
            print(type(ret_value), type(is_ok))
            self.ret_label.setText(f'{ret_value}')
        

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())