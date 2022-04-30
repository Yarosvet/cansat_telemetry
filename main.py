from window import MainWindow
from rx_serial import SerialReader
import sys
from PyQt5.QtWidgets import QApplication


def main():
    # ser = SerialReader()
    app = QApplication(sys.argv)
    window = MainWindow()
    ser = SerialReader(window.update_press_temp_graph)
    ser.start_imitation_rx()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
