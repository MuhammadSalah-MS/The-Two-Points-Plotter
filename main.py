from PySide6.QtWidgets import QApplication,QPushButton
from mainwindow import MainWindow
import sys
from PySide6.QtGui import QAction,QIcon

app = QApplication(sys.argv)
w = MainWindow()

w.show()
app.exec_()
