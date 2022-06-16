from PyQt5.QtWidgets import QMainWindow
import pyqtgraph as pg
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtGui
from main_window import Ui_MainWindow
from config import *
from rx_serial import SerialReader
import numpy as np
from math import sqrt
from datetime import timedelta
import vtkplotlib as vpl
from stl.mesh import Mesh


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
        self.ui.press_temp.addLegend((1, 1))
        self.ui.temp_time.addLegend((1, 1))
        self.ui.acc_time.addLegend((1, 1))
        self.ui.gas_time.addLegend((1, 1))
        self.ui.press_temp.setLabels(left=("Pressure", "Pa"), bottom=("Temperature", "°C"))
        self.ui.temp_time.setLabels(left=("Temperature", "°C"), bottom=("Time", "Sec"))
        self.ui.acc_time.setLabels(left=("Acceleration module", "msec²"), bottom=("Time", "Sec"))
        self.ui.gas_time.setLabels(left=("Gas concentration", "ppm"), bottom=("Time", "Sec"))
        self.ui.hum_time.setLabels(left=("Humidity", "%"), bottom=("Time", "Sec"))
        self.ui.bright_time.setLabels(left=("Brightness", "V"), bottom=("Time", "Sec"))
        pen_sensor = pg.mkPen(color=(00, 208, 16), width=2, style=Qt.SolidLine)
        pen_imu = pg.mkPen(color=(255, 218, 0), width=2, style=Qt.SolidLine)
        pen_methane = pg.mkPen(color=(255, 24, 0), width=2, style=Qt.SolidLine)
        pen_hydrogen = pg.mkPen(color=(7, 118, 160), width=2, style=Qt.SolidLine)
        self.press_temp_curve = self.ui.press_temp.plot(name="Sensor", pen=pen_sensor)
        self.press_temp_imu_curve = self.ui.press_temp.plot(name="Imu", pen=pen_imu)
        self.temp_time_curve = self.ui.temp_time.plot(name="Temperature", pen=pen_sensor)
        self.temp_time_imu_curve = self.ui.temp_time.plot(name="Temperature Imu", pen=pen_imu)
        self.methane_curve = self.ui.gas_time.plot(name="Methane", pen=pen_methane)
        self.hydrogen_curve = self.ui.gas_time.plot(name="Hydrogen", pen=pen_hydrogen)
        self.humidity_curve = self.ui.hum_time.plot(name="Humidity", pen=pen_sensor)
        self.brightness_curve = self.ui.bright_time.plot(name="Brightness", pen=pen_sensor)
        self.accelerate_curve = self.ui.acc_time.plot(name="Acceleration module", pen=pen_sensor)
        self.accelerate_imu_curve = self.ui.acc_time.plot(name="Acceleration module Imu", pen=pen_imu)
        self.timer_update = QTimer()
        self.timer_update.timeout.connect(self.update_values)
        # self.mesh_figure = Mesh.from_file("3d/base.stl")
        # vpl.mesh_plot(self.mesh_figure, fig=self.ui.inclination_widget)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.timer_update.start(INTERVAL_GRAPHS_UPDATE)

    def update_realtime_value(self, label, text):
        if not text.replace(".", "").replace("-", "").isdigit():
            label.setText(text)
            return
        if float(text) >= float(label.text()):
            label.setStyleSheet("color: rgb(0, 208, 16);\nfont: 75 bold 12pt \"Consolas\";")
        else:
            label.setStyleSheet("color: rgb(255, 61, 51);\nfont: 75 bold 12pt \"Consolas\";")
        label.setText(text)

    def update_values(self):
        # Updating graphs
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
        # Updating real-time values
        self.update_realtime_value(self.ui.pressure_lab, str(int(self.serial.pressure)))
        self.update_realtime_value(self.ui.pressure_imu_lab, str(int(self.serial.pressure_imu)))
        self.update_realtime_value(self.ui.temperature_lab, str(self.serial.temperature))
        self.update_realtime_value(self.ui.temperature_imu_lab, str(self.serial.temperature_imu))
        self.update_realtime_value(self.ui.humidity_lab, str(int(self.serial.humidity)))
        acc_mod = round(sqrt(abs(self.serial.acc_ax ** 2 + self.serial.acc_ay ** 2 + self.serial.acc_az)) * 10) / 10
        acc_mod_imu = round(
            sqrt(abs(self.serial.acc_ax_imu ** 2 + self.serial.acc_ay_imu ** 2 + self.serial.acc_az_imu)) * 10) / 10
        self.update_realtime_value(self.ui.acceleration_lab, str(acc_mod))
        self.update_realtime_value(self.ui.acceleration_imu_lab, str(acc_mod_imu))
        self.update_realtime_value(self.ui.hydrogen_lab, str(int(self.serial.hydrogen)))
        self.update_realtime_value(self.ui.methane_lab, str(int(self.serial.methane)))
        self.update_realtime_value(self.ui.brightness_lab, str(self.serial.brightness))
        tx_time = timedelta(seconds=round(self.serial.time_start))
        self.update_realtime_value(self.ui.tx_time_lab, str(tx_time))
        magnetic_mod = round(sqrt(abs(self.serial.mag_mx ** 2 + self.serial.mag_my ** 2 + self.serial.mag_mz ** 2)))
        self.update_realtime_value(self.ui.magnetic_lab, str(magnetic_mod))
