import os, sys
sys.path.insert(0, os.path.abspath("."))

from PyQt5 import Qt, QtCore

import sys
import threading
import psutil
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect, QWidget, QListWidget, QListView
from icon_button import QIcon_Button
from option_input import QInput, QFourInputs, QTwoInputs, QCheckInput


class NavBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(50)
        self.setFixedWidth(330)
        self.layout = Qt.QHBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.btn =  QIcon_Button(icon="angle-left.png", toolTip="Назад")
        self.btn2 = QIcon_Button(icon="angle-right.png", toolTip="Вперед")
        self.btn3 = QIcon_Button(icon="folder.png", toolTip="Сохранить")

        self.setContentsMargins(4, 0, 4, 0)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)

class Options_list(QFrame):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.layout = Qt.QVBoxLayout()

            self.input1 = QInput("background-color:")
            self.input2 = QFourInputs("margin:")
            self.input3 = QTwoInputs("size - ", "width:", "height:")
            self.input4 = QCheckInput("show:")
            self.setContentsMargins(0, 0, 0, 0)
            self.layout.addWidget(self.input1)
            self.layout.addWidget(self.input2)
            self.layout.addWidget(self.input3)

            self.layout.addWidget(self.input4)

            self.setLayout(self.layout)


class Options_menu(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.options = []
        self.navbar = NavBar()
        self.o_list = Options_list()
        self.setStyleSheet("background-color: #fffaff; border-radius: 3px 3px 3px 3px;")
        self.setFixedHeight(400)
        self.setFixedWidth(330)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout = Qt.QVBoxLayout(self)
        self.layout.setAlignment( QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)

        self.layout.addWidget(self.navbar)
        self.layout.addWidget(self.o_list)

        self.setLayout(self.layout)
        
        
        

    def save_style(self):
        return 

    def on_backward(self):
        return

    def on_forward(self):
        return         
        
        

class Options(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(340, 1200)
        self.o_menu = Options_menu()
        
        self.gray_palette = self.palette()
        self.gray_palette.setColor(QPalette.Window, QColor(50, 50, 50))
        
        self.setPalette(self.gray_palette)
        self.setContentsMargins(5, 5, 5, 5)
        layout = Qt.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignTop)

        layout2 = Qt.QVBoxLayout(self)
        layout3 = Qt.QVBoxLayout(self)
        layout.addWidget(self.o_menu)
    
        layout2.addLayout(layout)
        layout2.addLayout(layout3)
        self.setLayout(layout2)
        





        


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = Options()
    w.show()
    sys.exit(app.exec_())       