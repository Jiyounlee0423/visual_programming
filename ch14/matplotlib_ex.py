import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.image import imread

from PySide6.QtWidgets import (
        QApplication, QMainWindow, QVBoxLayout, 
        QWidget, QPushButton, QFileDialog, QMessageBox
        )

class InteractivePlot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.axis("off")

        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        layout.addWidget(self.canvas)
        layout.addWidget(self.load_button)

        self.dragging = False
        self.rect = None
        self.start_point = (0,0)
        self.click_count = 0
        self.image = None
        
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('motion_notify_event', self.on_drag)
        self.canvas.mpl_connect('button_release_event', self.on_release)

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self,
                                                   "Open Image",
                                                   "",
                                                   "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.image = imread(file_name)
            print(type(self.image))
            self.ax.clear()
            self.ax.imshow(self.image)
            self.ax.axis("on")
            self.canvas.draw()


    def on_click(self, event):
        if self.image is None:
            return
        if event.button == 3:
            self.on_right_click(event)
        else:
            if event.inaxes != self.ax:
                return
            self.dragging = True
            self.start_point = (event.xdata, event.ydata)
            self.rect = self.ax.add_patch(
                plt.Rectangle(self.start_point,
                              0,0,
                              fill=False, color='red')
            ) 
            self.canvas.draw()

    def on_right_click(self, event):
        if self.image is None:
            return
        if event.dblclick:
            self.ax.add_patch(
                plt.Circle(
                    (event.xdata, event.ydata),
                    10,
                    color='blue', fill=True
                )
            )
            self.canvas.draw()

    def on_drag(self, event):
        if self.image is None:
            return
        if not self.dragging or not event.inaxes:
            return
        if event.dblclick:
            return
        x0, y0 = self.start_point
        x1, y1 = event.xdata, event.ydata
        self.rect.set_width(x1 - x0)
        self.rect.set_height(y1 - y0)
        self.rect.set_xy((min(x0, x1), min(y0, y1)))
        self.canvas.draw()

    def on_release(self, event):
        if self.image is None:
            return
        if event.button == 3:
            return
        if self.dragging:
            self.dragging = False
            response = QMessageBox.question(self,
                                            "Confirm",
                                            "Keep the rectangle?",
                                            QMessageBox.Yes|QMessageBox.No)
        if response == QMessageBox.No:
            self.rect.remove()
        self.canvas.draw()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = InteractivePlot()
    mwd.show()
    sys.exit(app.exec())
