
from PyQt5 import Qt, QtCore

import sys
import threading
import psutil
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect, QWidget, QListWidget, QListView



class QListItem(QWidget):
    def __init__(self, title, icon=None):
        super().__init__()
        self.title = title
        self.icon = icon
        self.active = True

        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("border: 1px 1px 0px 0px;")
        self.resize(220, 18)
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

    
        self.btn.setFixedWidth(220)
        self.btn.setStyleSheet("color: #141313; letter-spacing: 1px; border-bottom: 1px solid gray; padding: 5px, 5px, 5px, 5px; text-align: left; ")
        self.btn.setIcon(self.Icon)
        self.btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.layout.addWidget(self.btn)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)


    def event(self, e):
        if e.type() == QtCore.QEvent.Enter:
            self.btn.setStyleSheet(
                "background-color: #dbdbdb; color: #141313; letter-spacing: 1px; border-bottom: 1px solid gray; padding: 5px, 5px, 5px, 5px; text-align: left;")
        elif e.type() == QtCore.QEvent.Leave:
            self.btn.setStyleSheet(
                "color: #141313; letter-spacing: 1px; border-bottom: 1px solid gray; padding: 5px, 5px, 5px, 5px; text-align: left;")

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



class QList(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)

        self.btn = QListItem("stupid things")
        self.btn2 = QListItem("clever things")
        self.btn3 = QListItem("funny things")
        self.btn4 = QListItem("fuck off")
  
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.addWidget(self.btn4)
        self.layout.setSpacing(0)
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)



if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QList()
    w.show()
    sys.exit(app.exec_())