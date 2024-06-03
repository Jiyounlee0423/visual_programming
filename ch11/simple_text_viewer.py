import sys
from PySide6.QtWidgets import (QMainWindow, QFileDialog, QMessageBox, QApplication)

from viewer_outfile import Ui_MainWindow 

class MW(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Simple Text Viewer") # 메인 Window Title

        self.actionOpen.triggered.connect(self.open_file) # actionOpen instance의 trifferred signal을 처리할 self.open_file slot연결
        self.actionOpen.setShortcut('Ctrl+F') # actionOpen instance의 shortcut Key 설정
        self.actionSave.triggered.connect(self.save) # actionSave instance의 trifferred signal을 처리할 self.save slot연결
        self.actionSave.setShortcut('Ctrl+S') # actionSave instance의 shortcut Key 설정
        self.actionSave_as.triggered.connect(self.save_as) # actionSave_as instance의 trifferred signal을 처리할 self.save_as slot연결
        self.actionSave_as.setShortcut('Ctrl+Shift+S') # actionSave_as instance의 shortcut Key 설정
        self.actionClear.triggered.connect(self.clear) # actionClear instance의 trifferred signal을 처리할 self.clear slot연결
        self.actionClear.setShortcut('Ctrl+Del') # actionClear instance의 shortcut Key 설정

        self.textEdit.textChanged.connect(self.my_slot) #QTextEdit instance에서 사용자가 입력한 text가 변경될 때 self.my_slot slot 연결

        self.show()

    def open_file(self):
        # QFileDialg를 사용하여 파일선택 다이알로그를 띄움
        self.file_name, is_ok = QFileDialog.getOpenFileName(
               self,                 
               "open file",     
               "./",                   
               "txt files (*.txt)")
        
        with open(self.file_name, 'r', encoding='UTF8') as f: # Path 정보로 파일을 읽기 모드로 열기 
            data = f.read() # 파일을 읽어와 변수 data에 저장 
            self.textEdit.setPlainText(data) # data를 순수한 text로 취급하여 QTextEdit의 content로 설정하여 보여줌  

        name = self.file_name.split("/") # 파일 경로를 /로 구분
        self.label.setText(f"파일 명: {name[-1]}") # 구분된 파일경로의 마지막 부분 = 파일 이름

        number = len(self.textEdit.toPlainText()) # QTextEdit의 content의 내용을 plain text로 반환하여 글자수 계산 
        self.statusbar.showMessage(f"글자 수: {number}") # status bar에 글자수 표시
    
    def save(self):
        try:
            fname= self.file_name # 파일을 열때 가져왔던 file의 path를 변수 fname에 저장 
            data = self.textEdit.toPlainText() # QTextEdit의 content의 내용을 plain text로 반환하여 변수 data에 저장 
            with open(fname,'w', encoding='UTF8') as f: # Path 정보로 파일을 쓰기 모드로 열기 
                f.write(data) #  QTextEdit의 content의 내용을 plain text로 반환하여 변수 data의 내용을 작성 

            print("save file is {}".format(fname))  # 저장 위치 출력 
            number = len(self.textEdit.toPlainText()) # QTextEdit의 content의 내용을 plain text로 반환하여 글자수 계산 
            self.statusbar.showMessage(f"글자 수: {number} save file") # status bar에 글자수와 저장 완료 표시
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
        data = self.textEdit.toPlainText() # QTextEdit의 content의 내용을 plain text로 반환하여 변수 data에 저장 

        with open(fname,'w', encoding='UTF8') as f: # Path 정보로 파일을 읽기모드로 열기
            f.write(data) #  QTextEdit의 content의 내용을 plain text로 반환하여 변수 data의 내용을 작성 
         
        print("save as file is {}".format(fname)) # 저장 위치 출력 
        number = len(self.textEdit.toPlainText()) # QTextEdit의 content의 내용을 plain text로 반환하여 글자수 계산 
        self.statusbar.showMessage(f"글자 수: {number} save file") # status bar에 글자수와 저장 완료 표시

    def clear(self):
        self.textEdit.clear() # QTextEdit의 현재 content를 다 지움 

    def my_slot(self):
        number = len(self.textEdit.toPlainText()) # QTextEdit의 content의 내용을 plain text로 반환하여 글자수 계산 
        self.statusbar.showMessage(f"글자 수: {number}") # status bar에 글자수 표시

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())