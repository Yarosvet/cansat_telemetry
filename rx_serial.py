import serial
from config import *
from time import sleep
from threading import Thread
from random import randint
from math import sqrt


class SerialReader:
    def __init__(self):
        self.com_port = "COM11"
        self.serial_port = 9600
        self.alive = True
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
        self.gps_lat = 0
        self.gps_lon = 0
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

    def update_from_str(self, s):
        # "time=1000 pressure=101325 acc_ax=0 acc_ay=0 acc_az=-9 temperature=25.5 pressure_imu=101325 acc_ax_imu=0
        # acc_ay_imu=0 acc_az_imu=-9 temperature_imu=25.5 mag_mx=9 mag_my=9 mag_mz=9 gyr_x=0 gyr_y=0 gyr_z=200
        # brightness=3.75 humidity=46 methane=500 hydrogen=600 gps_lat=54.22 gps_lon=36.55"
        kvalues = list(map(lambda x: (x.split("=")[0], float(x.split("=")[1])), s.split()))
        for k, v in kvalues:
            if k == "time":
                self.time_start = v / 1000
            elif k == "pressure":
                self.pressure = v
            elif k == "acc_ax":
                self.acc_ax = v
            elif k == "acc_ay":
                self.acc_ay = v
            elif k == "acc_az":
                self.acc_az = v
            elif k == "temperature":
                self.temperature = v
            elif k == "pressure_imu":
                self.pressure_imu = v
            elif k == "acc_ax_imu":
                self.acc_ax_imu = v
            elif k == "acc_ay_imu":
                self.acc_ay_imu = v
            elif k == "acc_az_imu":
                self.acc_az_imu = v
            elif k == "temperature_imu":
                self.temperature_imu = v
            elif k == "mag_mx":
                self.mag_mx = v
            elif k == "mag_my":
                self.mag_my = v
            elif k == "mag_mz":
                self.mag_mz = v
            elif k == "gyr_x":
                self.gyr_x = v
            elif k == "gyr_y":
                self.gyr_y = v
            elif k == "gyr_z":
                self.gyr_z = v
            elif k == "brightness":
                self.brightness = v
            elif k == "humidity":
                self.humidity = v
            elif k == "methane":
                self.methane = v
            elif k == "hydrogen":
                self.hydrogen = v
            elif k == "gps_lat":
                self.gps_lat = v
            elif k == "gps_lon":
                self.gps_lon = v
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
        mod_acc = sqrt(abs(self.acc_ax ** 2 + self.acc_ay ** 2 + self.acc_az ** 2))
        self.accelerate_time_data.append([self.time_start, mod_acc])
        mod_acc_imu = sqrt(abs(self.acc_ax_imu ** 2 + self.acc_ay_imu ** 2 + self.acc_az_imu ** 2))
        self.accelerate_time_imu_data.append([self.time_start, mod_acc_imu])

    def rx(self):
        ser = serial.Serial(self.com_port, self.serial_port)
        try:
            while True:
                self.update_from_str(ser.readline().decode("utf-8"))
        except serial.serialutil.SerialException:
            self.alive = False

    def imitate_rx(self):
        time_start = 0
        while True:
            time_start += 32
            s = f"time={time_start} pressure={randint(90000, 102000)} acc_ax={randint(-9, 0)}" \
                f" acc_ay={randint(-9, 0)} acc_az={randint(-9, 0)} " \
                f"temperature={randint(-90, 250) / 10} pressure_imu={randint(90000, 102000)}" \
                f" acc_ax_imu={randint(-9, 0)} acc_ay_imu={randint(-9, 0)} acc_az_imu={randint(-9, 0)}" \
                f" temperature_imu={randint(-90, 250) / 10} mag_mx={9} mag_my={9} mag_mz={9}" \
                f" gyr_x={randint(0, 15)} gyr_y={randint(0, 15)} gyr_z={randint(0, 15)}" \
                f" brightness={randint(100, 500) / 100} humidity={randint(10, 40)} methane={500} hydrogen={400}" \
                f" gps_lat={54 + randint(1, 99) / 100} gps_lon={36 + randint(1, 99) / 100}"
            self.update_from_str(s)
            sleep(0.032)
