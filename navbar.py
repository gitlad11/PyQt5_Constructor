from json import tool
import sys
from textwrap import fill

from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QLabel, QFrame, QApplication, QToolBar, QAction, QMenu, QMenuBar
import ctypes
from PyQt5 import QtWidgets
from icon_button import QIcon_Button
from button import QButton


class QSetting_btn(QFrame):
    def __init__(self, icon, text,  toolTip):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)

        self.icon = icon
        self.text = text
        self.active = True
        self.toolTip = toolTip

        self.setMinimumWidth(120)
        self.setMinimumHeight(35)
        self.btn = QIcon_Button(icon=self.icon, toolTip=self.toolTip, fill=False, onClick=self.on_active)
        self.text = QLabel(str(self.text))

        self.setStyleSheet(""" QFrame { 
        background-color: rbga(250, 250 ,250, 0); color: #fff;  padding: 3px 3px 3px 3px;
        } """)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.text)

        self.setLayout(self.layout)
        self.layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

    def on_active(self):
        return

class QSettings(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.setContentsMargins(0, 0, 0, 0)

        self.btn1 = QSetting_btn(icon='icons/add_white.png', text="Создать проект", toolTip="Новый проект")
        self.btn2 = QSetting_btn(icon='icons/list_white.png', text='Открыть проект', toolTip="Открыть проект")
        self.btn3 = QSetting_btn(icon='icons/settings_white.png', text='настройки', toolTip='Настройки')

        self.layout.addWidget(self.btn3)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn1)

        self.setFixedHeight(40)
        self.setMinimumWidth(200)
        self.layout.setSpacing(0)

        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignLeft)
        
        self.setLayout(self.layout)

class QNav_Menu(QFrame):
    def __init__(self):
        super().__init__()

        self.layout = Qt.QHBoxLayout(self)
           
        
        self.btn1 = Qt.QPushButton("")
        self.btn2 = Qt.QPushButton("")
        self.btn1.setStyleSheet(""" QPushButton { border: 1px inset gray; background-color : #fff; margin : 2px 0px 0px 4px; border-radius : 5px 5px 5px 5px; } """)
        self.btn2.setStyleSheet(""" QPushButton { border: 1px inset gray; background-color : #fff; margin : 2px 0px 0px 4px; border-radius : 5px 5px 5px 5px; } """)
        self.setContentsMargins(0, 0, 0, 0)
        self.btn1.setFixedHeight(25)
        self.btn1.setFixedWidth(50)

        self.btn2.setFixedHeight(25)
        self.btn2.setFixedWidth(50)

        self.Icon1 = QIcon()
        self.pix = QPixmap("caret-r.png")
        self.pix.scaled(QSize(16, 16))
        self.Icon1.addPixmap(self.pix)

        self.Icon2 = QIcon()
        self.pix = QPixmap("stop.png")
        self.pix.scaled(QSize(16, 16))
        self.Icon2.addPixmap(self.pix)

        self.btn2.setIcon(self.Icon2)
        self.btn1.setIcon(self.Icon1)

        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)

        self.btn1.setFixedWidth(50)
        self.btn2.setFixedWidth(50)

        self.cursor_pix = QPixmap('cursor-dark2.png')
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(18, 18), QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.btn1.setCursor(self.current_cursor)
        self.btn2.setCursor(self.current_cursor)

        self.setStyleSheet(""" QFrame { background-color: rgba(60, 60, 110, 0.8
        ); border-radius: 6px 6px 6px 6px; }  
        QPushButton::hover { background : rgba(160, 160, 160, 1); color : #fff; } """)

        self.setFixedWidth(400)
        self.setFixedHeight(50)
        self.layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

class QNavBar(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
       

        self.settings = QSettings()
        self.btn_list = QNav_Menu()
        
        self.layout.addWidget(self.settings)
        self.layout.addWidget(self.btn_list)
        self.layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)
        self.setFixedHeight(60)

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QNavBar()
    w.show()
    sys.exit(app.exec_())