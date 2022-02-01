import sys

from PyQt5 import Qt, QtCore, QtWidgets
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QColor
from icon_button import QIcon_Button


class Tab(QtWidgets.QFrame):
    def __init__(self, title, icon=None):
        super().__init__()
        self.title = title
        self.icon = icon 
        self.layout = Qt.QHBoxLayout(self)
        self.btn1 = QtWidgets.QPushButton()
        self.Icon = QIcon()
        self.btn1.setMaximumWidth(240)
        self.btn1.setMinimumWidth(200)
        
        self.pix = QPixmap(str(self.icon))
        self.pix.scaled(QSize(24, 24))
        self.Icon.addPixmap(self.pix)   
        self.btn1.setIcon(self.Icon)
        self.btn1.setIcon(self.Icon)
        self.btn1.setText(str(self.icon))
        self.btn1.setFixedHeight(30)
        self.setContentsMargins(0, 0, 0, 0)
        self.close = QIcon_Button("icons/close.png")

        self.color1 = QColor(200, 200, 230)
        self.color2 = QColor(230, 230, 255)
        
        self.cursor_pix = QPixmap('cursor-dark2.png')  
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(21, 21), QtCore.Qt.KeepAspectRatio) 
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.setCursor(self.current_cursor)

        self.setMaximumWidth(280)
        self.setMinimumWidth(220)
        self.setMinimumHeight(34)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.close)
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignTop)

        self.btn1.setStyleSheet("""
   
         QPushButton { 
            background-color: rgba(190, 190, 230, 0); 
           
            font: 75 9pt "Microsoft YaHei UI";
            font-weight: bold;
            border: 0px;
            color: #000;
            padding: 0px 4px 5px 5px;
            text-align: left;
             } """)
        self.setLayout(self.layout)
        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250
        )

    def _animate(self, value):
      
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        
        self.setStyleSheet(grad)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)




class QTab_list(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
     
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(50)
        self.setStyleSheet("background-color: rgba(40, 40, 40, 1); padding: 2px 2px 2px 2px;")
        self.tab = Tab(title="new page", icon="icons/page.png")
        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)


class QEditor_list(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.setStyleSheet(""" QFrame { background-color: rgba(170, 170, 200, 1); border: 1px solid gray; } QPushButton { border : 0px; } """)
        
        self.btn1 = QIcon_Button(icon='hand.png', fill=True)
        self.btn2 = QIcon_Button(icon='editor.png', fill=True)
        self.btn3 = QIcon_Button(icon='expand.png', fill=True)

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
        self.layout = Qt.QHBoxLayout(self)
        self.setStyleSheet(""" QFrame { border: 1px solid gray; background-color: rgba(10, 10, 10, 1); } """)
        self.resize(800, 1000)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)


class QEditor(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)

        self.tabs = QTab_list()
        self.edit_list = QEditor_list()
        self.content = QEditor_block()
        self.setStyleSheet("background-color: rgba(40, 40, 40, 1);")
        self.resize(1000, 1000)
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.edit_list)
        self.layout.addWidget(self.content)


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QEditor()
    w.show()
    sys.exit(app.exec_())
