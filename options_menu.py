import os, sys
sys.path.insert(0, os.path.abspath("."))

from PyQt5 import Qt, QtCore

import sys
import threading
import psutil
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect, QWidget, QListWidget, QListView


from menu_tab import QMenuOption



                     

class Options(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(340, 1200)
        self.o_menu = QMenuOption()
        
        self.gray_palette = self.palette()
        self.gray_palette.setColor(QPalette.Window, QColor(50, 50, 50))
        
        self.setPalette(self.gray_palette)
        self.setContentsMargins(5, 5, 5, 5)
        layout = Qt.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignTop)

        layout2 = Qt.QVBoxLayout(self)
        layout3 = Qt.QVBoxLayout(self)
        layout.addWidget(self.o_menu)
    
        layout2.addLayout(layout)
        layout2.addLayout(layout3)
        self.setLayout(layout2)
        





        


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = Options()
    w.show()
    sys.exit(app.exec_())       