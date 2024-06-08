import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, 
    QVBoxLayout, QWidget, QFileDialog, QMenuBar, 
    QStatusBar)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Directory to QListWidget Example")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        menubar.setNativeMenuBar(False)

        open_action = QAction("Open Directory", self)
        open_action.triggered.connect(self.open_directory)
        file_menu.addAction(open_action)

        self.list_widget.itemClicked.connect(self.show_file_path)

        self.dir_path = None
        self.show()

    def open_directory(self):
        self.dir_path = QFileDialog.getExistingDirectory(self, "Select Directory")

        if self.dir_path:
            self.list_widget.clear()

            txt_files = [os.path.basename(f)
                         for f in os.listdir(self.dir_path)
                         if f.endswith('.txt')]
            
            for txt_file in txt_files:
                self.list_widget.addItem(txt_file)

    def show_file_path(self, item):
        f_path = os.path.join(self.dir_path, item.text())
        self.status_bar.showMessage(f_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())