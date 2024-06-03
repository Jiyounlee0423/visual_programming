from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

import sys

class main_wnd (QWidget):
    
    def __init__(self):
        super().__init__()

        #main window 크기 등을 설정
        self.setGeometry(100, 100, 600, 600) #Top left가 (100,100), 폭이 600, 높이가 300
        self.setFixedSize(600,300)  #폭, 높이 600,300으로 고정

        #mian window에 포함되는 Widgets을 생성 및 추가
        label0 = QLabel("Hello, World!", self)
        label0.move(30,30)  #label0를 (30,30) 좌표로 이동

        self.show() #window 보이기




if __name__ == "__main__":
    app = QApplication(sys.argv)

    #내가 만든 Qt 관련 main window 인스턴스를 만들어져야한다.
    mw = main_wnd()

    sys.exit(app.exec())



    