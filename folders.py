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
        self.btn.setIcon(self.Icon)
        self.btn.setText(str(self.title))

        self.btn.setMinimumHeight(20)
        self.btn.setMinimumWidth(180)
        self.setMinimumWidth(180)
        self.setMinimumHeight(21)
  
        self.setStyleSheet(""" QFrame { background-color: rgba(10, 10, 10, 0);  } QPushButton { 
            background-color: rgba(10, 10, 10, 0); 
            font: 75 9pt "Microsoft YaHei UI";
            font-weight: bold;
            color: #fff;
            padding: 0px 4px 5px 5px;
            text-align: left;
            } """)

        
        self.icon_btn = QIcon_Button("left-a.png")
        self.layout.addWidget(self.icon_btn)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)
        

class Folder_list(Qt.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.setContentsMargins(0, 0, 0, 0)
        self.tab = Tab( title="folder", icon="folder-dir.png")
        self.tab2 = Tab(title="folder 2", icon="folder-dir.png")
        self.setMinimumHeight(200)
        self.setFixedWidth(180)
        self.layout.addWidget(self.tab)
        self.layout.addWidget(self.tab2)
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)


class Folders(Qt.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self) 
        self.setContentsMargins(0, 0, 0, 0)
        self.list = Folder_list()

        self.setMinimumHeight(200)
        self.setFixedWidth(180)

        self.layout.addWidget(self.list)
        self.setLayout(self.layout)
        