import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget() # 위젯의 기본
window.show()

app.exec_()