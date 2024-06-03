from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import (
        QApplication, QLabel, 
        QPushButton, QVBoxLayout, QWidget,
        )
import time, sys, os

class WorkerThread(QThread):
    update_signal = Signal(str)

    def run(self):
        for i in range(5):
            time.sleep(1)
            self.update_signal.emit(f"Working {i+1}")

        self.update_signal.emit("Taxk completed!")

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.label = QLabel("Thread Example",self)
        self.button = QPushButton("Start Thread", self)
        self.button.clicked.connect(self.start_thread)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.worker = WorkerThread()
        self.worker.update_signal.connect(self.update_label)

    def start_thread(self):
        if not self.worker.isRunning():
            self.worker.start()

    def update_label(self,message):
        self.label.setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())