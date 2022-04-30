from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from pyqtgraph import PlotWidget, plot, PlotDataItem
import pyqtgraph


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('main_window.ui', self)
        self.press_temp_data = [[], []]

    def update_press_temp_graph(self, pressure, temperature):
        self.press_temp_data[0].append(temperature)
        self.press_temp_data[1].append(pressure)
        self.press_temp.plot(self.press_temp_data)
