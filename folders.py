from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from title import Title
from icon_button import QIcon_Button
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor,  QPixmap, QIcon
from PyQt5.QtCore import QThread,  QSize

class Tab(Qt.QFrame):
    def __init__(self, title, icon=None):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.title = title
        self.icon = icon

        self.btn =  QtWidgets.QPushButton()
        self.Icon = QIcon()
        self.pix = QPixmap(str(self.icon))
        self.pix.scaled(QSize(13, 13))
        self.Icon.addPixmap(self.pix)   
        self.btn.setIcon(str(self.Icon))
        
        self.btn.setMinimumHeight(20)
        self.btn.setMinimumWidth(180)
        self.setMinimumWidth(180)
        self.setMinimumHeight(21)
        self.btn.setMaximumWidth(210)
        self.btn.setMinimumWidth(170)

        self.icon_btn = QIcon_Button("left-a.png")
        self.layout.addWidget(self.icon_btn)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)
        

class Folder_list(Qt.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.setContentsMargins(0, 0, 0, 0)
        


class Folders(Qt.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self) 
        self.setContentsMargins(0, 0, 0, 0)

        self.s