import psutil
import sys
import random
import time

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication
)
from PySide6.QtCore import QTimer

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
matplotlib.use('QtAgg')

class MyCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, figsize =(5,5), dpi=100):

        self.fig, self.axes = plt.subplots(
            1,2,
            figsize=figsize, 
            dpi=dpi
        )
        super(MyCanvas, self).__init__(self.fig)

class MW(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("CPU & RAM")

        self.plt_canvas = MyCanvas(self, (5,10), 100)


        self.interval_ms = 10

        #self.cpu = psutil.cpu_percent(interval=1)
        #self.ram = psutil.virtual_memory()
        self.old_plot_ref_cpu = None
        self.update_cpu()
        self.old_plot_ref_ram = None
        self.update_ram()

        self.setCentralWidget(self.plt_canvas)
        self.show()

        self.timer0 = QTimer()
        self.timer0.setInterval(self.interval_ms)
        self.timer0.timeout.connect(self.update_cpu)
        self.timer0.start()

        self.timer1 = QTimer()
        self.timer1.setInterval(self.interval_ms)
        self.timer1.timeout.connect(self.update_ram)
        self.timer1.start()


        

    def update_cpu(self):

        self.cpu = []
        self.time_cpu = []

        # self.cpu_value = psutil.cpu_percent(interval=1)
        # print(self.cpu_value)
        # self.time_cpu_value = time.time()
        # print(self.time_cpu_value)

        # self.cpu.append(self.cpu_value)
        # print(self.cpu)
        # self.time_cpu.append(self.time_cpu_value)

        # if self.old_plot_ref_cpu is not None:
        #     self.old_plot_ref_cpu.set_ydata(self.time_cpu)
        # else: 
        #     self.old_plot_ref_cpu = self.plt_canvas.axes[0].plot(
        #         self.time_cpu, self.cpu, 
        #         label='CPU',
        #     )[0]
        #     #self.plt_canvas.axes[0].plot([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10])
        #     self.plt_canvas.axes[0].grid()
        #     #self.plt_canvas.axes[0].legend(loc='upper right')
        # self.plt_canvas.draw()
        count = 0
        while (count < self.interval_ms):
             self.cpu_value = psutil.cpu_percent(interval=1)
             print(self.cpu_value)
             self.time_cpu_value = time.time()
             print(self.time_cpu_value)

             self.cpu.append(self.cpu_value)
             print(self.cpu)
             self.time_cpu.append(self.time_cpu_value)

             self.plt_canvas.axes[0].cla()
             self.plt_canvas.axes[0].plot(self.time_cpu, self.cpu, label='method0')
             #self.plt_canvas.axes[0].plot([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10])
             self.plt_canvas.axes[0].grid()
             #self.plt_canvas.axes[0].legend(loc='upper right')
             self.plt_canvas.draw()
             #self.plt_canvas.pause(self.interval_ms)
             count += 1

            


    def update_ram(self):
        self.ram = []
        self.time_ram = []

        count = 0
        while (count < self.interval_ms):
            self.ram_value = psutil.virtual_memory()
            self.used_ram = self.ram_value.used / (1024 * 1024) # 메모리 사용량을 MB 단위로 변환
            self.time_ram_value = time.time()

            self.ram.append(self.used_ram)
            self.time_ram.append(self.time_ram_value)

            self.plt_canvas.axes[1].cla()
            self.plt_canvas.axes[1].plot(self.time_ram, self.ram, label='method0')
            #self.plt_canvas.axes[1].plot([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10])
            self.plt_canvas.axes[1].grid()
            #self.plt_canvas.axes[1].legend(loc='upper right')
            self.plt_canvas.draw()
            count += 1

if __name__ == "__main__":
    app = QApplication()
    wnd = MW()
    sys.exit(app.exec())

# # CPU 사용량 조회
# cpu_usage = psutil.cpu_percent(interval=1)
# print(f"CPU Usage: {cpu_usage}%")

# # 메모리 사용량 조회
# memory_usage = psutil.virtual_memory()
# print(f"Memory Usage: {memory_usage.percent}%")

# # 디스크 사용량 조회
# disk_usage = psutil.disk_usage('/')
# print(f"Disk Usage: {disk_usage.percent}%")

# # 네트워크 정보 조회
# net_io = psutil.net_io_counters()
# print(f"Bytes Sent: {net_io.bytes_sent}")
# print(f"Bytes Received: {net_io.bytes_recv}")
