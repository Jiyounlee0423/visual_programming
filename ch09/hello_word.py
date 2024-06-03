from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QApplication, QVBoxLayout

import sys, os

class main_wnd (QMainWindow):
    
    def __init__(self):
        super().__init__()

        #main window 크기 등을 설정
        self.setGeometry(800, 400, 300, 300) #Top left가 (800,400), 폭이 300, 높이가 300

        c_module_path = os.path.realpath(__file__) # 파일의 실제 경로
        c_module_dir = os.path.dirname(c_module_path) #파일 이름 없이 디렉토리 얻어오기
        print(c_module_dir) #MainWindow 스크립트 파일의 디렉토리 위치 출력

        #mian window에 포함되는 Widgets을 생성 및 추가
        label0 = QLabel("Hello, World!") #고정된 text 문자열을 보여주는 QLabel widget을 이용하여 "Hello, widget" 출력
        label_d = QLabel(f"realpath: {c_module_dir}") #고정된 text 문자열을 보여주는 QLabel widget을 이용하여 MainWindow 스크립트 파일의 디렉토리 위치 출력
        
        vbox = QVBoxLayout() #수직으로 widget들을 배치하는 layout manager 생성
        vbox.addWidget(label0) # 생성된 layout manager인 vbox에 widget추가
        vbox.addWidget(label_d) # 생성된 layout manager인 vbox에 widget추가
        
        container = QWidget() # Container 생성
        container.setLayout(vbox) # 생성된 Container의 layout manager을 vbox로 설정
        
        self.setCentralWidget(container) #생성한 Container를 MainWindow의 CentralWidget으로 설정

        self.show() #window 보이기


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = main_wnd()
    sys.exit(app.exec())
