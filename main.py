from window import MainWindow
from rx_serial import SerialReader
import sys
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    ser = SerialReader()
    ser.start_imitation_rx()
    window = MainWindow(ser)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
