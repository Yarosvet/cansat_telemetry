import serial
from config import *
from time import sleep


class SerialReader:
    def __init__(self):
        self.ser = serial.Serial(COM_PORT, SERIAL_PORT)

    def rx(self):
        while True:
            cc = str(self.ser.readline())

    def imitate_rx(self):
        while True:
            cc = "161 10 144 0 0 192  8 16 31 157 0 160 40 72 112 0 0 0 0 0 16 0 0 0 0 0 1716 21 0 0 0"
