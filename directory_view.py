
from PyQt5 import Qt, QtCore

import os, sys

from PyQt5.QtCore import  QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QLabel, QLineEdit, QFrame, QWidget
import datetime
import ctypes
from QMargin import QMargin


class QDirectoryBtn(QFrame):
    def __init__(self, type, name, ):
        super().__init__()
        self.type = type
        self.name = name
        self.layout = Qt.QVBoxLayout(self)
        self.setStyleSheet('border: 0px;')
        self.cursor_pix = QPixmap('cursor-dark2.png')
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(23, 23), QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
    
        self.btn = Qt.QPushButton("")
        self.btn.setCursor(self.current_cursor)

        self.Icon = QIcon()
        if self.type == "folder":
            self.image = Qt.QImage("folder-dir.png")
        else:
            self.image = Qt.QImage("script-dir.png")     
        self.pix = QPixmap.fromImage(self.image)
        self.pix.scaled(QSize(67, 67), QtCore.Qt.KeepAspectRatio)
        self.Icon.addPixmap(self.pix)
        self.btn.setIcon(self.Icon)
        self.btn.setIconSize(QSize(67, 67))

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
            self.setStyleSheet(""" QFrame { border: 1px solid gray; border-radius: 4px 4px 4px 4px; } """)
        elif e.type() == QtCore.QEvent.Leave:
            self.setStyleSheet(""" QFrame { border: 0px; } """)
    
        return QWidget.event(self, e)
        

class QDirectoryList(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.items = [
            { "name" : ".idea", "type" : "folder" },
            { "name" : "player.py", "type" : 'file' },
            { "name" : "script-dir.png", "type" : "file" }
        ]
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignCenter)
        self.setStyleSheet(""" QFrame{ background-color: rgba(40, 40, 60, 1);
                           border-radius: 0px 0px 0px 0px; 
                           border: 0px;
                            }""")

        self.initUI()
        self.setLayout(self.layout) 

    def initUI(self):
        for i in self.items:
            item = QMargin(QDirectoryBtn(i['type'], i['name']), 10, 30, 10, 10)
            self.layout.addWidget(item)


class QCurrent_dir(QFrame):
    def __init__(self, directory):
        super().__init__()
        self.dir = directory
        self.layout = Qt.QHBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignLeft)
        self.directory = QLabel("directory:")
        self.directory.setFont(QFont("Helvetica", 9))
        self.directory.setStyleSheet(""" QLabel { font-weight : bold; color : #fff; border: 0px; } """)

        self.label = QLabel(str(self.dir))
        self.label.setFont(QFont("Helvetica", 9))
        self.label.setStyleSheet(""" QLabel { color : #fff; border: 0px; } """)
        self.setStyleSheet(""" QFrame { border-bottom : 1px solid gray; } """)

        self.layout.addWidget(self.directory)
        self.layout.addWidget(self.label)
        
        self.layout.setContentsMargins(10, 10, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)


class QDirectory(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.dir = ""
        self.setStyleSheet(""" QFrame{ background-color: rgba(40, 40, 60, 1);
                                  border-radius: 4px 4px 4px 4px;
                                  
                                  }""")
        self.resize(1200, 160)
        self.setMaximumHeight(200)

        self.setLayout(self.layout)
        self.initUI()

        self.d_list = QDirectoryList()       
        self.current_dir = QCurrent_dir(self.dir)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.current_dir)
        self.layout.addWidget(self.d_list)

    def initUI(self):
        self.dir = str(os.getcwd())
        

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QDirectory()
    w.show()
    sys.exit(app.exec_())