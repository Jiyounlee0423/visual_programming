import psutil
import sys, os
import random
import time

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QInputDialog
)
from PySide6.QtCore import QTimer

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
matplotlib.use('QtAgg') # matplotlib을 QtAgg 백엔드로 사용하도록 설정

# 사용자 정의 캔버스 클래스 정의
class MyCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, figsize =(5,5), dpi=100):
        # Figure 및 Axes 생성
        self.fig, self.axes = plt.subplots(
            1,2,
            figsize=figsize, 
            dpi=dpi
        )
        super(MyCanvas, self).__init__(self.fig)

# 메인 윈도우 클래스 정의
class MW(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("CPU & RAM")  # 윈도우 타이틀 설정

        self.plt_canvas = MyCanvas(self, (500,10), 100) #MyCanvas 객체 생성

         # CPU 및 RAM 데이터 및 시간 데이터 저장을 위한 리스트 초기화
        self.cpu = []
        self.time_cpu = []
        self.ram = []
        self.time_ram = []

        # 사용자 입력 다이얼로그를 통해 갱신 간격 설정

        ret_int, is_ok = QInputDialog.getInt( # 사용자로 부터 정수 입력을 받는 modal dialog
            self,  # 부모 widget
            "Interval_ms",      # dialog title
            "Enter Yout Int Value!",            # input field위의 label text
            1,         # 기본 text값.
            1, 100, # min and max
            1, #step
        )


        self.interval_ms = ret_int

        self.setCentralWidget(self.plt_canvas) #생성한 self.plt_canvas를 MainWindow의 CentralWidget으로 설정
        self.show() #window 보이기

        # CPU 및 RAM 데이터 갱신을 위한 타이머 설정
        self.timer0 = QTimer() #QTimer 객체 생성
        self.timer0.setInterval(self.interval_ms) #QTimer interval 설정(ms단위)
        self.timer0.timeout.connect(self.update_cpu) #매 interval 마다 self.update_cpu 실행
        self.timer0.start() #QTimer가 시간 체크 시작

        self.timer1 = QTimer() #QTimer 객체 생성
        self.timer1.setInterval(self.interval_ms) #QTimer interval 설정(ms단위)
        self.timer1.timeout.connect(self.update_ram) #매 interval 마다 self.update_ram 실행
        self.timer1.start() #QTimer가 시간 체크 시작


        

    def update_cpu(self):
        # CPU 사용량 및 시간 정보 업데이트
        self.cpu_value = psutil.cpu_percent(interval=1) #CPU 사용률을 백분율로 리턴해줌
        print(self.cpu_value)
        self.time_cpu_value = time.strftime('%M:%S') #입력받은 struct_time을 포맷에 지정된 문자열로 변환 후 반환, 분:초
        print(self.time_cpu_value)

        # CPU 데이터를 리스트에 추가
        self.cpu.append(self.cpu_value)
        self.time_cpu.append(self.time_cpu_value)

        # CPU 그래프 업데이트
        self.plt_canvas.axes[0].cla() #좌표평면의 제외한 그래프의 figure을 지움
        if (len(self.cpu) >= 10): # 가져온 CPU 데이터의 갯수가 10개 이상이면
            self.plt_canvas.axes[0].plot(
                    self.time_cpu[-10:], self.cpu[-10:], 
                    label='CPU',
                )[0] #최근 10개의 데이터를 그래프로 그림
        else:
            if (len(self.cpu) >= 2): # 가져온 CPU 데이터의 갯수가 2개 이상 10개 미만이면
                self.plt_canvas.axes[0].plot(
                        self.time_cpu, self.cpu, 
                        label='CPU',
                    )[0] #가져온 데이터의 갯수만큼 데이터를 그림
        self.plt_canvas.axes[0].grid() #격자설정
        self.plt_canvas.axes[0].legend(loc='upper right') #그래프 범례 표시
        self.plt_canvas.draw() # 그래프 그리기




    def update_ram(self):
        # RAM 사용량 및 시간 정보 업데이트
        self.ram_value = psutil.virtual_memory() #시스템 메모리 사용량을 여러 항목(total,used 등)을 바이트 단위로 리턴
        self.used_ram = self.ram_value.used / (1024 * 1024) # 메모리 사용량을 MB 단위로 변환, used: 사용되는 메모리
        self.time_ram_value = time.strftime('%M:%S')  #입력받은 struct_time을 포맷에 지정된 문자열로 변환 후 반환, 분:초

        # RAM 데이터를 리스트에 추가
        self.ram.append(self.used_ram)
        self.time_ram.append(self.time_ram_value)

        # RAM 그래프 업데이트
        self.plt_canvas.axes[1].cla() #좌표평면의 제외한 그래프의 figure을 지움
        if (len(self.ram) >= 10): # 가져온 RAM 데이터의 갯수가 10개 이상이면
            self.plt_canvas.axes[1].plot(
                    self.time_ram[-10:], self.ram[-10:], 
                    label='RAM',
                )[0] #최근 10개의 데이터를 그래프로 그림
        else:
            if (len(self.cpu) >= 2): # 가져온 CPU 데이터의 갯수가 2개 이상 10개 미만이면
                self.plt_canvas.axes[1].plot(
                        self.time_ram, self.ram, 
                        label='RAM',
                    )[0] #가져온 데이터의 갯수만큼 데이터를 그림
        self.plt_canvas.axes[1].grid() #격자설정
        self.plt_canvas.axes[1].legend(loc='upper right') #그래프 범례 표시
        self.plt_canvas.draw() # 그래프 그리기


if __name__ == "__main__":
    app = QApplication()
    wnd = MW()
    sys.exit(app.exec())

