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
        self.eventClose = None

    def start_rx(self):
        self.rx_thread = Thread(target=self.rx, name="rxThread", daemon=True)
        self.rx_thread.start()

    def start_imitation_rx(self):
        self.rx_thread = Thread(target=self.imitate_rx, name="rxThread", daemon=True)
        self.rx_thread.start()

    def update_from_str(self, s):
        kvalues = dict()
        for el in s.split():
            kvalues[el.split("=")[0]] = float(el.split("=")[1])
        if "time" in kvalues.keys():
            self.time_start = kvalues["time"]
        if "press" in kvalues.keys():
            self.pressure = kvalues["press"]
        if "acc_ax" in kvalues.keys():
            self.acc_ax = kvalues["acc_ax"]
        if "acc_ay" in kvalues.keys():
            self.acc_ay = kvalues["acc_ay"]
        if "acc_az" in kvalues.keys():
            self.acc_az = kvalues["acc_az"]
        if "temp" in kvalues.keys():
            self.temperature = kvalues["temp"]
        if "press_imu" in kvalues.keys():
            self.pressure_imu = kvalues["press_imu"]
        if "acc_ax_imu" in kvalues.keys():
            self.acc_ax_imu = kvalues["acc_ax_imu"]
        if "acc_ay_imu" in kvalues.keys():
            self.acc_ay_imu = kvalues["acc_ay_imu"]
        if "acc_az_imu" in kvalues.keys():
            self.acc_az_imu = kvalues["acc_az_imu"]
        if "temp_imu" in kvalues.keys():
            self.temperature_imu = kvalues["temp_imu"]
        if "mag_mx" in kvalues.keys():
            self.mag_mx = kvalues["mag_mx"]
        if "mag_my" in kvalues.keys():
            self.mag_my = kvalues["mag_my"]
        if "mag_mz" in kvalues.keys():
            self.mag_mz = kvalues["mag_mz"]
        if "gyr_x" in kvalues.keys():
            self.gyr_x = kvalues["gyr_x"]
        if "gyr_y" in kvalues.keys():
            self.gyr_y = kvalues["gyr_y"]
        if "gyr_z" in kvalues.keys():
            self.gyr_z = kvalues["gyr_z"]
        if "bright" in kvalues.keys():
            self.brightness = kvalues["bright"]
        if "hum" in kvalues.keys():
            self.humidity = kvalues["hum"]
        if "methane" in kvalues.keys():
            self.methane = kvalues["methane"]
        if "hydrogen" in kvalues.keys():
            self.hydrogen = kvalues["hydrogen"]
        if "gps_lat" in kvalues.keys():
            self.gps_lat = kvalues["gps_lat"]
        if "gps_lon" in kvalues.keys():
            self.gps_lon = kvalues["gps_lon"]
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
        while True:
            try:
                self.update_from_str(ser.readline().decode("utf-8"))
            except serial.serialutil.SerialException:
                if self.eventClose:
                    self.eventClose()

    def imitate_rx(self):
        time_start = 0
        while True:
            time_start += 32
            s = " ".join(map(str, ["time=" + str(time_start), "press=" + str(randint(90000, 102000)),
                                   "acc_ax=" + str(randint(-9, 0)), "acc_ay=" + str(randint(-9, 0)),
                                   "acc_az=" + str(randint(-9, 0)),
                                   "temp=" + str(randint(-90, 250) / 10), "press_imu=" + str(randint(90000, 102000)),
                                   "acc_ax_imu=" + str(randint(-9, 0)), "acc_ay_imu=" + str(randint(-9, 0)),
                                   "acc_az_imu=" + str(randint(-9, 0)), "temp_imu=" + str(randint(-90, 250) / 10),
                                   "mag_mx=9", "mag_my=9", "mag_mz=9", "gyr_x=" + str(randint(0, 15)),
                                   "gyr_y=" + str(randint(0, 15)),
                                   "gyr_z=" + str(randint(0, 15)), "bright=" + str(randint(100, 500) / 100),
                                   "hum=" + str(randint(10, 40)), "methane=500", "hydrogen=400",
                                   "gps_lat=" + str(54 + randint(1, 99) / 100),
                                   "gps_lon=" + str(36 + randint(1, 99) / 100)]))
            self.update_from_str(s)
            sleep(0.032)
