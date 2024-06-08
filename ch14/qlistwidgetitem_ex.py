import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget,
    QListWidgetItem, 
    QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QMenuBar, 
    QStatusBar)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.image as mpimg

class ImageCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
        self.setStyleSheet("background-color: #2f2f2f;")
        self.ax.axis("off")
        self.fig.subplots_adjust(
            left=0, right=1,
            top=1, bottom=0
        )

    def display_image(self, image_path):
        self.ax.clear()
        img = mpimg.imread(image_path)
        self.ax.imshow(img)
        self.ax.axis("off")
        self.fig.subplots_adjust(
            left=0, right=1,
            top=1, bottom=0
        )
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PNG Viewer")

        main_layout = QHBoxLayout()
        central_Widget = QWidget()
        central_Widget.setLayout(main_layout)
        self.setCentralWidget(central_Widget)

        right_layout = QVBoxLayout()
        right_Widget = QWidget()
        right_Widget.setLayout(right_layout)

        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        main_layout.addWidget(self.list_widget)

        self.canvas = ImageCanvas(self)

        self.nav_toolbar = NavigationToolbar(self.canvas, self)

        right_layout.addWidget(self.nav_toolbar)
        right_layout.addWidget(self.canvas)

        main_layout.addWidget(right_Widget)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("Select img Dir")
        menubar.setNativeMenuBar(False)

        open_action = QAction("Open Directory", self)
        open_action.triggered.connect(self.open_directory)
        file_menu.addAction(open_action)

        self.show()
    
    def open_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.list_widget.clear()
            jpg_files = [f for f in os.listdir(directory) if f.endswith(".jpg")]
            for jpg_file in jpg_files:
                item = QListWidgetItem(jpg_file)
                item.setData(Qt.UserRole, os.path.join(directory, jpg_file))
                self.list_widget.addItem(item)

    def on_item_clicked(self, item):
        file_path = item.data(Qt.UserRole)
        self.canvas.display_image(file_path)
        self.status_bar.showMessage(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())