import sys

from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QLinearGradient, QColor, QBrush
from navbar import QNavBar
from content import QContent


class Index(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)

        p = QPalette()

        gradient = QLinearGradient(0, 0, 0, 700)
        self.color1 = QtGui.QColor(90, 90, 120)
        self.color2 = QtGui.QColor(30, 30, 40)
        self.navbar = QNavBar()
        self.content = QContent()
        gradient.setColorAt(0.0, self.color1)
        gradient.setColorAt(1.0, self.color2)
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        self.resize(1500, 900)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.addWidget(self.navbar)
        self.layout.addWidget(self.content)



if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = Index()
    w.show()
    sys.exit(app.exec_())
    