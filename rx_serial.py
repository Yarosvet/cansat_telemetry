import serial
from config import *
from time import sleep
from threading import Thread


class SerialReader:
    def __init__(self, func_press_temp):
        self.func_press_temp = func_press_temp

    def start_rx(self):
        self.rx_thread = Thread(target=self.rx, name="rxThread")
        self.rx_thread.start()

    def start_imitation_rx(self):
        self.rx_thread = Thread(target=self.imitate_rx, name="rxThread")
        self.rx_thread.start()

    def rx(self):
        self.ser = serial.Serial(COM_PORT, SERIAL_PORT)
        while True:
            cc = str(self.ser.readline())
            time_start = cc[0]
            pressure = cc[1]
            acc_ax = cc[2]
            acc_ay = cc[3]
            acc_az = cc[4]
            temperature = cc[5]
            pressure_imu = cc[6]
            acc_ax_imu = cc[7]
            acc_ay_imu = cc[8]
            acc_az_imu = cc[9]
            temperature_imu = cc[10]
            mag_mx = cc[11]
            mag_my = cc[12]
            mag_mz = cc[13]
            gyr_x = cc[14]
            gyr_y = cc[15]
            gyr_z = cc[16]
            brightness = cc[17]
            humidity = cc[18]
            methane = cc[19]
            hydrogen = cc[20]

    def imitate_rx(self):
        while True:
            cc = list(map(float, "1000 101325 0 0 -9 25.5 101325 0 0 -9 25.5 9 9 9 0 0 200 3.75 46 500 600".split()))
            time_start = cc[0]
            pressure = cc[1]
            acc_ax = cc[2]
            acc_ay = cc[3]
            acc_az = cc[4]
            temperature = cc[5]
            pressure_imu = cc[6]
            acc_ax_imu = cc[7]
            acc_ay_imu = cc[8]
            acc_az_imu = cc[9]
            temperature_imu = cc[10]
            mag_mx = cc[11]
            mag_my = cc[12]
            mag_mz = cc[13]
            gyr_x = cc[14]
            gyr_y = cc[15]
            gyr_z = cc[16]
            brightness = cc[17]
            humidity = cc[18]
            methane = cc[19]
            hydrogen = cc[20]
            self.func_press_temp(pressure, temperature)
            sleep(0.03)
