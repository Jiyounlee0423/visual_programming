import sys,os
import csv
import numpy as np
from PySide6.QtWidgets import (QMainWindow,QStatusBar, QListWidgetItem, QLabel,QListWidget, QHBoxLayout, QWidget, QVBoxLayout, QFileDialog, QMessageBox, QApplication)
from PySide6.QtGui import QAction, QFont
from PySide6.QtCore import Qt

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.image as mpimg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

import turtle

class MW(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer") # 메인 Window Title

        self.create_actions() # 액션 생성 메소드 호출
        self.create_menu() # 메뉴 생성 메소드 호출

        # 창의 기본 설정: 그래프 영역, 캔버스, 그리기 도구 및 버튼 초기화 
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setStyleSheet("background-color: #E6E6FA;")
        self.ax = self.figure.add_subplot(111)
        self.ax.axis('off')

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter) # 가운데 정렬
        font = QFont("Sans-serif", 15, QFont.Bold)
        self.label.setFont(font) 

        layout = QHBoxLayout() # 메인 레이아웃 설정
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        layout.addWidget(self.canvas)
        
        right_layout = QVBoxLayout() # 우측 레이아웃 설정
        right_widget = QWidget()
        right_widget.setLayout(right_layout)

        # QListWidget 생성 및 설정
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.on_item_clicked) # 아이템 클릭 시 호출될 메소드 연결
        layout.addWidget(self.list_widget)
        
        # NavigationToolbar 생성 및 설정.
        self.nav_toolbar = NavigationToolbar(self.canvas, self)
        
        right_layout.addWidget(self.label)
        right_layout.addWidget(self.nav_toolbar)
        right_layout.addWidget(self.canvas)

        layout.addWidget(right_widget)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.list = []
        
        # 상태 변수 초기화 
        self.dragging = False
        self.next = False
        self.start_point = (0,0)
        self.image = None
        self.point_on = False
        self.line_on = False

        # 마우스 이벤트 연결
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('button_release_event', self.on_release)

        self.show() # 윈도우 표시
    
    def create_actions(self):
        self.actionOpen = QAction("Open")
        self.actionSave = QAction("Save")
        self.actionSave_as = QAction("Save as")
        self.actionClear = QAction("Clear")

        # 각 액션에 대한 단축키 및 연결 메소드 설정
        self.actionOpen.triggered.connect(self.open_file) # actionOpen instance의 trifferred signal을 처리할 self.open_file slot연결
        self.actionOpen.setShortcut('Ctrl+F') # actionOpen instance의 shortcut Key 설정
        self.actionSave.triggered.connect(self.save) # actionSave instance의 trifferred signal을 처리할 self.save slot연결
        self.actionSave.setShortcut('Ctrl+S') # actionSave instance의 shortcut Key 설정
        self.actionSave_as.triggered.connect(self.save_as) # actionSave_as instance의 trifferred signal을 처리할 self.save_as slot연결
        self.actionSave_as.setShortcut('Ctrl+Shift+S') # actionSave_as instance의 shortcut Key 설정
        self.actionClear.triggered.connect(self.clear) # actionClear instance의 trifferred signal을 처리할 self.clear slot연결
        self.actionClear.setShortcut('Ctrl+Del') # actionClear instance의 shortcut Key 설정

    def create_menu(self):
        mb = self.menuBar()

        menu_item = mb.addMenu("File") # 파일 메뉴 생성
        menu_item.addAction(self.actionOpen)
        menu_item.addAction(self.actionSave)
        menu_item.addAction(self.actionSave_as)
        menu_item.addAction(self.actionClear)
    
    def on_item_clicked(self, item):
        # 선택된 아이템의 파일 경로를 가져와서 이미지 표시
        self.file_path = item.data(Qt.UserRole)
        self.file_name = self.file_path.replace("\\","/")
        self.name = self.file_name.split("/") # 파일 경로를 /로 구분
        self.label.setText(f"파일 명: {self.name[-1]}") # 구분된 파일경로의 마지막 부분 = 파일 이름
        self.display_image(self.file_path)
        self.status_bar.showMessage(self.file_path)

    def display_image(self, image_path):
        self.ax.clear()
        self.point_on = False
        self.line_on = False
        self.image = mpimg.imread(image_path)
        self.ax.imshow(self.image)
        self.ax.axis("off")
        self.figure.subplots_adjust(
            left=0, right=1,
            top=1, bottom=0
        )
        self.canvas.draw()

    def open_file(self):
        self.list = []
        # QFileDialg를 사용하여 파일선택 다이알로그를 띄움
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.list_widget.clear()
            # 디렉토리의 jpg 파일 목록 가져오기
            jpg_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
            for jpg_file in jpg_files:
                item = QListWidgetItem(jpg_file)
                item.setData(Qt.UserRole, os.path.join(directory, jpg_file))
                self.list_widget.addItem(item)

    ### 사진을 불러와 
    ### 1. 좌클릭을 하면 빨간 점이 표시되고 좌표값이 list에 추가 된 후 저장하면 좌표값들이 CSV파일로 저장
    ### OR
    ### 2. 우클릭을 하고 드래그하면 선의 시작점이 시작되고 클릭이 해제되면 끝점이 설정되어 선이 그어짐
    ### 2-1. 이후 다시 우클릭을 하고 클릭을 해제하면 마지막점을 시작점으로 하여 다시 선을 그림
    ### 1과 마찬가지로 좌표값이 list에 추가 된 후 저장하면 좌표값들이 CSV파일로 저장

    def on_click(self, event):
            if self.image is None:
                return

            if event.button == 1: # 좌클릭
                if self.line_on == True: # 이미 선이 그려져 있는지 확인
                    result = QMessageBox.information(self, 
                                                     'Message', 
                                                     'The line has already been set.',
                                                     QMessageBox.Ok | QMessageBox.Cancel, 
                                                     QMessageBox.Ok)
                else:  
                    # 클릭한 위치에 빨간 점을 그림
                    self.ax.add_patch(
                        plt.Circle(
                            (event.xdata, event.ydata),
                            10,
                            color='red', fill = True)
                        )
                    self.list.append((event.xdata, event.ydata)) # 좌표 리스트에 추가
                    self.point_on = True
                    self.canvas.draw()

            else: # 우클릭
                if self.point_on == True: # 이미 점이 그려져 있는지 확인
                    result = QMessageBox.information(self, 
                                                     'Message', 
                                                     'The point has already been set.',
                                                     QMessageBox.Ok | QMessageBox.Cancel, 
                                                     QMessageBox.Ok)
                else:
                    if event.inaxes != self.ax:
                        return  
                    if self.next == False: # 드래그 시작 지점 설정
                        self.dragging = True
                        self.start_point = (event.xdata, event.ydata)
                        self.list.append((event.xdata, event.ydata))
            print(self.list)

    def on_drag(self,event):
        if self.image is None:
            return
        if self.next == True:
            return
        # 우클릭인 상태에서 시작점이 설정된 경우 다음 우클릭부턴 시작점이 따로 설정되지 않도록 설정 
        if event.button == 3 and self.dragging and self.next == False:
            self.next = True

    def on_release(self,event):
        if self.image is None:
            return
        if event.button == 1: # 좌클릭인 경우는 무시.
            return
        
        end_point = (event.xdata, event.ydata)
        self.list.append(end_point) # 끝 지점 좌표 추가
        self.ax.plot([self.start_point[0], end_point[0]], [self.start_point[1], end_point[1]], color='blue')
        self.canvas.draw()
        self.start_point = end_point #마지막점을 시작점으로 설정 
        self.next = True
        self.line_on = True

    
    def save(self):
        try:
            fname= self.file_name # 파일을 열때 가져왔던 file의 path를 변수 fname에 저장 
            data = self.list # 좌표값을 변수 data에 저장 
            with open(fname.replace('jpg','csv'),'w', encoding='UTF8', newline='') as f: # Path 정보로 파일을 쓰기 모드로 열기, 단 파일 이름은 불러온 jpg파일을 csv파일로 변경해서 열기
                writer = csv.writer(f)
                writer.writerows(data) # 좌표값 쓰기
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
            writer.writerows(data) # 좌표값 쓰기
            f.close()
         
        print("save as file is {}".format(fname)) # 저장 위치 출력 


    def clear(self):
        self.ax.clear()  
        self.ax.axis("off")
        self.list = []  # 좌표 리스트 초기화
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())