import sys

from PyQt5 import Qt, QtCore, QtWidgets
from icon_button import QIcon_Button

class Edit_btn(QtWidgets.QPushButton):
    def __init__(self, icon, onClick=None):
        super().__init__()
        self.layout = Qt.QHBoxLayout()
        self.icon = icon
        self.onClick = onClick
        self.btn = QIcon_Button(icon = self.icon, onClick = self.onClick)
        self.setStyleSheet("border-right: 1px solid gray")
        self.layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.btn)


class QEditor_list(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.setStyleSheet(""" QFrame { background-color: #fff; border: 1px solid gray; } QPushButton { border : 0px; } """)
        
        self.btn1 = QIcon_Button(icon='hand.png')
        self.btn2 = QIcon_Button(icon='editor.png')
        self.btn3 = QIcon_Button(icon='expand.png')

        self.layout.setAlignment(QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(8, 8, 8, 8)
        self.setFixedHeight(40)
        self.setLayout(self.layout)


class QEditor_block(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout()
        self.setStyleSheet(""" QFrame { border: 1px solid gray; background-color: rgba(10, 10, 10, 1); } """)
        self.resize(800, 900)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)


class QEditor(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.edit_list = QEditor_list()
        self.content = QEditor_block()
        self.resize(900, 1000)
        self.layout.addWidget(self.edit_list)
        self.layout.addWidget(self.content)


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QEditor()
    w.show()
    sys.exit(app.exec_())
