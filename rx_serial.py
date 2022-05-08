import serial
from config import *
from time import sleep
from threading import Thread
from random import randint
from math import sqrt


class SerialReader:
    def __init__(self):
        # Values
        self.time_start = 0
        self.pressure = 0
        self.acc_ax = 0
        self.acc_ay = 0
        self.acc_az = 0
        self.temperature = 0
        self.pressure_imu = 0
        self.acc_ax_imu = 0
        self.acc_ay_imu = 0
        self.acc_az_imu = 0
        self.temperature_imu = 0
        self.mag_mx = 0
        self.mag_my = 0
        self.mag_mz = 0
        self.gyr_x = 0
        self.gyr_y = 0
        self.gyr_z = 0
        self.brightness = 0
        self.humidity = 0
        self.methane = 0
        self.hydrogen = 0
        # Data sets
        self.presstemp_data = []
        self.presstemp_imu_data = []
        self.temptime_data = []
        self.temptime_imu_data = []
        self.hydrogen_time_data = []
        self.methane_time_data = []
        self.humidity_time_data = []
        self.brightness_time_data = []
        self.accelerate_time_data = []
        self.accelerate_time_imu_data = []

    def start_rx(self):
        self.rx_thread = Thread(target=self.rx, name="rxThread", daemon=True)
        self.rx_thread.start()

    def start_imitation_rx(self):
        self.rx_thread = Thread(target=self.imitate_rx, name="rxThread", daemon=True)
        self.rx_thread.start()

    def update_from_str(self, s):  # "1000 101325 0 0 -9 25.5 101325 0 0 -9 25.5 9 9 9 0 0 200 3.75 46 500 600"
        cc = list(map(float, s.split()))
        self.time_start = cc[0]
        self.pressure = cc[1]
        self.acc_ax = cc[2]
        self.acc_ay = cc[3]
        self.acc_az = cc[4]
        self.temperature = cc[5]
        self.pressure_imu = cc[6]
        self.acc_ax_imu = cc[7]
        self.acc_ay_imu = cc[8]
        self.acc_az_imu = cc[9]
        self.temperature_imu = cc[10]
        self.mag_mx = cc[11]
        self.mag_my = cc[12]
        self.mag_mz = cc[13]
        self.gyr_x = cc[14]
        self.gyr_y = cc[15]
        self.gyr_z = cc[16]
        self.brightness = cc[17]
        self.humidity = cc[18]
        self.methane = cc[19]
        self.hydrogen = cc[20]
        # Updating datasets
        self.presstemp_data.append([self.temperature, self.pressure])
        self.presstemp_data.sort()
        self.presstemp_imu_data.append([self.temperature_imu, self.pressure_imu])
        self.presstemp_imu_data.sort()
        self.temptime_data.append([self.time_start, self.temperature])
        self.temptime_imu_data.append([self.time_start, self.temperature_imu])
        self.hydrogen_time_data.append([self.time_start, self.hydrogen])
        self.methane_time_data.append([self.time_start, self.methane])
        self.humidity_time_data.append([self.time_start, self.humidity])
        self.brightness_time_data.append([self.time_start, self.brightness])
        mod_acc = sqrt(self.acc_ax ** 2 + self.acc_ay ** 2 + self.acc_az ** 2)
        self.accelerate_time_data.append([self.time_start, mod_acc])
        mod_acc_imu = sqrt(self.acc_ax_imu ** 2 + self.acc_ay_imu ** 2 + self.acc_az_imu ** 2)
        self.accelerate_time_imu_data.append([self.time_start, mod_acc_imu])

    def rx(self):
        ser = serial.Serial(COM_PORT, SERIAL_PORT)
        while True:
            self.update_from_str(str(ser.readline()))

    def imitate_rx(self):
        time_start = 0
        while True:
            time_start += 32
            s = " ".join(map(str, [time_start, randint(90000, 102000), randint(-9, 0), randint(-9, 0), randint(-9, 0),
                                   randint(-90, 250) / 10, randint(90000, 102000), randint(-9, 0), randint(-9, 0),
                                   randint(-9, 0), randint(-90, 250) / 10, 9, 9, 9, randint(0, 15), randint(0, 15),
                                   randint(0, 15), randint(100, 500) / 100, randint(10, 40), 500, 400]))
            self.update_from_str(s)
            sleep(0.032)
