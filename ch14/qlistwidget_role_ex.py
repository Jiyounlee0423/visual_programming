import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, 
    QListWidgetItem, QVBoxLayout, QWidget, 
    QStatusBar, QPushButton, QWhatsThis,
)
from PySide6.QtGui import QFont, QColor, QIcon
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget Roles Example")

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.whats_this_button = QPushButton("What's This?")
        self.whats_this_button.clicked.connect(self.toggle_whats_this_mode)
        layout.addWidget(self.whats_this_button)

        self.edit_button = QPushButton("Edit Item")
        self.edit_button.clicked.connect(self.edit_selected_item)
        layout.addWidget(self.edit_button)

        item1 = QListWidgetItem("Display Role Text 1")
        item1.setData(Qt.DisplayRole, "Updated Display Role Text 1")
        item1.setData(Qt.ToolTipRole, "ToolTip Role Text 1")
        item1.setData(Qt.StatusTipRole, "StatusTip Role Text 1")
        item1.setData(Qt.WhatsThisRole, "What's This Role Text 1")

        font1 = QFont("Arial", 12, QFont.Bold)
        item1.setData(Qt.FontRole, font1)

        item1.setData(Qt.TextAlignmentRole, Qt.AlignCenter)

        background_color1 = QColor(Qt.yellow)
        item1.setData(Qt.BackgroundRole, background_color1)

        foreground_color1 = QColor(Qt.red)
        item1.setData(Qt.ForegroundRole, foreground_color1)

        item1.setData(Qt.CheckStateRole, Qt.Checked)

        icon1 = QIcon("C:\visual_programming\ch11\img\save_file.png")
        item1.setData(Qt.DecorationRole, icon1)

        self.list_widget.addItem(item1)

        item2 = QListWidgetItem("Display Role Text 2")
        item2.setData(Qt.DisplayRole, "Updated Display Role Text 2")
        item2.setData(Qt.ToolTipRole, "ToolTip Role Text 2")
        item2.setData(Qt.StatusTipRole, "StatusTip Role Text 2")
        item2.setData(Qt.WhatsThisRole, "What's This Role Text 2")

        font2 = QFont("Times New Roman", 10)
        item2.setData(Qt.FontRole, font2)

        item1.setData(Qt.TextAlignmentRole, Qt.AlignCenter)

        background_color2 = QColor(Qt.green)
        item2.setData(Qt.BackgroundRole, background_color2)

        foreground_color2 = QColor(Qt.blue)
        item2.setData(Qt.ForegroundRole, foreground_color2)

        item2.setData(Qt.CheckStateRole, Qt.Checked)

        icon2 = QIcon("C:\visual_programming\ch11\img\open_file.png")
        item2.setData(Qt.DecorationRole, icon2)

        self.list_widget.addItem(item2)

        self.list_widget.itemEntered.connect(self.show_status_tip)

        self.list_widget.setMouseTracking(True)

    def toggle_whats_this_mode(self):
        if QWhatsThis.inWhatsThisMode():
            QWhatsThis.leaveWhatsThisMode()
        else:
            QWhatsThis.enterWhatsThisMode()

    def show_status_tip(self, item):
        status_tip = item.data(Qt.StatusTipRole)
        self.status_bar.showMessage(status_tip)

    def edit_selected_item(self):
        current_item = self.list_widget.currentItem()
        current_item.setFlags(current_item.flags() | Qt.ItemIsEditable)

        if current_item:
            self.list_widget.editItem(current_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
