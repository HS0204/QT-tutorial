from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("../ui/mybutton.ui", self)

        # ui 내 위젯 찾기
        button = self.findChild(QPushButton, 'pushButton') # ui XML 내 name 찾아서 입력
        button.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        print("0점으로 채점되었습니다.")


app = QApplication([])
window = UI()
window.show()
app.exec_()