from PyQt5 import QtWidgets
from ui import qt_design
from serial_monitor import serial_monitor

# Convert qt.ui in qt_design.py by using this command from the terminal app:
# pyuic5 qt.ui -o qt_design.py


# Window builder class
class SerialDisposerApp(QtWidgets.QMainWindow, qt_design.Ui_MainWindow):
    def __init__(self):
        # Init window
        super().__init__()
        self.setupUi(self)
        # Variables
        self.port = None
        # Update ports list than refresh button is clicked
        self.pushButton_refresh.clicked.connect(lambda: self.refresh_ports())
        # Connect to the selected port
        self.pushButton_connect.clicked.connect(lambda: self.connect_port())

    # Refresh ports list in comboBox
    def refresh_ports(self):
        self.comboBox_ports.clear()
        for item in serial_monitor.comports_refresh():
            self.comboBox_ports.addItem(item.device)

    # Connect to the selected port
    def connect_port(self):
        device = self.comboBox_ports.currentText()
        baudrate = self.comboBox_baudrate.currentText()
        if device is not None:
            self.port = serial_monitor.Port(device, baudrate)
            self.port.connect()