import sys
import sys
import threading
import psutil
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect, QWidget, QListWidget, QListView
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class QCustomQWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()

        self.textDownQLabel = QLabel()

        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout = QHBoxLayout()
        self.iconQLabel = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')
        self.setFixedHeight(30)

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))

class exampleQMainWindow (QMainWindow):
    def __init__ (self):
        super(exampleQMainWindow, self).__init__()
        # Create QListWidget
        self.myQListWidget = QListWidget(self)
        for index, name, icon in [
            ('No.1', 'Meyoko',  'left-a.png'),
            ('No.2', 'Nyaruko', 'left-a.png'),
            ('No.3', 'Louise',  'left-a.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.setIcon(icon)
            myQCustomQWidget.setFixedHeight(30)
            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        self.setCentralWidget(self.myQListWidget)


app = QApplication([])
window = exampleQMainWindow()
window.show()
sys.exit(app.exec_())
