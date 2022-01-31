import sys

from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QLabel, QFrame, QApplication
import ctypes


class QNav_Menu(QFrame):
    def __init__(self):
        super().__init__()

        self.layout = Qt.QHBoxLayout(self)
        self.btn1 = Qt.QPushButton("")
        self.btn2 = Qt.QPushButton("")
        self.btn1.setStyleSheet(""" QPushButton { border: 0px; background-color : #fff; margin : 5px 0px 0px 6px; border-radius : 5px 5px 5px 5px; } """)
        self.btn2.setStyleSheet(""" QPushButton { border: 0px; background-color : #fff; margin : 5px 0px 0px 6px; border-radius : 5px 5px 5px 5px; } """)
        
        self.btn1.setFixedHeight(30)
        self.btn1.setFixedWidth(50)

        self.btn2.setFixedHeight(30)
        self.btn2.setFixedWidth(50)

        self.Icon1 = QIcon()
        self.pix = QPixmap("caret-r.png")
        self.pix.scaled(QSize(16, 16))
        self.Icon1.addPixmap(self.pix)

        self.Icon2 = QIcon()
        self.pix = QPixmap("stop.png")
        self.pix.scaled(QSize(16, 16))
        self.Icon2.addPixmap(self.pix)

        self.btn2.setIcon(self.Icon2)
        self.btn1.setIcon(self.Icon1)

        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)

        self.btn1.setFixedWidth(50)
        self.btn2.setFixedWidth(50)

        self.cursor_pix = QPixmap('cursor-dark2.png')
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(18, 18), QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.btn1.setCursor(self.current_cursor)
        self.btn2.setCursor(self.current_cursor)

        self.setStyleSheet(""" QFrame { background-color: rgba(230, 230, 230, 0.6); border-radius: 6px 6px 6px 6px; }  
        QPushButton::hover { background : rgba(160, 160, 160, 1); color : #fff; } """)

        self.setFixedWidth(400)
        self.setFixedHeight(46)
        self.layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

class QNavBar(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.setStyleSheet(""" QFrame { background-color: rgba(20, 20, 20, 0.2); } """)


        self.btn_list = QNav_Menu()
        self.layout.addWidget(self.btn_list)
        self.setLayout(self.layout)
        self.setFixedHeight(54)

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QNavBar()
    w.show()
    sys.exit(app.exec_())