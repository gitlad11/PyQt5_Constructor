
from PyQt5 import Qt, QtCore

import sys

from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect, QWidget, QListWidget, QListView
from option_input import QInput, QFourInputs, QTwoInputs, QCheckInput
from icon_button import QIcon_Button

class QMenuTab(QWidget):
    def __init__(self, title, icon=None):
        super().__init__()
        self.title = title
        self.icon = icon
        self.active = True

        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("border: 1px 1px 0px 0px;")
        self.resize(300, 22)
        self.setWindowOpacity(0.6)

        self.layout = Qt.QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.Icon = QIcon()
        self.pix = QPixmap('left-a.png')
        self.pix.scaled(QSize(13, 13))
        self.Icon.addPixmap(self.pix)
        self.btn = Qt.QPushButton('')
        self.btn.clicked.connect(self.on_active)
        self.btn.setText(str(self.title))
        self.btn.setFont(QFont("Helvetica", 11))

    
        self.btn.setFixedWidth(300)
        self.btn.setStyleSheet("color: #fff; background-color: rgba(40, 40, 40, 1); letter-spacing: 1px; border-bottom: 1px solid gray; padding: 5px, 5px, 5px, 5px; text-align: left; ")
        self.btn.setIcon(self.Icon)
        self.btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.layout.addWidget(self.btn)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

    def event(self, e):
        if e.type() == QtCore.QEvent.Enter:
            self.btn.setStyleSheet(
                  "background-color: rgba(100, 100, 100, 1); color: #fff; letter-spacing: 1px; border-bottom: 1px solid gray; padding: 5px, 5px, 5px, 5px; text-align: left;")
        elif e.type() == QtCore.QEvent.Leave:
            self.btn.setStyleSheet(
                "color: #000; background-color: rgba(255, 255, 255, 1); letter-spacing: 1px; border-bottom: 1px solid gray; padding: 5px, 5px, 5px, 5px; text-align: left;")

        return QWidget.event(self, e)

    def on_active(self):
            if self.active:
                self.pix = QPixmap('left-a.png')
                self.pix.scaled(QSize(19, 19))
                self.Icon.addPixmap(self.pix)
                self.btn.setIcon(self.Icon)
                self.active = False
            else:
                self.pix = QPixmap('down-a.png')
                self.pix.scaled(QSize(19, 19))
                self.Icon.addPixmap(self.pix)
                self.btn.setIcon(self.Icon)
                self.active = True    


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
        self.o_list = QMenuOption()
        self.setStyleSheet("background-color: #ECE1F8; border-radius: 3px 3px 3px 3px;")
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


class QMenuOption(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tab = QMenuTab("background")
        self.menu = Options_menu()
        self.layout = Qt.QVBoxLayout(self)
       
        self.layout.addWidget(self.tab)
        self.layout.addWidget(self.menu)
        self.setLayout(self.layout)       