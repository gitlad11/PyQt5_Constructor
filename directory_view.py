

from PyQt5 import Qt, QtCore

import os, sys

from PyQt5.QtCore import  QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QLabel, QLineEdit, QFrame, QWidget, QScrollArea
import datetime
import ctypes
from QMargin import QMargin
from icon_button import QIcon_Button
from title import Title
from folders import Folders


class QDirectoryBtn(QFrame):
    def __init__(self, type, name, open_folder=None):
        super().__init__()
        self.type = type
        self.name = name
        self.open_folder = open_folder
        self.layout = Qt.QVBoxLayout(self)
        self.setStyleSheet('border: 0px;')

        self.cursor_pix = QPixmap('cursor-dark2.png')
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(23, 23), QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.btn = Qt.QPushButton("")
        self.setCursor(self.current_cursor)

        if open_folder:
            self.btn.clicked.connect(lambda : self.open_folder(self.name))

        self.Icon = QIcon()
        if self.type == "folder":
            self.image = Qt.QImage("folder-dir.png")
        else:
            self.image = Qt.QImage("script-dir.png") 
        self.pix = QPixmap.fromImage(self.image)
        self.pix.scaled(QSize(67, 67), QtCore.Qt.KeepAspectRatio)
        self.Icon.addPixmap(self.pix)
        self.btn.setIcon(self.Icon)
        self.btn.setIconSize(QSize(46, 46))

      
        self.setFixedHeight(90)
        self.setFixedWidth(120)
        self.label = QLabel(str(self.name))
        self.label.setFont(QFont("Helvetica", 10))
        self.label.setStyleSheet(""" QLabel { color : #fff; font-weight: bold; letter-spacing: 1px; border : 0px;  } """)

        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        self.setStyleSheet(" margin: 10px 10px 10px 10px; ")
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setStyleSheet(""" QFrame { border: 0px; } """)

    def event(self, e):
        if e.type() == QtCore.QEvent.Enter:
            self.setStyleSheet(""" QFrame { border: 1px solid gray; border-radius: 4px 4px 4px 4px; background-color: rgba(160, 160, 160, 0.2); } """)
            
        elif e.type() == QtCore.QEvent.Leave:
            self.setStyleSheet(""" QFrame { border: 0px; } """)

        

        return QWidget.event(self, e)
        

class QDirectoryList(QFrame):
    def __init__(self, dir, open_folder):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.dir = dir
        self.open_folder = open_folder
        self.extensions_image = ['img', 'jpeg', 'web', 'png', 'favicon', 'svg']
        self.extensions_files = ['py', 'cpp', 'js', 'txt', 'json', 'xml', 'html', 'jsx', 'css', 'sass', 'csharp', 'c', 'rb', 'dart']
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.setStyleSheet(""" QFrame{ background-color: rgba(60, 60, 80, 1);
                           border-radius: 0px 0px 0px 0px; 
                           border: 0px;
                            }""")

        self.initUI()
        self.setLayout(self.layout) 

    def initUI(self):
        list = os.listdir(self.dir)
        
        for i in list:
            splited = i.split('.')
            if len(splited) > 1 and splited[1] in self.extensions_files:
                item = QMargin(QDirectoryBtn(type='file', name=i), 10, 30, 10, 10)
                self.layout.addWidget(item)
            elif len(splited) > 1 and splited[1] in self.extensions_image:
                item = QMargin(QDirectoryBtn(type='image', name=i), 10, 30, 10, 10)
                self.layout.addWidget(item)
            elif os.path.isdir(i):
                second_item = QMargin(QDirectoryBtn('folder', i, open_folder= self.open_folder), 10, 30, 10, 10)  
                self.layout.addWidget(second_item)     
     
        

class QCurrent_dir(QFrame):
    def __init__(self, directory, back_folder):
        super().__init__()
        self.dir = directory
        self.back_folder = back_folder
        self.layout = Qt.QHBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignLeft)
        self.directory = QLabel("directory:")
        self.directory.setFont(QFont("Helvetica", 9))
        self.directory.setStyleSheet(""" QLabel { font-weight : bold; color : #fff; border: 0px; } """)

        self.label = QLabel(str(self.dir))
        self.label.setFont(QFont("Helvetica", 9))
        self.label.setStyleSheet(""" QLabel { color : #fff; border: 0px; } """)
        self.setStyleSheet(""" QFrame { border-bottom : 1px solid gray; } """)

        self.back_btn = QIcon_Button(icon='icons/arrow-back.png', height=22, width=34, onClick=self.back_folder, fill=False )
        
        self.layout.addWidget(self.back_btn)
        self.layout.addWidget(self.directory)
        self.layout.addWidget(self.label)
        self.setFixedHeight(33)
        self.layout.setContentsMargins(10, 10, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)


class QDirectory_view(QFrame):
    def __init__(self):
        super().__init__()
        self._current_directory = ''
        self._root_directory = ''
        self.layout = Qt.QHBoxLayout(self)
        self.initUI()
        self.directory = QDirectory(dir=self._current_directory, open_folder=self.open_folder, back_folder=self.back_folder )
        self.folders = Folders(dir=self._current_directory)
        self.setStyleSheet(""" QFrame{ 
                                  background-color: rgba(60, 60, 80, 1);
                                  border-radius: 4px 4px 4px 4px;
                                  
                                  }""")

        self.layout.addWidget(self.directory)
        self.layout.addWidget(self.folders)
        self.resize(850, 160)
        
        self.setMaximumHeight(200)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.setLayout(self.layout)
        

    def initUI(self):
        try:
            self._current_directory = str(os.getcwd())
            self._root_directory = str(os.getcwd())
        except Exception:
            print("Oops!  not a folder.  Try again...")

    def open_folder(self, folder):
        
        self._current_directory += "/" + folder  
        self.directory = QDirectory(dir=self._current_directory, open_folder=self.open_folder, back_folder=self.back_folder)
        self.layout.itemAt(0).widget().deleteLater()
        self.layout.insertWidget(0, self.directory)

    def back_folder(self):

        if self._current_directory != self._root_directory:
            folders = self._current_directory.split('/')
            folders.pop()
            string = ''
            for i in folders:
                i + '/'
                string += i

            self._current_directory = string
            self.directory = QDirectory(dir=self._current_directory, open_folder=self.open_folder, back_folder=self.back_folder)
            self.layout.itemAt(0).widget().deleteLater()
            self.layout.insertWidget(0, self.directory)   
            
        

class QDirectory(QFrame):
    def __init__(self, dir, open_folder, back_folder):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.dir = dir
        self.back_folder = back_folder
        self.open_folder = open_folder
        self.setStyleSheet(""" QFrame{ background-color: rgba(60, 60, 80, 1);
                                  border-radius: 4px 4px 4px 4px;
                                  
                                  }""")
        self.resize(850, 160)
        self.setMinimumWidth(800)
        self.setMaximumHeight(200)

        self.setLayout(self.layout)
        
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)

        self.d_list = QDirectoryList(dir=self.dir, open_folder=self.open_folder)    
        self.scroll.setWidget(self.d_list)

        self.current_dir = QCurrent_dir(self.dir, back_folder=self.back_folder)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)

        self.layout.addWidget(self.current_dir)
        self.layout.addWidget(self.scroll)
        

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QDirectory_view()
    w.show()
    sys.exit(app.exec_())