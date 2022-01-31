from PyQt5 import Qt

from PyQt5.QtCore import QSize
from PyQt5.QtGui import  QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QFrame
from PyQt5 import QtCore


class QList_item(QFrame):
    def __init__(self, title, icon=None):
        super().__init__()
        self.title = title
        self.icon = icon
        self.layout = Qt.QHBoxLayout(self)
        self.setStyleSheet(""" QPushButton { background-color: #fff; border-bottom : 0px; margin : 0px 0px 0px 0px;
                                    padding : 0px 60px 0px 60px; text-align: left; letter-spacing: 0.5px; font-weight: bold;}  
                                    QPushButton::hover { background-color : rgba(61, 217, 245 , 0.8); } 
                               QHBoxLayout { padding: 0px 0px 0px 0px; margin: 0x 0px 0px 0px; } """)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumWidth(360)

        self.btn = Qt.QPushButton()
        self.btn.setMinimumHeight(25)
        self.btn.setText(str(self.title))
        if self.icon:
            self.Icon = QIcon()
            self.pix = QPixmap(str(self.icon))
            self.pix.scaled(QSize(13, 13))
            self.Icon.addPixmap(self.pix)
            self.btn.setIcon(self.Icon)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)


class QList_widget(QFrame):
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.layout = Qt.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setFixedWidth(360)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.initUI()


    def initUI(self):
        for i in self.items:
            self.layout.addWidget(QList_item(title=i["name"], icon=i["icon"]))
