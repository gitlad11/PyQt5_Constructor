from PyQt5 import Qt, QtCore

import sys
import threading
import psutil
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor
from PyQt5.QtWidgets import QLabel, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect, QWidget


class QButton(Qt.QPushButton):
    def __init__(self, title, color, width, height, contain, toolTip= None):
        super().__init__()
        self.title = title
        self.color = color
        self.width = width
        self.height = height
        self.contain = contain
        self.toolTip = toolTip

        self.style = ""
        self.red_palette = self.palette()
        self.red_palette.setColor(QPalette.Window, QColor(255, 100, 100))
        self.blue_palette = self.palette()
        self.blue_palette.setColor(QPalette.Window, QColor(30, 30, 255))
        self.yellow_palette = self.palette()
        self.yellow_palette.setColor(QPalette.Window, QColor(230, 255, 0))
        self.purple_palette = self.palette()
        self.purple_palette.setColor(QPalette.Window, QColor(100, 100, 255))

        if self.color == 'yellow':
            self.setPalette(self.yellow_palette)
        elif self.color == 'purple':
            self.setPalette(self.purple_palette)
        elif self.color == 'red':
            self.setPalette(self.red_palette)
        else:
            self.setPalette(self.blue_palette)

        if self.color == "yellow" and self.contain:
            self.style = "background : rgba(255, 255, 0, 1);"
        elif self.color == "red" and self.contain:
            self.style = "background : rgba(255, 60, 60, 1);"
        elif self.color == "blue" and self.contain:
            self.style = "background : rgba(100, 76, 255, 1);"
        elif self.color == "purple" and self.contain:
            self.style = "background : rgba(60, 60, 255, 1);"

        if self.contain:
            self.setStyleSheet(self.style + "border: 2px ridge gray; border-radius: 2px 2px 2px 2px; color: #fff; letter-spacing: 1px;")
        else:
            self.setStyleSheet("color: #141313; letter-spacing: 1px;")
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        if self.toolTip:
            self.setToolTip(str(self.toolTip))

        self.setToolTipDuration(3000)
        self.setFont(QFont("Helvetica", 15, QFont.Bold))
        self.setText(str(self.title))
        if self.width > 0:
            self.setFixedWidth(self.width)
        if self.height > 0:
            self.setFixedHeight(self.height)

    def event(self, e):
        if e.type() == QtCore.QEvent.Enter:
            print('mouse entered')
        elif e.type() == QtCore.QEvent.Leave:
            print('mouse leave')
        return QWidget.event(self, e)


class Window(Qt.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.btn = QButton("click", 'red', 220, 30, contain=False, toolTip="click fast!")
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)



if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
