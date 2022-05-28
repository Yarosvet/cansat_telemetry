# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1340, 758)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(16, 16, 16);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.press_temp = PlotWidget(self.centralwidget)
        self.press_temp.setObjectName("press_temp")
        self.verticalLayout_2.addWidget(self.press_temp)
        self.temp_time = PlotWidget(self.centralwidget)
        self.temp_time.setObjectName("temp_time")
        self.verticalLayout_2.addWidget(self.temp_time)
        self.acc_time = PlotWidget(self.centralwidget)
        self.acc_time.setObjectName("acc_time")
        self.verticalLayout_2.addWidget(self.acc_time)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gas_time = PlotWidget(self.centralwidget)
        self.gas_time.setObjectName("gas_time")
        self.verticalLayout_3.addWidget(self.gas_time)
        self.hum_time = PlotWidget(self.centralwidget)
        self.hum_time.setObjectName("hum_time")
        self.verticalLayout_3.addWidget(self.hum_time)
        self.bright_time = PlotWidget(self.centralwidget)
        self.bright_time.setObjectName("bright_time")
        self.verticalLayout_3.addWidget(self.bright_time)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(391, 200))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/img/img/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.horizontalLayout_17.addWidget(self.logo)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_14.addWidget(self.label)
        self.pressure_lab = QtWidgets.QLabel(self.centralwidget)
        self.pressure_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pressure_lab.setFont(font)
        self.pressure_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.pressure_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressure_lab.setObjectName("pressure_lab")
        self.horizontalLayout_14.addWidget(self.pressure_lab)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_14)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.pressure_imu_lab = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_imu_lab.sizePolicy().hasHeightForWidth())
        self.pressure_imu_lab.setSizePolicy(sizePolicy)
        self.pressure_imu_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pressure_imu_lab.setFont(font)
        self.pressure_imu_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.pressure_imu_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressure_imu_lab.setObjectName("pressure_imu_lab")
        self.horizontalLayout_7.addWidget(self.pressure_imu_lab)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.temperature_lab = QtWidgets.QLabel(self.centralwidget)
        self.temperature_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.temperature_lab.setFont(font)
        self.temperature_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.temperature_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperature_lab.setObjectName("temperature_lab")
        self.horizontalLayout_6.addWidget(self.temperature_lab)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.temperature_imu_lab = QtWidgets.QLabel(self.centralwidget)
        self.temperature_imu_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.temperature_imu_lab.setFont(font)
        self.temperature_imu_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.temperature_imu_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperature_imu_lab.setObjectName("temperature_imu_lab")
        self.horizontalLayout_5.addWidget(self.temperature_imu_lab)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.humidity_lab = QtWidgets.QLabel(self.centralwidget)
        self.humidity_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.humidity_lab.setFont(font)
        self.humidity_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.humidity_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.humidity_lab.setObjectName("humidity_lab")
        self.horizontalLayout_9.addWidget(self.humidity_lab)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_15.addWidget(self.label_3)
        self.tx_time_lab = QtWidgets.QLabel(self.centralwidget)
        self.tx_time_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tx_time_lab.setFont(font)
        self.tx_time_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.tx_time_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_time_lab.setObjectName("tx_time_lab")
        self.horizontalLayout_15.addWidget(self.tx_time_lab)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.acceleration_lab = QtWidgets.QLabel(self.centralwidget)
        self.acceleration_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.acceleration_lab.setFont(font)
        self.acceleration_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.acceleration_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.acceleration_lab.setObjectName("acceleration_lab")
        self.horizontalLayout_13.addWidget(self.acceleration_lab)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_12.addWidget(self.label_14)
        self.acceleration_imu_lab = QtWidgets.QLabel(self.centralwidget)
        self.acceleration_imu_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.acceleration_imu_lab.setFont(font)
        self.acceleration_imu_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.acceleration_imu_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.acceleration_imu_lab.setObjectName("acceleration_imu_lab")
        self.horizontalLayout_12.addWidget(self.acceleration_imu_lab)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_11.addWidget(self.label_16)
        self.methane_lab = QtWidgets.QLabel(self.centralwidget)
        self.methane_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.methane_lab.setFont(font)
        self.methane_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.methane_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.methane_lab.setObjectName("methane_lab")
        self.horizontalLayout_11.addWidget(self.methane_lab)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_4.addWidget(self.label_18)
        self.hydrogen_lab = QtWidgets.QLabel(self.centralwidget)
        self.hydrogen_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.hydrogen_lab.setFont(font)
        self.hydrogen_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.hydrogen_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hydrogen_lab.setObjectName("hydrogen_lab")
        self.horizontalLayout_4.addWidget(self.hydrogen_lab)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_10.addWidget(self.label_20)
        self.brightness_lab = QtWidgets.QLabel(self.centralwidget)
        self.brightness_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.brightness_lab.setFont(font)
        self.brightness_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.brightness_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.brightness_lab.setObjectName("brightness_lab")
        self.horizontalLayout_10.addWidget(self.brightness_lab)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_16.addWidget(self.label_7)
        self.magnetic_lab = QtWidgets.QLabel(self.centralwidget)
        self.magnetic_lab.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.magnetic_lab.setFont(font)
        self.magnetic_lab.setStyleSheet("color: rgb(0, 208, 16);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.magnetic_lab.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.magnetic_lab.setObjectName("magnetic_lab")
        self.horizontalLayout_16.addWidget(self.magnetic_lab)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 bold 12pt \"Consolas\";")
        self.tabWidget.setObjectName("tabWidget")
        self.map_tab = QtWidgets.QWidget()
        self.map_tab.setObjectName("map_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.map_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.map_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_6.addWidget(self.graphicsView)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.map_tab, "")
        self.inclination_tab = QtWidgets.QWidget()
        self.inclination_tab.setObjectName("inclination_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.inclination_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_3.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.inclination_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CanSat Telemetry Receiver"))
        self.label.setText(_translate("MainWindow", "Pressure"))
        self.pressure_lab.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Pressure IMU"))
        self.pressure_imu_lab.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Temperature"))
        self.temperature_lab.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Temperature IMU"))
        self.temperature_imu_lab.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Humidity"))
        self.humidity_lab.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "TX time"))
        self.tx_time_lab.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "Acceleration"))
        self.acceleration_lab.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "Acceleration IMU"))
        self.acceleration_imu_lab.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Methane"))
        self.methane_lab.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Hydrogen"))
        self.hydrogen_lab.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "Brightness"))
        self.brightness_lab.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Magnetic"))
        self.magnetic_lab.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.map_tab), _translate("MainWindow", "Map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inclination_tab), _translate("MainWindow", "Inclination"))
from pyqtgraph import PlotWidget
import res_rc
