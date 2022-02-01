import os, sys

from icon_button import QIcon_Button

sys.path.insert(0, os.path.abspath("."))
from PyQt5 import Qt, QtCore
import sys
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QFrame
from menu_tab import QMenuOption
from sized_box import QSizedBox
from gradient_button import GradientButton



class NavBar(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(30)
        self.setFixedWidth(330)
        self.layout = Qt.QHBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.btn = QIcon_Button(icon="icons/angle-left.png", toolTip="Назад")
        self.btn2 = QIcon_Button(icon="icons/angle-right.png", toolTip="Вперед")
        self.btn3 = QIcon_Button(icon="icons/folder.png", toolTip="Сохранить")
        self.btn4 = QIcon_Button(icon='icons/plus.png', toolTip="Добавить компонент")
        self.setStyleSheet(""" QFrame {  border: 0px; } """)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.addWidget(self.btn4)


class Options_navbar(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignCenter)
        self.navbar = NavBar()
        self.white_palette = self.palette()
        self.white_palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(self.white_palette)
        self.setStyleSheet(""" QFrame { background-color: rgba(170, 170, 200, 1); border: 1px solid gray ; border-radius: 4px 4px 4px 4px; } """)
        self.setMinimumWidth(350)
        self.setMinimumHeight(30)

        self.layout.addWidget(self.navbar)
        self.setLayout(self.layout)


class Options(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(120)
        self.setMaximumWidth(340)
        self.setMinimumHeight(700)

        self.o_menu = QMenuOption()
        self.o_menu1 = QMenuOption()
        self.o_menu2 = QMenuOption()
        self.add_component = GradientButton()
        self.navbar = Options_navbar()

        self.setStyleSheet(""" QFrame{ 
                                 background-color: rgba(60, 60, 80, 1);
                                 border: 1px inset gray;
                                  
                                  }""")
        self.setContentsMargins(0, 0, 0, 0)
        layout = Qt.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)

        layout2 = Qt.QVBoxLayout(self)
        layout3 = Qt.QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.navbar)

        layout.addWidget(self.o_menu)
        layout.addWidget(self.o_menu1)
        layout.addWidget(self.o_menu2)

        layout.addWidget(self.add_component)
        layout2.addLayout(layout)
        layout2.addLayout(layout3)
        self.setLayout(layout2)


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = Options()
    w.show()
    sys.exit(app.exec_())       