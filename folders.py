from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from title import Title
from icon_button import QIcon_Button
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor,  QPixmap, QIcon
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import QThread,  QSize
import os


class Tab_items(Qt.QFrame):
    def __init__(self, directory, title):
        super().__init__()
        self.dir = directory
        self.title = title
        self.layout = Qt.QVBoxLayout(self)
        self.setStyleSheet(""" QFrame { border-bottom: 1px solid gray; border-left: 1px solid gray; padding: 0px 0px 0px 0px; border-radius: 0px; }""")
        self.setMinimumHeight(1)
        self.setLayout(self.layout)        
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        self.setContentsMargins(0, 0, 0, 0)
        self.extensions_image = ['img', 'jpeg', 'web', 'png', 'favicon', 'svg']
        self.extensions_files = ['py', 'cpp', 'js', 'txt', 'json', 'xml', 'html', 'jsx', 'css', 'sass', 'csharp', 'c','rb', 'dart']
        self.initUI()

    def initUI(self):
        if self.dir:
            list = os.listdir(self.dir + '/' + self.title)

            for i in list:
                splited = i.split('.')
                if len(splited) > 1 and splited[1] in self.extensions_files:
                    item = Tab(title=i, icon="script-dir.png", type="file", directory='')
                    self.layout.addWidget(item)
                else:
                    tab = Tab_btn(title=str(i), icon="folder-dir.png", type='folder', directory='')
                    self.layout.addWidget(tab)



class Tab_btn(Qt.QFrame):
    def __init__(self, title, icon=None, type=None, on_tab_click=None, directory=None):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.title = title
        self.icon = icon
        self.type = type
        self.dir = directory
        self.on_tab_click = on_tab_click
        self.active = False

        self.btn = QtWidgets.QPushButton()


        self.file_icon = QIcon_Button(self.icon, onClick=self.on_active)
        self.btn.setText(str(self.title))
        self.btn.clicked.connect(self.on_active)
        self.items = Tab_items(directory=self.dir, title=self.title)

        self.btn.setFixedHeight(30)
        self.btn.setMinimumWidth(220)
        self.setContentsMargins(0, 0, 0, 0)
        self.setMinimumWidth(250)
        self.setFixedHeight(34)

        self.setStyleSheet(""" QFrame { background-color: rgba(10, 10, 10, 0); padding: 0px 0px 0px 0px; border: 0px } QPushButton { 
            background-color: rgba(10, 10, 10, 0); 
            font: 75 9pt "Microsoft YaHei UI";
            font-weight: bold;
            color: #fff;
            padding: 0px 0px 5px 0px;
            text-align: left;
            margin: 0px 0px 0px 0px;
            border: 0px;
            } """)

        if self.type == "folder":
            self.Icon = QIcon()
            self.pix = QPixmap(str("left-a.png"))
            self.pix.scaled(QSize(13, 13))
            self.Icon.addPixmap(self.pix)   
            self.btn.setIcon(self.Icon)
           

        self.layout.addWidget(self.file_icon)
        self.layout.addWidget(self.btn)
        

        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)

        self.cursor_pix = QPixmap('cursor-dark2.png')  
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(18, 18), QtCore.Qt.KeepAspectRatio) 
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.setCursor(self.current_cursor)
        
    def event(self, e):
        if e.type() == QtCore.QEvent.Enter:
             self.setStyleSheet(""" QFrame { background-color: rgba(150, 150, 150, 0.2);   border: 0px; } QPushButton { 
           background-color: rgba(10, 10, 10, 0);  
            font: 75 9pt "Microsoft YaHei UI";
            font-weight: bold;
            color: #fff;
            padding: 0px 0px 5px 0px;
            margin: 0px 0px 0px 0px;
            text-align: left;
            border: 0px;
            } """)
            
        elif e.type() == QtCore.QEvent.Leave:
             self.setStyleSheet(""" QFrame { background-color: rgba(10, 10, 10, 0);   border: 0px; } QPushButton { 
            background-color: rgba(10, 10, 10, 0); 
            font: 75 9pt "Microsoft YaHei UI";
            font-weight: bold;
            color: #fff;
            padding: 0px 0px 5px 0px;
            margin: 0px 0px 0px 0px;
            text-align: left;
            border: 0px;
            } """)
        elif e.type() == QtCore.QEvent.MouseButtonPress:
            if self.type == "folder":
                print('folder')


        return QWidget.event(self, e)

    def on_active(self):
        
        if self.active:
            self.pix = QPixmap('left-a.png')
            self.pix.scaled(QSize(13, 13))
            self.Icon.addPixmap(self.pix)
            self.btn.setIcon(self.Icon)

            self.active = False
            self.on_tab_click(False)
        else:
            self.pix = QPixmap('down-a.png')
            self.pix.scaled(QSize(13, 13))
            self.Icon.addPixmap(self.pix)
            self.btn.setIcon(self.Icon)

            self.active = True
            self.on_tab_click(True)

        

class Tab(Qt.QFrame):
    def __init__(self, title, directory, icon=None, type=None, on_tab_open=None, on_tab_close=None):
        super().__init__()
        self.title = title
        self.icon = icon
        self.type = type
        self.dir = directory
        self.on_tab_open = on_tab_open
        self.on_tab_close = on_tab_close
        self.active = False
        self.layout = Qt.QVBoxLayout(self)

        self.tab_btn = Tab_btn(title=self.title, icon=self.icon, type=self.type, on_tab_click=self.on_tab_click, directory=self.dir)
        self.setContentsMargins(0, 0, 0, 0)
        
        self.layout.addWidget(self.tab_btn)
        self.setStyleSheet(""" QFrame { margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; } """)
        self.setMinimumHeight(44)
        self.setMinimumWidth(250)
        
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def on_tab_click(self, active):
        if active:
            tab_items = Tab_items(directory=self.dir, title=self.title)
            self.layout.addWidget(tab_items)
            self.setMinimumHeight(200)
        else:
            self.layout.itemAt(1).widget().deleteLater()
            self.setMinimumHeight(44)
            return


class Folder_list(Qt.QFrame):
    def __init__(self, dir):
        super().__init__()
        self.height = 200
        self.dir = dir
        self.layout = Qt.QVBoxLayout(self)
        self.setContentsMargins(0, 0, 0, 0)
        self.extensions_image = ['img', 'jpeg', 'web', 'png', 'favicon', 'svg']
        self.extensions_files = ['py', 'cpp', 'js', 'txt', 'json', 'xml', 'html', 'jsx', 'css', 'sass', 'csharp', 'c', 'rb', 'dart']
        self.setMinimumHeight(200)
        self.setFixedWidth(250)

        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
            list = os.listdir(self.dir)
            for i in list:
                self.height += 60
                splited = i.split('.')

                if len(splited) > 1 and splited[1] in self.extensions_files:
                    item = Tab(title=i, icon="script-dir.png", type="file", directory='')
                    self.layout.addWidget(item)
                elif len(splited) > 1 and splited[1] in self.extensions_image:
                    item = Tab(title=i, icon="script-dir.png", type="image", directory='')
                    self.layout.addWidget(item)
                elif os.path.isdir(i):
                    second_item = Tab(title=i, icon="folder-dir.png", type="folder", directory=self.dir)
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
        self.setFixedWidth(250)

        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)
        