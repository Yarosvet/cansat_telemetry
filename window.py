from PyQt5.QtWidgets import QMainWindow
import pyqtgraph as pg
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtGui
from main_window import Ui_MainWindow
from config import *
from rx_serial import SerialReader
import numpy as np


def first_items(l):
    return np.array([el[0] for el in l])


def sec_items(l):
    return np.array([el[1] for el in l])


def xy(l):
    return [first_items(l), sec_items(l)]


class MainWindow(QMainWindow):
    def __init__(self, serial: SerialReader):
        super().__init__()
        self.serial = serial
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Pressure - temperature
        pen_sensor = pg.mkPen(color=(00, 208, 10), width=2, style=Qt.SolidLine)
        pen_imu = pg.mkPen(color=(255, 218, 0), width=2, style=Qt.SolidLine)
        pen_methane = pg.mkPen(color=(255, 24, 0), width=2, style=Qt.SolidLine)
        pen_hydrogen = pg.mkPen(color=(7, 118, 160), width=2, style=Qt.SolidLine)
        self.press_temp_curve = self.ui.press_temp.plot(name="PressTemp", pen=pen_sensor)
        self.press_temp_imu_curve = self.ui.press_temp.plot(name="PressTempImu", pen=pen_imu)
        self.temp_time_curve = self.ui.temp_time.plot(name="TempTime", pen=pen_sensor)
        self.temp_time_imu_curve = self.ui.temp_time.plot(name="TempTimeImu", pen=pen_imu)
        self.methane_curve = self.ui.gas_time.plot(name="MethaneTime", pen=pen_methane)
        self.hydrogen_curve = self.ui.gas_time.plot(name="HydrogenTime", pen=pen_hydrogen)
        self.humidity_curve = self.ui.hum_time.plot(name="HumidityTime", pen=pen_sensor)
        self.brightness_curve = self.ui.bright_time.plot(name="BrightnessTime", pen=pen_sensor)
        self.accelerate_curve = self.ui.acc_time.plot(name="AccelerationTime", pen=pen_sensor)
        self.accelerate_imu_curve = self.ui.acc_time.plot(name="AccelerationTimeImu", pen=pen_imu)
        self.timer_update = QTimer()
        self.timer_update.timeout.connect(self.update_graphs)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.timer_update.start(INTERVAL_GRAPHS_UPDATE)

    def update_graphs(self):
        self.press_temp_curve.setData(*xy(self.serial.presstemp_data))
        self.press_temp_imu_curve.setData(*xy(self.serial.presstemp_imu_data))
        self.temp_time_curve.setData(*xy(self.serial.temptime_data))
        self.temp_time_imu_curve.setData(*xy(self.serial.temptime_imu_data))
        self.hydrogen_curve.setData(*xy(self.serial.hydrogen_time_data))
        self.methane_curve.setData(*xy(self.serial.methane_time_data))
        self.humidity_curve.setData(*xy(self.serial.humidity_time_data))
        self.brightness_curve.setData(*xy(self.serial.brightness_time_data))
        self.accelerate_curve.setData(*xy(self.serial.accelerate_time_data))
        self.accelerate_imu_curve.setData(*xy(self.serial.accelerate_time_imu_data))
