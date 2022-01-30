
from PyQt5 import Qt, QtCore

from PyQt5.QtWidgets import QFrame


class QMargin(QFrame):
    def __init__(self, item, top, left, bottom, right):
        super().__init__()
        self.item = item
        self.top = int(top)
        self.left = int(left)
        self.bottom = int(bottom)
        self.right = int(right)
        self.layout = Qt.QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setContentsMargins(self.top, self.left, self.bottom, self.right)
        self.layout.addWidget(self.item)
        self.setLayout(self.layout)
        self.setStyleSheet("border: 0px;")