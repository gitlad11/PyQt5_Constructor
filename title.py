from PyQt5 import Qt, QtCore, QtWidgets, QtGui

class Title(QtWidgets.QWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.layout = Qt.QVBoxLayout(self)
        self.setFixedHeight(20)
        self.label = QtWidgets.QLabel(str(self.title))
        self.label.setStyleSheet(""" QLabel { 
            font: 75 14pt "Microsoft YaHei UI";
            font-weight: bold;
            color: rgb(255, 255, 255);
            border-style: solid;
            border-radius:21px; } """)
      
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
