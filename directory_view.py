
from PyQt5 import Qt, QtCore
import pyqtgraph as pg
import numpy as np
import os, sys
import threading
import psutil
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon, QPixmap, QCursor, QPainter, QPen
from PyQt5.QtWidgets import QLabel,QLineEdit, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect,  QCheckBox
import datetime
import ctypes
from QMargin import QMargin


class QDirectoryBtn(Qt.QPushButton):
    def __init__(self, icon, name):
        super().__init__()
        self.icon = icon
        self.name = name

        self.setStyleSheet('border: 0px;')
        self.cursor_pix = QPixmap('cursor-dark2.png')
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(23, 23), QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.setCursor(self.current_cursor)

        self.Icon = QIcon()
        self.image = Qt.QImage(str(self.icon))
        self.pix = QPixmap.fromImage(self.image)
        self.pix.scaled(QSize(85, 85), QtCore.Qt.KeepAspectRatio)
        self.Icon.addPixmap(self.pix)
        self.setIcon(self.Icon)
        self.setIconSize(QSize(85, 85))
        self.setFixedWidth(85)
        self.setFixedHeight(85)
        self.setStyleSheet(" margin: 10px 10px 10px 10px; ")



class QDirectory(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.resize(900, 200)
        self.setStyleSheet(""" QFrame{ background-color: rgba(80, 80, 80, 1);
                           border-radius: 0px 0px 0px 0px; 
                           border: 1px solid gray; }""")

        self.folder = QMargin(QDirectoryBtn("folder-dir.png", "animations"), 10, 30, 10, 10)
        self.folder1 = QMargin(QDirectoryBtn("folder-dir.png", "sprites"), 10, 30, 10, 10)
        self.file1 = QMargin(QDirectoryBtn("script-dir.png", "player.py"), 10, 30, 10, 10)

        self.layout.addWidget(self.folder)
        self.layout.addWidget(self.folder1)
        self.layout.addWidget(self.file1)


        self.setLayout(self.layout)

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QDirectory()
    w.show()
    sys.exit(app.exec_())