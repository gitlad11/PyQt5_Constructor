
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QCursor, QIcon, QPixmap
import sys


class QIcon_Button(Qt.QPushButton):
    def __init__(self, icon, toolTip=None):
        super().__init__()
        self.icon = icon
        self.toolTip = toolTip

        self.setStyleSheet('border: 0px;')

        if self.toolTip:
            self.setToolTip(str(self.toolTip))
            self.setToolTipDuration(4000)


        self.setStyleSheet("""QToolTip { 
                           background-color: rgba(50, 50, 50, 1); 
                           color: white;
                           border-radius: 4px 4px 4px 4px; 
                           border: #fff solid 1px
                           } 
                           QPushButton { border: 0px; } """)
        self.Icon = QIcon()
        self.pix = QPixmap(str(self.icon))
        self.pix.scaled(QSize(27, 27))
        self.Icon.addPixmap(self.pix)   
        self.setIcon(self.Icon)
        
        self.setFixedWidth(20)
        self.setFixedHeight(20)


        self.cursor_pix = QPixmap('cursor-dark2.png')  
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(21, 21), QtCore.Qt.KeepAspectRatio) 
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.setCursor(self.current_cursor)
        

class Window(Qt.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.btn = QIcon_Button(icon="angle-left.png", toolTip="Назад")
        self.btn2 = QIcon_Button(icon="angle-right.png", toolTip="Вперед")
        self.btn3 = QIcon_Button(icon="folder.png", toolTip="Сохранить")
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.setLayout(self.layout)



if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())