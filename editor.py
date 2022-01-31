from PyQt5 import Qt, QtCore, QtWidgets
from icon_button import QIcon_Button

class Edit_btn(QtWidgets.QPushButton):
    def __init__(self, icon, onClick=None):
        super().__init__(self)
        self.icon = icon
        self.onClick = onClick
        self.btn = QIcon_Button(self.icon, self.onClick)
        self.setStyleSheet("border-right: 1px solid gray")


class QEditor_list(QtWidgets.QFrame):
    def __init__(self):
        super().__init__(self)
        self.layout = Qt.QHBoxLayout(self)
        self.setStyleSheet(""" QFrame { background-color: #fff; border: 1px solid gray; } QPushButton { border : 0px; } """)
        
        self.btn1 = Edit_btn('hand.png')
        self.btn2 = Edit_btn('editor.png')
        self.btn2 = Edit_btn('expand.png')

        self.layout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.layout)


class QEditor_block(QtWidgets.QFrame):
    def __init__(self):
        super().__init__(self)
        self.setStyleSheet(""" QFrame { border: 1px solid gray; background-color: rgba(10, 10, 10, 1); } """)
        self.resize(800, 900)
        self.setLayout(self.layout)


class QEditor(QtWidgets.QFrame):
    def __init__(self):
        super().__init__(self)
        self.layout = Qt.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.edit_list = QEditor_list()
        self.content = QEditor_block()

        self.layout.addWidget(self.edit_list)
        self.layout.addWidget(self.content)