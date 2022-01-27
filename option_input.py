import subprocess
from tabnanny import check
import time

import PyQt5
from PyQt5 import Qt, QtCore
import pyqtgraph as pg
import numpy as np
import os, sys
import threading
import psutil
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QLabel,QLineEdit, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect,  QCheckBox
import datetime
import ctypes


class QInput(QFrame):
    def __init__(self, title, value=None):
        super().__init__()
        self.title = title
        self.value = value
        self.layout = Qt.QHBoxLayout(self)
        self.setFixedHeight(35)
        self.setFixedWidth(295)

        self.label = QLabel(str(self.title))
        self.label.setFont(QFont("Helvetica", 10))
        self.input = QLineEdit(self)
        self.setStyleSheet("""QFrame { 
                        
                            background-color: rgba(40, 40, 40, 1); 
                            color: white;
                            border-radius: 4px 4px 4px 4px; 
                           
                           } 
                           QLineEdit { 
                               border: 1px inset gray;
                               margin: 0px 7px 0px 0px
                           } 
                           QLabel {
                               font-weight: bold
                           }
                           """)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)

class QFourInputs(QFrame):
    def __init__(self, title, v1=None, v2=None, v3=None, v4=None):
        super().__init__()
        self.title = title
        
        self.layout = Qt.QHBoxLayout(self)
        self.setFixedHeight(35)
        self.setFixedWidth(295)

        self.label = QLabel(str(self.title))
        self.label.setFont(QFont("Helvetica", 10))

        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.input3 = QLineEdit(self)
        self.input4 = QLineEdit(self)
        self.input1.setFixedWidth(35)
        self.input2.setFixedWidth(35)
        self.input3.setFixedWidth(35)
        self.input4.setFixedWidth(35)

        self.setStyleSheet("""QFrame { 
                           
                            background-color: rgba(40, 40, 40, 1); 
                            color: white;
                            border-radius: 4px 4px 4px 4px; 
                       
                           } 
                           QLineEdit { 
                               border: 1px inset gray;
                               margin: 0px 7px 0px 0px
                           } 
                           QLabel {
                               font-weight: bold
                           }
                           """)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.input2)
        self.layout.addWidget(self.input3)
        self.layout.addWidget(self.input4)
        
        self.setLayout(self.layout)

class QTwoInputs(QFrame):
    def __init__(self,  title, label1, label2, v1=None, v2=None):
        super().__init__()
        self.title = title
        self.l = label1
        self.l2 = label2
        self.layout = Qt.QHBoxLayout(self)
        self.setFixedHeight(35)
        self.setFixedWidth(295)

        self.label = QLabel(str(self.title))
        self.label.setFont(QFont("Helvetica", 10))
        
        self.label1 = QLabel(str(self.l))
        self.label1.setFont(QFont("Helvetica", 10))

        self.label2 = QLabel(str(self.l2))
        self.label2.setFont(QFont("Helvetica", 10))

        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)

        self.input1.setFixedWidth(35)
        self.input2.setFixedWidth(35)


        self.setStyleSheet("""QFrame { 
                            
                            background-color: rgba(40, 40, 40, 1); 
                            color: white;
                            border-radius: 4px 4px 4px 4px; 
                       
                           } 
                           QLineEdit { 
                               border: 1px inset gray;
                               margin: 0px 7px 0px 0px
                           }
                           QLabel {
                               font-weight: bold
                           }
                            """)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.input2)

        self.setLayout(self.layout)
    
class QCheckInput(QFrame):
        def __init__(self, title, checked=False):
            super().__init__()
            self.checked = checked
            self.title = title

            self.layout = Qt.QHBoxLayout(self)
            self.setFixedHeight(35)
            self.setFixedWidth(155)
           
            self.label = QLabel(str(self.title))
            self.label.setFont(QFont("Helvetica", 10))

            self.setStyleSheet("""QFrame { 
                            
                            background-color: rgba(40, 40, 40, 1); 
                            color: white;
                            border-radius: 4px 4px 4px 4px; 
                       
                           } 
                           QLabel {
                               font-weight: bold
                           }
                            """)

            self.checkbox = QCheckBox()
            self.checkbox.setFixedWidth(13)
            self.checkbox.setFixedHeight(13)
            self.layout.addWidget(self.label)
            self.layout.addWidget(self.checkbox)

            self.setLayout(self.layout)

            