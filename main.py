import subprocess
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
from PyQt5.QtWidgets import QLabel, QFrame, QToolBar, QAction, QStatusBar, QGraphicsDropShadowEffect
import datetime


class Process_Thread(QThread):
    signal = QtCore.pyqtSignal(list)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.processes = []
        self.running = False


    def run(self):
        self.running = True
        while self.running:
            self.process_count()
            self.sleep(1)

    def process_count(self):
        for proc in psutil.process_iter():
            try:
                process_name = proc.name()
                process_id = proc.pid
                process = {int(process_id): str(process_name)}
                if process not in self.processes:
                    self.processes.append(process)
                else:
                    return

                self.signal.emit(self.processes)

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


class Graph_Thread(QThread):
    signal = QtCore.pyqtSignal(float)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.positions = np.array([0, 0, 0, 0, 0, 0, 0])
        self.running = False

    def run(self):
        self.random_plot()

    def random_plot(self):
        self.running = True
        while self.running:
            cpu = psutil.cpu_percent()
            time.sleep(1)
            self.signal.emit(cpu)



class Window(Qt.QWidget):

    def __init__(self):
        super().__init__()
        self.layout = Qt.QVBoxLayout(self)

        self.positions = np.array([0, 0, 0, 0, 0, 0, 0])
        self.processes_running = 0
        self.view = view = pg.PlotWidget()
        self.pen = pg.mkPen(color=(255, 255, 0), width=2)

        self.curve = view.plot(name="Line", pen=self.pen, )
        self.view.setBackground((30, 35, 35))

        self.view.setTitle("Performance", color="w", size="12pt")
        self.view.showGrid(x=True, y=True)
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(0, 0)
        effect.setBlurRadius(15)

        self.gh_thread = Graph_Thread()
        self.gh_thread.start()
        self.gh_thread.signal.connect(self.onchange)


        self.red_palette = self.palette()
        self.red_palette.setColor(QPalette.Window, QColor(255, 100, 100))
        self.blue_palette = self.palette()
        self.blue_palette.setColor(QPalette.Window, QColor(100, 100, 255))
        self.yellow_palette = self.palette()
        self.yellow_palette.setColor(QPalette.Window, QColor(160, 255, 0))
        self.purple_palette = self.palette()
        self.purple_palette.setColor(QPalette.Window, QColor(100, 100, 255))
        self.setPalette(self.red_palette)
        self.layout.addWidget(self.view)
        self.view.setLabel('left', 'Percentage', color="white", size='8pt', units='%')
        self.resize(360, 300)

    def onchange(self, s):

        if len(self.positions) < 100:
            array2 = np.append(self.positions, s)
            self.positions = array2
        else:
            new_array = np.delete(self.positions, 0, 0)
            n_array = np.append(new_array, s)
            self.positions = n_array

        self.curve.setData(self.positions)

        if s > 30:
            self.setPalette(self.yellow_palette)
        elif s > 50:
            self.setPalette(self.purple_palette)
        elif s > 70:
            self.setPalette(self.red_palette)
        else:
            self.setPalette(self.blue_palette)

        print(self.positions)

    def closeEvent(self, event):

        self.hide()
        self.gh_thread.running = False
        self.gh_thread.wait(2000)

        event.accept()


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())