from PyQt5.QtWidgets import QDialog
from device_dialog import Ui_Dialog
from rx_serial import SerialReader
from serial.tools.list_ports import comports


class DeviceDialog(QDialog):
    def __init__(self, serial: SerialReader, main_window):
        super().__init__()
        self.main_window = main_window
        self.serial = serial
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.OkPressed)
        for el in comports():
            self.ui.com_port.addItem(str(el), userData=el.device)
        self.ui.com_port.addItem("Imitation mode", userData="imitation")

    def OkPressed(self):
        self.serial.com_port = self.ui.com_port.currentData()
        self.serial.serial_port = self.ui.serial_port.value()
        if self.ui.com_port.currentData() == "imitation":
            self.serial.start_imitation_rx()
        else:
            self.serial.start_rx()
        self.close()
        self.main_window.show()
