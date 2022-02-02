from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from title import Title
from icon_button import QIcon_Button
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor,  QPixmap, QIcon
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import QThread,  QSize
import os

class Tab_items(Qt.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.setStyleSheet(""" QFrame { border-bottom: 1px solid gray; border-left: 1px solid gray; }""")
        self.setMinimumHeight(1)
        self.setLayout(self.layout)        
        

class Tab_btn(Qt.QFrame):
    def __init__(self, title, icon=None, type=None, on_tab_click=None):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.title = title
        self.icon = icon
        self.type = type
        self.on_tab_click = on_tab_click
        self.active = True

        self.btn =  QtWidgets.QPushButton()
        self.Icon = QIcon()
        self.pix = QPixmap(str(self.icon))
        self.pix.scaled(QSize(13, 13))
        self.Icon.addPixmap(self.pix)   
        self.btn.setIcon(self.Icon)
        self.btn.setText(str(self.title))

        self.items = Tab_items()
        
        self.btn.setFixedHeight(30)
        self.btn.setMinimumWidth(220)
        self.setContentsMargins(0, 0, 0, 0)
        self.setMinimumWidth(220)
        self.setFixedHeight(34)

        self.setStyleSheet(""" QFrame { background-color: rgba(10, 10, 10, 0);  } QPushButton { 
            background-color: rgba(10, 10, 10, 0); 
            font: 75 9pt "Microsoft YaHei UI";
            font-weight: bold;
            color: #fff;
            padding: 0px 0px 5px 0px;
            text-align: left;
            margin: 0px 0px 0px 0px;

            } """)

        if self.type == "folder":
            self.icon_btn = QIcon_Button("left-a.png")
            self.layout.addWidget(self.icon_btn)
            self.btn.clicked.connect(self.on_active)
        
        self.layout.addWidget(self.btn)
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)

        self.cursor_pix = QPixmap('cursor-dark2.png')  
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(18, 18), QtCore.Qt.KeepAspectRatio) 
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.setCursor(self.current_cursor)
        
    def event(self, e):
        if e.type() == QtCore.QEvent.Enter:
             self.setStyleSheet(""" QFrame { background-color: rgba(150, 150, 150, 0.2);  } QPushButton { 
           background-color: rgba(10, 10, 10, 0);  
            font: 75 9pt "Microsoft YaHei UI";
            font-weight: bold;
            color: #fff;
            padding: 0px 0px 5px 0px;
            margin: 0px 0px 0px 0px;
            text-align: left;
            } """)
            
        elif e.type() == QtCore.QEvent.Leave:
             self.setStyleSheet(""" QFrame { background-color: rgba(10, 10, 10, 0);  } QPushButton { 
            background-color: rgba(10, 10, 10, 0); 
            font: 75 9pt "Microsoft YaHei UI";
            font-weight: bold;
            color: #fff;
            padding: 0px 0px 5px 0px;
            margin: 0px 0px 0px 0px;
            text-align: left;
        
            } """)
        elif e.type() == QtCore.QEvent.MouseButtonPress:
            if self.type == "folder":
                print('folder')
                self.on_active()    

        return QWidget.event(self, e)

    def on_active(self):
        
        if self.active:
            self.layout.itemAt(0).widget().deleteLater()
            icon_btn = QIcon_Button("down-a.png")
            self.layout.insertWidget(0, icon_btn)
            self.active = False
            
        else:
            self.layout.itemAt(0).widget().deleteLater()
            icon_btn = QIcon_Button("left-a.png")
            self.layout.insertWidget(0, icon_btn)
            self.active = True

        self.on_tab_click(self.active)    
        

class Tab(Qt.QFrame):
    def __init__(self, title, icon=None, type=None, on_tab_open=None, on_tab_close=None):
        super().__init__()
        self.title = title
        self.icon = icon
        self.type = type
        self.on_tab_open = on_tab_open
        self.on_tab_close = on_tab_close
        self.active = True
        

        self.layout = Qt.QVBoxLayout(self)
        self.tab_btn = Tab_btn(title=self.title, icon=self.icon, type=self.type, on_tab_click = self.on_tab_click)
        self.tab_items = Tab_items()
        self.setContentsMargins(0, 0, 0, 0)
        
        self.layout.addWidget(self.tab_btn)


        self.setStyleSheet(""" QFrame { margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; } """)
        self.setMinimumHeight(44)
        self.setMinimumWidth(220)
        
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def on_tab_click(self, active):
        if active:
           self.on_tab_open(height=1000)
        else : 
            self.on_tab_close(height=1000)    


class Folder_list(Qt.QFrame):
    def __init__(self, dir):
        super().__init__()
        self.height = 200
        self.dir = dir
        self.layout = Qt.QVBoxLayout(self)
        self.setContentsMargins(0, 0, 0, 0)
        self.extensions_image = ['img', 'jpeg', 'web', 'png', 'favicon']
        self.extensions_files = ['py', 'cpp', 'js', 'txt', 'json', ]
        self.setMinimumHeight(200)


        self.setFixedWidth(220)

        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
            list = os.listdir(self.dir)
            for i in list:
                self.height += 44
                splited = i.split('.')
                print(splited)
                if len(splited) > 1 and splited[1] in self.extensions_files:
                    item = Tab(title=i, icon="script-dir.png", type="file")
                    self.layout.addWidget(item)
                elif len(splited) > 1 and splited[1] in self.extensions_image:
                    item = Tab(title=i, icon="script-dir.png", type="image")
                    self.layout.addWidget(item)
                elif os.path.isdir(i):
                    second_item = Tab(title=i, icon="folder-dir.png", type="folder")  
                    self.layout.addWidget(second_item)   
            
            self.setFixedHeight(self.height)   

    def on_open_tab_size(self, height):
        self.height += height
        print(self.height)
        self.setFixedHeight(self.height)   

    def on_close_tab_size(self, height):
        self.height -= height 
        print(self.height)   
        self.setFixedHeight(self.height)   


class Folders(Qt.QFrame):
    def __init__(self, dir):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self) 
        self.setContentsMargins(0, 0, 0, 0)
        self.dir = dir
        self.list = Folder_list(dir=dir)
        self.scroll = QScrollArea()

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.list)

        self.setMinimumHeight(200)
        self.setFixedWidth(220)

        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)
        