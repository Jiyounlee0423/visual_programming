import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import ( QApplication, QWidget,
    QDialog,
    QMainWindow, QGroupBox, QButtonGroup,
    QRadioButton, QLabel, QDialogButtonBox, QVBoxLayout, QMessageBox
)
class CustomDlg(QDialog):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.setWindowTitle('Hello, QDialog')

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(buttons)

        self.button_box.accepted.connect(self.accept)

        self.button_box.rejected.connect(self.reject)

        message = QLabel('Is somthing ok?')

        self.layout = QVBoxLayout()
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box)

        self.setLayout(self.layout)

class MW(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog Ex.")

        lm = QVBoxLayout()

        self.radios = QGroupBox("QMessageBox")
        lm.addWidget(self.radios)

        self.set_radios()

        dummy= QWidget()
        dummy.setLayout(lm)

        self.setCentralWidget(dummy)

    def set_radios(self):
        lm = QVBoxLayout()

        self.button_group = QButtonGroup()

        self.button1 = QRadioButton("Simple QDialog")
        lm.addWidget(self.button1)
        self.button1.clicked.connect(self.button_clicked)
        self.button2 = QRadioButton("Custom Dialog")
        lm.addWidget(self.button2)
        self.button2.clicked.connect(self.button_clicked)
        self.button3 = QRadioButton("information")
        lm.addWidget(self.button3)
        self.button3.clicked.connect(self.button_clicked)
        self.button4 = QRadioButton("about")
        lm.addWidget(self.button4)
        self.button4.clicked.connect(self.button_clicked)
        self.button5 = QRadioButton("question")
        lm.addWidget(self.button5)
        self.button5.clicked.connect(self.button_clicked)
        self.button6 = QRadioButton("ciritical")
        lm.addWidget(self.button6)
        self.button6.clicked.connect(self.button_clicked)
        self.button7 = QRadioButton("warning")
        lm.addWidget(self.button7)
        self.button7.clicked.connect(self.button_clicked) 

        self.radios.setLayout(lm)


    def button_clicked(self):
        if self.button1.isChecked():
            print("click")
            dlg = QDialog(self) 
            dlg.setWindowTitle("QDialog Title") 
            dlg.exec()
        elif self.button2.isChecked():
            dlg = CustomDlg(self)
            if dlg.exec(): # Modal Dialog
                print('ok')
            else:
                print("cancel")
        elif self.button3.isChecked():
            result = QMessageBox.information(
                self,
                'Message',
                'This is an information message'
            )
            print(f'QMessage.information:{result}')
        elif self.button4.isChecked():
            result = QMessageBox.about(
                self,
                'About This SQ',
                """<p>The example of QMessageBox</p>
                <p>version 0.1</p>"""
            )
        elif self.button5.isChecked():
            ans = QMessageBox.question(
                self,
                'title of question', #질문 제목
                'content of question', # 질문 내용
                QMessageBox.StandardButton.No | 
                QMessageBox.StandardButton.Yes, # responses
                QMessageBox.StandardButton.Yes #default respons
            )
        elif self.button6.isChecked():
            result = QMessageBox.critical(
                self,
                'Message',
                'This is an information message'
            )
        elif self.button7.isChecked():
            result = QMessageBox.warning(
                self,
                'Message',
                'This is an information message'
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    app.exec()
