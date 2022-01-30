from PyQt5 import Qt, QtCore, QtGui, QtWidgets

class QSizedBox(Qt.QFrame):
    def __init__(self, color=None, height=0, width=0):
        super().__init__()
        self.color = color
        self.height = height
        self.width = width

        self.layout = Qt.QHBoxLayout(self)
        self.setFixedHeight(self.height)
        self.setFixedWidth(self.width)

        if self.color:
            self.setStyleSheet(""" QFrame { background-color: %s; } """ % self.color)