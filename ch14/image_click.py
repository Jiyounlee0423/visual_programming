import sys
import csv
import numpy as np
from PySide6.QtWidgets import (QMainWindow, QLabel, QWidget, QVBoxLayout, QFileDialog, QMessageBox, QApplication)
from PySide6.QtGui import QAction

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.image import imread

class MW(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Text Viewer") # 메인 Window Title

        self.create_actions()
        self.create_menu()

        # 창의 기본 설정: 그래프 영역, 캔버스, 그리기 도구 및 버튼 초기화 
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.axis('off')

        self.label = QLabel()

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        layout.addWidget(self.label)
        layout.addWidget(self.canvas)
        
        self.list = []
        
        # 마우스 드래그 상태 및 사각형 선택을 위한 변수 초기화 
        self.dragging = False
        self.rect = None
        self.start_point = (0,0)
        self.click_count = 0 #클릭 횟수 카운트를 위한 변수 
        self.image = None

        self.canvas.mpl_connect('button_press_event', self.on_click)





        self.show()
    
    def create_actions(self):
        self.actionOpen = QAction("Open")
        self.actionSave = QAction("Save")
        self.actionSave_as = QAction("Save as")
        self.actionClear = QAction("Clear")

        self.actionOpen.triggered.connect(self.open_file) # actionOpen instance의 trifferred signal을 처리할 self.open_file slot연결
        self.actionOpen.setShortcut('Ctrl+F') # actionOpen instance의 shortcut Key 설정
        self.actionSave.triggered.connect(self.save) # actionSave instance의 trifferred signal을 처리할 self.save slot연결
        self.actionSave.setShortcut('Ctrl+S') # actionSave instance의 shortcut Key 설정
        self.actionSave_as.triggered.connect(self.save_as) # actionSave_as instance의 trifferred signal을 처리할 self.save_as slot연결
        self.actionSave_as.setShortcut('Ctrl+Shift+S') # actionSave_as instance의 shortcut Key 설정
        self.actionClear.triggered.connect(self.clear) # actionClear instance의 trifferred signal을 처리할 self.clear slot연결
        self.actionClear.setShortcut('Ctrl+Del') # actionClear instance의 shortcut Key 설정

        #self.textEdit.textChanged.connect(self.my_slot) #QTextEdit instance에서 사용자가 입력한 text가 변경될 때 self.my_slot slot 연결

    def create_menu(self):
        mb = self.menuBar()

        menu_item = mb.addMenu("File")
        menu_item.addAction(self.actionOpen)
        menu_item.addAction(self.actionSave)
        menu_item.addAction(self.actionSave_as)
        menu_item.addAction(self.actionClear)
        


    def open_file(self):
        self.list = []
        # QFileDialg를 사용하여 파일선택 다이알로그를 띄움
        self.file_name, is_ok = QFileDialog.getOpenFileName(
               self,                 
               "open file",     
               "./",                   
               "image files (*.jpg)")
        
        if self.file_name:
            self.image = imread(self.file_name)
            print(type(self.image))
            self.ax.clear()
            self.ax.imshow(self.image)
            self.ax.axis('on')
            self.canvas.draw()

        self.name = self.file_name.split("/") # 파일 경로를 /로 구분
        self.label.setText(f"파일 명: {self.name[-1]}") # 구분된 파일경로의 마지막 부분 = 파일 이름

    def on_click(self, event):
            if self.image is None:
                return
            # 마우스 클릭 이벤트 핸들러: 더블클릭 검출을 위해 클릭 횟수 계산
            if event.button == 1:
                self.ax.add_patch(
                    plt.Circle(
                        (event.xdata, event.ydata),
                        10,
                        color='red', fill = True)
                    )
                self.canvas.draw()
                self.list.append((event.xdata, event.ydata))

            
            print(self.list)


    
    def save(self):
        try:
            fname= self.file_name # 파일을 열때 가져왔던 file의 path를 변수 fname에 저장 
            data = self.list # 좌표값을 변수 data에 저장 
            with open(fname.replace('jpg','csv'),'w', encoding='UTF8', newline='') as f: # Path 정보로 파일을 쓰기 모드로 열기 
                writer = csv.writer(f)
                writer.writerows(data)
                f.close()

            print("save file is {}".format(fname))  # 저장 위치 출력 

        except: # 가져온 파일 데이터가 없으면 뜨는 알림창, 파일을 열지 여부를 정하고 Yes선택 시 파일 Open으로 연결 
            dialog = QMessageBox.question(
                    self,
                    'Message',
                    'Not Select File, Select File?',
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
            if dialog == QMessageBox.StandardButton.Yes:
                self.open_file()
         

    def save_as(self):
        fname= QFileDialog.getSaveFileName(self) #파일 저장 위치 선택 요청
        data = self.list # 좌표값을 변수 data에 저장 
        with open(f'{fname[0]}.csv','w', encoding='UTF8', newline='') as f: # Path 정보로 파일을 쓰기 모드로 열기 
            writer = csv.writer(f)
            writer.writerows(data)
            f.close()
         
        print("save as file is {}".format(fname)) # 저장 위치 출력 


    def clear(self):
        self.figure.clear()  
        self.canvas.draw()

    def my_slot(self):
        number = len(self.textEdit.toPlainText()) # QTextEdit의 content의 내용을 plain text로 반환하여 글자수 계산 
        self.statusbar.showMessage(f"포인트 수: {number}") # status bar에 글자수 표시

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())