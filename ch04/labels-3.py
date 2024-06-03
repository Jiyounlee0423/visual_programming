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

        self.ds_set_mwd()
        self.ds_set_label1()

        self.show() #window 보이기

    def ds_set_mwd(self):
        label0 = QLabel("Hello, World!", self)
        label0.setFont(QFont('Arial',20)) #Font 설정
        label0.setStyleSheet('background-color:red') #배경 설정
        label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label0.move(30,30)  #label0를 (30,30) 좌표로 이동

    def ds_set_label1(self):
        label1 = QLabel(self)

        
        pixmap = QPixmap('./image/labelImage.jpg')
        label1.setPixmap(pixmap)

        # label1.setPixmap(Qpixmap('./image/labelImage.png'))식으로 한줄로도 작성 가능

        pixmap = pixmap.scaled(200,200,Qt.AspectRatioMode.KeepAspectRatio) 
        label1.setScaledContents(True)


        label1.move(30,80)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #내가 만든 Qt 관련 main window 인스턴스를 만들어져야한다.
    mw = main_wnd()

    sys.exit(app.exec())



    