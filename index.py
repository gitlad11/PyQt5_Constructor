import sys

from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QLinearGradient, QColor, QBrush


class Index(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)

        p = QPalette()

        gradient = QLinearGradient(0, 0, 0, 400)
        self.color1 = QtGui.QColor(144, 70, 251)
        self.color2 = QtGui.QColor(74, 216, 241)
        gradient.setColorAt(0.0, self.color2)
        gradient.setColorAt(1.0, self.color1)
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        self.resize(1200, 900)


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = Index()
    w.show()
    sys.exit(app.exec_())
    