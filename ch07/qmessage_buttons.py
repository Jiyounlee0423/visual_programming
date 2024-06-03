import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import ( QApplication, QWidget,
    QDialog,
    QMainWindow,
    QPushButton, QLabel, QDialogButtonBox, QVBoxLayout, QMessageBox
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
        '''
        # for 문으로 간단히 구현
        1_str = ['Simple Dialog',
                  'Custom Dialog',
                  'QMessageBox.information',
                  'QMessageBox.warning',
                  'QMessageBox.critical',
                  'QMessageBox.about',
                  'QMessageBox.question']
        1_slot = [self.slot0,
                  self.slot1,
                  self.slot2,
                  self.slot3,
                  self.slot4,
                  self.slot5,
                  self.slot6,
                  self.slot7]

        layout = QVBoxLayout()
        for idx, (i,s) in enumerate(zip(1_str, 1_slot)):
        self.i = idx
        button = QPushButton(i)
        button.clicked.connect(s)
        layout.addWidget(button)

        a = QWidget()
        a.setLayout(layout)
        self.setCentralWidget(a)

        '''

        lm = QVBoxLayout()
        
        button1 = QPushButton("Press it for a Simple QDialog")
        lm.addWidget(button1)
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Press it for a Custom Dialog")
        lm.addWidget(button2)
        button2.clicked.connect(self.button2_clicked)
        button3 = QPushButton("Press it for a information")
        lm.addWidget(button3)
        button3.clicked.connect(self.button3_clicked)
        button4 = QPushButton("Press it for a about")
        lm.addWidget(button4)
        button4.clicked.connect(self.button4_clicked)
        button5 = QPushButton("Press it for a question")
        lm.addWidget(button5)
        button5.clicked.connect(self.button5_clicked)
        button6 = QPushButton("Press it for a ciritical")
        lm.addWidget(button6)
        button6.clicked.connect(self.button6_clicked)
        button7 = QPushButton("Press it for a warning")
        lm.addWidget(button7)
        button7.clicked.connect(self.button7_clicked)

        dummy= QWidget()
        dummy.setLayout(lm)

        self.setCentralWidget(dummy)

    def button1_clicked(self):
        print("click")
        dlg = QDialog(self) 
        dlg.setWindowTitle("QDialog Title") 
        dlg.exec()

    def button2_clicked(self):
        dlg = CustomDlg(self)
        if dlg.exec(): # Modal Dialog
             print('ok')
        else:
             print("cancel")

    def button3_clicked(self):
        result = QMessageBox.information(
            self,
            'Message',
            'This is an information message'
        )
        print(f'QMessage.information:{result}')

    def button4_clicked(self):
        result = QMessageBox.about(
            self,
            'About This SQ',
            """<p>The example of QMessageBox</p>
            <p>version 0.1</p>"""
        )

    def button5_clicked(self):
        ans = QMessageBox.question(
            self,
            'title of question', #질문 제목
            'content of question', # 질문 내용
             QMessageBox.StandardButton.No | 
             QMessageBox.StandardButton.Yes, # responses
             QMessageBox.StandardButton.Yes #default respons
        )  

    def button6_clicked(self):
        result = QMessageBox.critical(
            self,
            'Message',
            'This is an information message'
        )
    
    def button7_clicked(self):
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
