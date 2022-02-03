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

class QMenu_Action(QFrame):
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.layout = Qt.QVBoxLayout(self)
        self.setFixedWidth(200)
        self.setMinimumHeight(200)
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.layout.setSpacing(0)
        self.initUI()

     
        
    def initUI(self):
        for index, item in enumerate(self.items):
            item = QButton(title=item['name'], contain=False, color='red', height=20, width=180)
            self.layout.addWidget(item)

class QSetting_btn(QFrame):
    def __init__(self, icon, toolTip):
        super().__init__()
        self.icon = icon
        self.active = True
        self.toolTip = toolTip
        self.layout = Qt.QVBoxLayout(self)
        self.tabs = [{ "name" : 'новый проект' }, { "name" : 'открыть проект' }, { 'name' : 'сохранить' }]
        self.setFixedWidth(35)
        self.setMinimumHeight(35)
        self.btn = QIcon_Button(icon=self.icon, toolTip=self.toolTip, fill=True, onClick=self.on_active)
        self.setStyleSheet(""" QFrame { background-color: rbga(250, 250 ,250, 1); color: #000;  padding: 0px 0px 0px 0px; border-radius: 4px 4px 4px 4px; } """)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

    def on_active(self):
        if self.active:
            self.layout.itemAt(1).widget().deleteLater()
            self.active = False
        else:
            item_list = QMenu_Action(self.tabs)
            self.layout.addWidget(item_list)
            self.setMinimumHeight(200)

            self.active = True

class QSettings(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.setContentsMargins(0, 0, 0, 0)

        self.btn1 = QSetting_btn(icon='icons/settings.png', toolTip="Настройки")
        self.btn2 = QSetting_btn(icon='icons/list.png', toolTip="Файл")
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