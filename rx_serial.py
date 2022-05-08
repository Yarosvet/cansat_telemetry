import serial
from config import *
from time import sleep
from threading import Thread
from random import randint


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
        self.press_data = []
        self.temp_data = []

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
            self.press_data.append(self.pressure)
            self.press_data.sort()
            self.temp_data.append(self.temperature)
            self.temp_data.sort()
            sleep(0.032)
