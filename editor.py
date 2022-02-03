from fileinput import close
import sys

from PyQt5 import Qt, QtCore, QtWidgets
from PyQt5.QtCore import QThread, QSize
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QColor
from icon_button import QIcon_Button
from PyQt5.QtWidgets import QScrollArea


class Tab(QtWidgets.QFrame):
    def __init__(self, title, icon=None, close_tab=None, index=None):
        super().__init__()
        self.title = title
        self.icon = icon
        self.index = index 
        self.close_tab = close_tab
        
        self.layout = Qt.QHBoxLayout(self)
        self.btn1 = QtWidgets.QPushButton()
        self.Icon = QIcon()
        self.btn1.setMaximumWidth(240)
        
        
        self.pix = QPixmap(str(self.icon))
        self.pix.scaled(QSize(24, 24))
        self.Icon.addPixmap(self.pix)   
        self.btn1.setIcon(self.Icon)
     
        self.btn1.setText(str(self.title))
        self.btn1.setFixedHeight(25)
        self.setContentsMargins(0, 0, 0, 0)
        self.close = QIcon_Button("icons/close.png", toolTip="Закрыть", height=26, width=26, onClick=self.close_tab, index=int(self.index))

        self.color1 = QColor(190, 190, 220)
        self.color2 = QColor(240, 240, 255)
        
        self.cursor_pix = QPixmap('cursor-dark2.png')  
        self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(21, 21), QtCore.Qt.KeepAspectRatio) 
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
        self.setCursor(self.current_cursor)

     
        self.setMinimumWidth(220)
        self.setMinimumHeight(36)
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
    def __init__(self, tabs, add_tab, close_tab):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.tabs = tabs
        self.add_tab = add_tab 
        self.close_tab = close_tab
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(50)
        self.setStyleSheet("background-color: rgba(40, 40, 40, 1); padding: 0px 2px 0px 0px;")
        self.add_btn = QIcon_Button(icon='icons/plus.png', fill=True, height=36, width=36, toolTip="Добавить сцену", onClick=self.add_tab)
       

        self.layout.addWidget(self.add_btn)
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        for index, item in enumerate(self.tabs):
            tab = Tab(title=item['name'], icon="icons/page.png", index=index, close_tab=self.close_tab)
            self.layout.addWidget(tab)


class QEditor_list(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QHBoxLayout(self)
        self.setStyleSheet(""" QFrame { background-color: rgba(170, 170, 200, 1); border: 1px solid gray; } QPushButton { border : 0px; } """)
        
        self.btn1 = QIcon_Button(icon='hand.png', fill=True, toolTip="обзор")
        self.btn2 = QIcon_Button(icon='editor.png', fill=True, toolTip='редактирование')
        self.btn3 = QIcon_Button(icon='expand.png', fill=True, toolTip='весь экран')

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
        self.setMinimumHeight(600)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)


class QEditor(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.tabs_list = [
            { 'name' : 'new page'},
            { 'name' : 'new page'},
            { 'name' : 'past page'}
        ]
        self.tabs = QTab_list(tabs=self.tabs_list, add_tab=self.add_tab, close_tab=self.close_tab)
        self.edit_list = QEditor_list()
        self.content = QEditor_block()
        self.setStyleSheet("background-color: rgba(40, 40, 40, 1);")
        self.resize(800, 1000)

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.tabs)
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.edit_list)
        self.layout.addWidget(self.content)
        self.layout.addStretch()

    def add_tab(self):
        self.tabs_list.append({ 'name' : 'new scene' })
        self.layout.itemAt(0).widget().deleteLater()
        tabs = QTab_list(tabs=self.tabs_list, add_tab=self.add_tab, close_tab=self.close_tab)
        self.layout.insertWidget(0, tabs)
          
    
    def close_tab(self, index):
        del self.tabs_list[index]
        self.layout.itemAt(0).widget().deleteLater()
        tabs = QTab_list(tabs=self.tabs_list, add_tab=self.add_tab, close_tab=self.close_tab)
        self.layout.insertWidget(0, tabs)
      

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = QEditor()
    w.show()
    sys.exit(app.exec_())
