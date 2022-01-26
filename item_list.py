from PyQt5 import Qt, QtCore

import sys
import threading
import psutil
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect, QWidget



class QListItem(QWidget):
    def __init__(self, title, icon=None):
        super().__init__()
        self.title = title
        self.icon = icon
        self.active = True

        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("border: 1px 1px 0px 0px;")
        self.resize(300, 18)
        self.setWindowOpacity(0.6)

        self.layout = Qt.QHBoxLayout(self)
        self.Icon = QIcon()
        self.pix = QPixmap('left-a.png')
        self.pix.scaled(QSize(16, 16))
        self.Icon.addPixmap(self.pix)
        self.btn = Qt.QPushButton('')
        self.btn.setIcon(self.Icon)
        self.label = QLabel(str(self.title))
        self.setFont(QFont("Helvetica", 11))
        self.setContentsMargins(40, 0, 40, 0)
        self.label.setStyleSheet("color: #141313; letter-spacing: 1px; border-bottom: 1px solid gray; padding: 2px, 2px, 4px, 2px;")
        self.btn.setStyleSheet("border: 0px;")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)


    def event(self, e):
        if e.type() == QtCore.QEvent.Enter:
            self.label.setStyleSheet(
                "background-color: #dbdbdb; color: #141313; letter-spacing: 1px; border-bottom: 1px solid gray; padding: 2px, 2px, 4px, 2px;")
        elif e.type() == QtCore.QEvent.Leave:
            self.label.setStyleSheet(
                "color: #141313; letter-spacing: 1px; border-bottom: 1px solid gray; padding: 2px, 2px, 4px, 2px;")
        elif e.type() == QtCore.QEvent.MouseButtonPress:
            print("mouse clocked")
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

        return QWidget.event(self, e)


class QList(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.btn = QListItem("stupid things")
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)



if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QList()
    w.show()
    sys.exit(app.exec_())