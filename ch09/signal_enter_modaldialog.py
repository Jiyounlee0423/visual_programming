import sys

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QApplication, QVBoxLayout, QInputDialog, QLineEdit)
from PySide6.QtCore import Qt, Signal, QObject, QSize
from PySide6.QtGui import QPixmap, QKeyEvent

class MW(QMainWindow):
    def __init__(self): # 생성자
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setGeometry(100, 100, 200, 300) #Top left가 (100,100), 폭이 200, 높이가 300
        self.setWindowTitle("Custom Signals: my_signal") # MainWindow Title 설정
        self.setup_main_wnd() # setup_main_wnd 실행
        self.show() #window 보이기

    def setup_main_wnd(self):

        lm = QVBoxLayout() # 수직으로 widget들을 배치하는 layout manager 생성

        info_label = QLabel("<p>Press <i>Enter</i> key to Input Int</p>") #고정된 text 문자열을 보여주는 QLabel widget을 이용하여 문자 출력
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter) # 레이블 내 텍스트 가운데 정렬
        lm.addWidget(info_label) # 생성된 layout manager인 lm에 widget추가

        self.ret_label = QLabel() #고정된 text 문자열을 보여주는 QLabel widget을 이용하여 문자(빈칸) 출력
        lm.addWidget(self.ret_label) # 생성된 layout manager인 lm에 widget추가


        container = QWidget() # Container 생성
        container.setLayout(lm) # 생성된 Container의 layout manager을 lm로 설정

        self.setCentralWidget(container) #생성한 Container를 MainWindow의 CentralWidget으로 설정

    def keyPressEvent(self, event: QKeyEvent):
        print(event.key())

        if event.key() == Qt.Key.Key_Return: # event.key 값이 Enter를 입력받은 값이면 self.my_signal 실행
            self.my_signal()
            
    
    def my_signal(self):
        ret_int, is_ok = QInputDialog.getInt( # 사용자로 부터 정수 입력을 받는 modal dialog
            self,  # 부모 widget
            "Input Integer",      # dialog title
            "Enter Yout Int Value!",            # input field위의 label text
            0,         # 기본 text값.
            0, 100, # min and max
            1, #step
        )

        self.ret_label.setText(f'{ret_int}') # 입력 받은 정수 값을 label에 표시


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())    
