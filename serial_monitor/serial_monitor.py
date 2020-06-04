import serial
import serial.tools.list_ports
from threading import Thread


# Serial port class
class Port:
    def __init__(self, device, baudrate=9600):
        self.device = device
        self.baudrate = baudrate
        self.port = None

    def connect(self):
        self.port = serial.Serial(self.device, self.baudrate, timeout=0.1)

    def disconnect(self):
        if self.port is not None:
            self.port.close()

    def send(self, command):
        self.port.write(bytes(command, encoding='utf-8'))

    def read(self):
        return self.port.readline()


# Refresh comports and return list
def comports_refresh():
    return list(serial.tools.list_ports.comports())
