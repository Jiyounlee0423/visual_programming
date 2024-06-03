import sys
import subprocess
import traceback

from PySide6.QtWidgets import (
    QMainWindow, QWidget,
    QVBoxLayout,
    QLineEdit, QLabel, QPushButton,
    QApplication)

class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        
        lm = QVBoxLayout()

        self.le = QLineEdit()
        lm.addWidget(self.le)
        self.le.returnPressed.connect(self.ds_slot)

        self.btn = QPushButton('Run')
        lm.addWidget(self.btn)
        self.btn.clicked.connect(self.ds_slot)

        self.dp1 = QLabel('')
        lm.addWidget(self.dp1)

        dummy_container = QWidget()
        dummy_container.setLayout(lm)

        self.setCentralWidget(dummy_container)
        self.show()

    def ds_run(self, cmd, enc='cp949'):
        ret_p = subprocess.run(cmd, shell=True, capture_output=True, encoding=enc)
        return ret_p.stdout
    
    def ds_slot(self):
        cmd_str = self.le.text()
        cmd = cmd_str.split()
        ret_str = self.ds_run(cmd)
        self.dp1.setText(ret_str)
        self.ds_run(self)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
