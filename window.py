from PyQt5.QtWidgets import QMainWindow
import pyqtgraph as pg
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtGui
from main_window import Ui_MainWindow
from config import *
from rx_serial import SerialReader
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self, serial: SerialReader):
        super().__init__()
        self.serial = serial
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Pressure - temperature
        self.press_temp_curve = self.ui.press_temp.plot(name="PressTemp",
                                                        pen=pg.mkPen(color=(00, 208, 10), width=3, style=Qt.SolidLine))
        self.timer_update = QTimer()
        self.timer_update.timeout.connect(self.update_graphs)
        self.press_temp_data = [np.array([]), np.array([])]

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.timer_update.start(INTERVAL_GRAPHS_UPDATE)

    def update_graphs(self):
        self.press_temp_curve.setData(np.array(self.serial.temp_data), np.array(self.serial.press_data))
