from PyQt5 import Qt, QtCore, QtGui

import sys

from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect, QWidget, \
    QListWidget, QListView
from option_input import QInput, QFourInputs, QTwoInputs, QCheckInput, QdropdownInput, QImageInput
from icon_button import QIcon_Button


class QMenuTab(QWidget):
    def __init__(self, title, on_show, icon=None, toolTip=None):
        super().__init__()
        self.title = title
        self.toolTip = toolTip
        self.on_show = on_show
        self.icon = icon
        self.active = False

        self.cursor_pix = QPixmap('cursor-dark2.png')
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(21, 21), QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.setCursor(self.current_cursor)

        self.color1 = QtGui.QColor(240, 83, 218)
        self.color2 = QtGui.QColor(101, 217, 245)

        self.setStyleSheet("border: 1px 1px 0px 0px;")
        self.resize(330, 22)
        self.setWindowOpacity(0.6)

        self.layout = Qt.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.Icon = QIcon()
        self.pix = QPixmap('left-a.png')
        self.pix.scaled(QSize(13, 13))
        self.Icon.addPixmap(self.pix)
        self.btn = Qt.QPushButton('')
        self.btn.clicked.connect(self.on_active)
        self.btn.setText(str(self.title))
        self.btn.setFont(QFont("Helvetica", 11))
        self.btn.setFixedWidth(330)
        self.btn.setFixedHeight(30)
        self.btn.setStyleSheet("color: #000; background-color: rgba(255, 255, 255, 1); letter-spacing: 1px; "
                               "border-radius: 4px 4px 4px 4px;"
                               "border-bottom: 1px solid gray; padding: 2px 10px 2px 10px; text-align: left; ")
        self.btn.setIcon(self.Icon)
        self.btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        if self.toolTip:
            self.btn.setToolTip(str(self.toolTip))
            self.btn.setToolTipDuration(4000)

        self.setStyleSheet("""QToolTip { 
                           background-color: rgba(30, 30, 30, 1); 
                           max-height : 40px;
                           color: white;
                           border-radius: 4px 4px 4px 4px; 
                           border: #fff solid 1px
                           } 
                           QPushButton { border: 0px; } """)
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
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1}); color: #000; letter-spacing: 1px;  padding: 2px 10px 2px 10px; text-align: left;".format(
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
            self.active = False
        else:
            self.pix = QPixmap('down-a.png')
            self.pix.scaled(QSize(19, 19))
            self.Icon.addPixmap(self.pix)
            self.btn.setIcon(self.Icon)
            self.active = True
        self.on_show(self.active)

class Options_list(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = Qt.QVBoxLayout()

        self.input1 = QInput("background-color:")
        self.input2 = QFourInputs("margin:")
        self.input3 = QTwoInputs("size - ", "width:", "height:")
        self.input4 = QCheckInput("show:")
        self.input5 = QdropdownInput("Map")
        self.input6 = QImageInput("down-a.png", "image: ")

        self.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.input2)
        self.layout.addWidget(self.input3)
        self.layout.addWidget(self.input5)
        self.layout.addWidget(self.input4)
        self.layout.addWidget(self.input6)
        self.setLayout(self.layout)


class Options_menu(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.options = []
        self.o_list = Options_list()
        self.setStyleSheet("background-color: rgba(60, 60, 90, 1); border-radius: 3px 3px 3px 3px;")
        self.setFixedHeight(400)
        self.setFixedWidth(330)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout = Qt.QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)

        self.layout.addWidget(self.o_list)
        self.setLayout(self.layout)

    def save_style(self):
        return

    def on_backward(self):
        return

    def on_forward(self):
        return


class QMenuOption(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.tab = QMenuTab("background", self.on_show, toolTip="set background of sprite")
        self.menu = Options_menu()
        self.layout = Qt.QVBoxLayout(self)
        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)
        self.layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(""" QFrame { border: 0px; } """)
    def on_show(self, show):
        print(show)
        if show:
            self.menu = Options_menu()
            self.layout.addWidget(self.menu)
        else:
            self.layout.itemAt(1).widget().deleteLater()

