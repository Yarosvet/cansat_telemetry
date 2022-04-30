from window import MainWindow
from rx_serial import SerialReader
import sys
from PyQt5.QtWidgets import QApplication


def main():
    # ser = SerialReader()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
