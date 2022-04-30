from PyQt5.QtWidgets import QMainWindow
from pyqtgraph import PlotWidget, plot, PlotDataItem
import pyqtgraph
from main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.press_temp_data = [[], []]

    def update_press_temp_graph(self, pressure, temperature):
        self.press_temp_data[0].append(temperature)
        self.press_temp_data[1].append(pressure)
        self.press_temp.plot(self.press_temp_data)
