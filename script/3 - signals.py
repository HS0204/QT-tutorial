from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QIcon


# 위젯 기본 클래스
class WindowExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)  # related QWidget (x,y,h) 창 크기 결정
        self.show()


app = QApplication([])
window = WindowExample()
sys.exit(app.exec_())