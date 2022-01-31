from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from item_list import QList
from directory_view import QDirectory
from options_menu import Options
from editor import QEditor

class QContent_block(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout()
        self.resize(800, 900)
     
        self.con = QEditor()
        self.con.setContentsMargins(0,0,0,0)
        self.con.resize(900, 600)
        self.con.setStyleSheet("background-color: #fff; ")

        self.directory = QDirectory()

        self.layout.addWidget(self.con)
        self.layout.addWidget(self.directory)
        self.layout.setContentsMargins(0, 0, 0, 0)
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