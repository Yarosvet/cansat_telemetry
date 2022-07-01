from window import MainWindow
from rx_serial import SerialReader
import sys
from PyQt5.QtWidgets import QApplication
from dialog import DeviceDialog
from db import db_session
from config import *


def main():
    db_session.global_init(DB_FILE)
    app = QApplication(sys.argv)
    ser = SerialReader()
    window = MainWindow(ser)
    ser.eventClose = window.close
    dialog = DeviceDialog(ser, window)
    dialog.show()
    # window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
