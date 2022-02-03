
from PyQt5 import Qt, QtCore, QtGui

import sys
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QFrame
import numpy as np
from list_widget import QList_widget
from main import Window

class QNavbar(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.setFixedWidth(270)
        self.setFixedHeight(30)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.btn1 = Qt.QPushButton('')
        self.btn1.setStyleSheet(""" QPushButton { border: 1px inset gray; background-color : #fff; margin : 5px 0px 0px 6px; border-radius : 5px 5px 5px 5px; } """)

        self.Icon1 = QIcon()
        self.pix1 = QPixmap('icons/plus.png')
        self.pix1.scaled(QSize(29, 29))
        self.Icon1.addPixmap(self.pix1)
        self.btn1.setFixedHeight(29)
        self.btn1.setFixedWidth(50)
        self.btn1.setContentsMargins(4, 4, 0, 0)
        self.btn1.setIcon(self.Icon1)

        self.cursor_pix = QPixmap('cursor-dark2.png')
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(18, 18), QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.btn1.setCursor(self.current_cursor)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        self.layout.addWidget(self.btn1)

        self.setLayout(self.layout)


class QListItemItem(QWidget):
    def __init__(self, item):
        super().__init__()
        self.item = item
        self.layout = Qt.QHBoxLayout(self)
        self.setStyleSheet(""" QFrame { border : 1px solid gray; } """)
        self.label = QLabel(str(self.item))
        self.label.setFont(QFont('Helvetica', 9))
        self.layout.addWidget(self.label)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)

class QListItem(QWidget):
    def __init__(self, title, items, icon=None):
        super().__init__()
        self.title = title
        self.items = items
        self.icon = icon
        self.active = False

        self.cursor_pix = QPixmap('cursor-dark2.png')
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(18, 18), QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.setCursor(self.current_cursor)

        self.setStyleSheet("border: 1px 1px 0px 0px;")
        self.resize(270, 18)
        self.setWindowOpacity(0.6)

        self.color1 = QtGui.QColor(240, 83, 218)
        self.color2 = QtGui.QColor(101, 217, 245)

        self.layout = Qt.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.Icon = QIcon()
        self.pix = QPixmap('left-a.png')
        self.pix.scaled(QSize(13, 13))
        self.Icon.addPixmap(self.pix)
        self.btn = Qt.QPushButton('')
        self.btn.clicked.connect(self.on_active)
        self.btn.setText(str(self.title))
        self.btn.setFont(QFont("Helvetica", 11))
        self.btn.setContentsMargins(0, 0, 0, 0)
        self.btn.setFixedWidth(270)
        self.btn.setStyleSheet("color: #141313; letter-spacing: 1px; border-bottom: 1px solid gray; padding: 5px 5px 5px 5px; text-align: left; font-weight: bold; ")
        self.btn.setIcon(self.Icon)
        self.btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        
        self.layout.addWidget(self.btn)

        self.layout.setAlignment(QtCore.Qt.AlignCenter)


        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250
        )

    def _animate(self, value):
        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: rgb(255, 255, 255);
            border-style: solid;
            border-radius:21px;
        """
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1}); color: #000; letter-spacing: 1px;  padding: 5px 5px 5px 5px; text-align: left;".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        self.btn.setStyleSheet(qss)    

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)


    def on_active(self):
            if self.active:
                self.pix = QPixmap('left-a.png')
                self.pix.scaled(QSize(19, 19))
                self.Icon.addPixmap(self.pix)
                self.btn.setIcon(self.Icon)
                
                self.layout.itemAt(1).widget().deleteLater()

                self.active = False

            else:
                self.pix = QPixmap('down-a.png')
                self.pix.scaled(QSize(19, 19))
                self.Icon.addPixmap(self.pix)
                self.btn.setIcon(self.Icon)

                menu = QList_widget(self.items)
                self.layout.addWidget(menu)
                self.active = True


class QList_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)

        self.list = [
            { "name": "player", "icon": "icons/person.png" },
            { "name": "static box", "icon": "icons/box.png" },
            { "name": "health points", "icon": "icons/interface.png" }
        ]
        self.l = np.array(["item 1", "item 2", "item 3"])
        self.btn = QListItem("stupid things", items=self.list)
        self.btn2 = QListItem("clever things", items=self.list)
        self.btn3 = QListItem("funny things", items=self.list)
        self.btn4 = QListItem("fuck off", items=self.list)
  
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.addWidget(self.btn4)
        self.layout.setSpacing(0)
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.resize(460, 270)
        self.setStyleSheet(""" QWidget { background-color: #fff; } """)


class QList(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = Qt.QVBoxLayout(self)
        self.setFixedHeight(900)
        self.setFixedWidth(270)
        self.list_widget = QList_Widget()
        self.navbar = QNavbar()
        self.graph = Window()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.navbar)
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.graph)
        self.setStyleSheet(""" QFrame{ background-color: rgba(60, 60, 80, 1);
                                border-radius: 4px 4px 4px 4px;
                                border: 1px inset gray; 
                                 }""")
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.layout)



if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QList()
    w.show()
    sys.exit(app.exec_())