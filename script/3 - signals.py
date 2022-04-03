from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys
from PyQt5.QtGui import QIcon


# 위젯 기본 클래스
class WindowExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)  # related QWidget (x,y,h) 창 크기 결정
        self.setWindowTitle("Beeary-VMI 채점")
        self.setWindowIcon(QIcon('../img/python.png'))

        self.create_buttons()

        #self.show()

    def create_buttons(self):
        btn1 = QPushButton("클릭하세요", self)
        #btn1.setText("두번째 텍스트")
        #btn1.move(200, 200) # 버튼 위치
        btn1.setGeometry(100, 100, 100, 100) # 버튼 위치 및 크기
        btn1.setIcon(QIcon("../img/python.png"))
        btn1.setStyleSheet('color:red') # 버튼 내 글자 색 바꾸기
        btn1.setStyleSheet('background-color:green')
        btn1.clicked.connect(self.clicked_btn)

        btn2 = QPushButton("두번째 클릭", self)
        btn2.setGeometry(200, 100, 100, 100)
        btn2.setStyleSheet('color:blue')
        btn2.clicked.connect(self.second_clicked)

    def clicked_btn(self):
        print("버튼1이 클릭되었습니다.")

    def second_clicked(self):
        print("버튼2가 클릭되었습니다.")



app = QApplication([])
window = WindowExample()
window.show()
sys.exit(app.exec_())