import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox, QFileDialog
from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Setup central widget and layout
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout()

        #setup Open File
        savelayout = QHBoxLayout()
        self.filebt = QPushButton("file open")
        self.filebt.clicked.connect(self.fileopen)
        savelayout.addWidget(self.filebt)
        self.savebt = QPushButton("save")
        self.savebt.clicked.connect(self.save)
        savelayout.addWidget(self.savebt)
        self.saveasbt = QPushButton("save as")
        self.saveasbt.clicked.connect(self.saveas)
        savelayout.addWidget(self.saveasbt)
        layout.addLayout(savelayout)

        # Setup QTextEdit
        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        # Setup search functionality
        self.searchLineEdit = QLineEdit()
        self.searchLineEdit.setPlaceholderText("Enter search text")
        self.searchButton = QPushButton("Search and Replace")
        self.searchButton.clicked.connect(self.searchAndReplace)
        searchLayout = QHBoxLayout()
        searchLayout.addWidget(self.searchLineEdit)
        searchLayout.addWidget(self.searchButton)
        layout.addLayout(searchLayout)

        # Setup replace functionality
        self.replaceFromLineEdit = QLineEdit()
        self.replaceFromLineEdit.setPlaceholderText("Replace from")
        self.replaceToLineEdit = QLineEdit()
        self.replaceToLineEdit.setPlaceholderText("Replace to")
        self.replaceButton = QPushButton("Replace All")
        self.replaceButton.clicked.connect(self.replaceAllText)
        replaceLayout = QHBoxLayout()
        replaceLayout.addWidget(self.replaceFromLineEdit)
        replaceLayout.addWidget(self.replaceToLineEdit)
        replaceLayout.addWidget(self.replaceButton)
        layout.addLayout(replaceLayout)

        container.setLayout(layout)
        self.setWindowTitle('Simple Notepad')
        self.setGeometry(300, 300, 600, 400)

    def fileopen(self):
        self.file_name, is_ok = QFileDialog.getOpenFileName(
               self,                 
               "open file",     
               "./",                   
               "txt files (*.txt, *.html, *.py);;all files(*.*)")
        
        with open(self.file_name[0], 'r', encoding='UTF8') as f: # Path 정보로 파일을 읽는다.
            data = f.read()
            self.textEdit.setText(data)

        
        
    def save(self):
        fname= self.file_name
        data = self.textEdit.toPlainText() 

        with open(fname[0],'w', encoding='UTF8') as f:
            f.write(data)
         
        print("save file is {}".format(fname[0]))

    def saveas(self):
        fname= QFileDialog.getSaveFileName(self) #파일 저장 위치 선택 요청
        data = self.textEdit.toPlainText() 

        with open(fname[0],'w', encoding='UTF8') as f:
            f.write(data)
         
        print("save as file is {}".format(fname[0]))


    def searchAndReplace(self):
        search_text = self.searchLineEdit.text()
        if search_text:
            self.highlightAndAskReplace(search_text)

    def replaceAllText(self):
        from_text = self.replaceFromLineEdit.text()
        to_text = self.replaceToLineEdit.text()
        if from_text and to_text:
            self.textEdit.setPlainText(self.textEdit.toPlainText().replace(from_text, to_text))
            QMessageBox.information(self, "Replace", f"All occurrences of '{from_text}' have been replaced with '{to_text}'.")

    def highlightAndAskReplace(self, text):
        cursor = QTextCursor(self.textEdit.document())
        format = QTextCharFormat()
        format.setBackground(QColor('yellow'))

        cursor.select(QTextCursor.Document)
        cursor.setCharFormat(QTextCharFormat())  # Reset format
        cursor.clearSelection()

        find_cursor = self.textEdit.document().find(text)
        while not find_cursor.isNull():
            find_cursor.mergeCharFormat(format)
            # Ask user if they want to replace this occurrence
            reply = QMessageBox.question(self, 'Replace Text',
                                         f"Do you want to replace '{text}'?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)

            if reply == QMessageBox.Yes:
                find_cursor.insertText(self.replaceToLineEdit.text())
            elif reply == QMessageBox.Cancel:
                break  # Stop the replace process
            find_cursor = self.textEdit.document().find(text, find_cursor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = View()
    ex.show()
    sys.exit(app.exec_())
