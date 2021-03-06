from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from item_list import QList
from directory_view import QDirectory_view
from options_menu import Options
from editor import QEditor

class QContent_block(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout()
       
     
        self.con = QEditor()
        self.setStyleSheet(""" QFrame { background-color: rgba(40, 40, 40, 0); padding: 0px 0px 0px 0px; } """)
        self.directory = QDirectory_view()

        self.layout.addWidget(self.con)
        self.layout.addWidget(self.directory)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        

class QContent(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(QtCore.Qt.AlignLeft)
        self.left_side = QList()
        self.content = QContent_block()
        self.right_side = Options()

        self.layout.addWidget(self.left_side)
        self.layout.addWidget(self.content)
        self.layout.addWidget(self.right_side)
        self.layout.addStretch()