from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QMainWindow
import sys
from PyQt5.QtGui import QIcon
"""
QWidget 확장/축소 가능 -> BASIC | 모든 위젯
QDialog 확장/축소 불가능 -> 유저 간 커뮤니케이션(알림) 등에서 사용
QMainWindow 확장/축소 가능 ->
"""

# 위젯 기본 클래스
class WindowExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)  # related QWidget (x,y,h) 창 크기 결정
        self.setWindowTitle("Beeary-VMI 채점")
        self.setWindowIcon(QIcon('../img/python.png'))

        #self.setFixedHeight(400) # 강제 사이즈 고정
        #self.setFixedWidth(300)

        #self.setWindowOpacity(0.5)
        self.setStyleSheet('background-color:green')

        self.show()


app = QApplication([])
window = WindowExample()
sys.exit(app.exec_())