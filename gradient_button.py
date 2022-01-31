from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QCursor


class GradientButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(60, 40)

        self.color1 = QtGui.QColor(240, 53, 218)
        self.color2 = QtGui.QColor(61, 217, 245)

        self.cursor_pix = QPixmap('cursor-dark2.png')
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(18, 18), QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.setCursor(self.current_cursor)
        self.setText("add component")
        
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
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    lay = QtWidgets.QVBoxLayout(w)

    lay.addStretch()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())