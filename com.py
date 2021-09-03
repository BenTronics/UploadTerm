import serial
import serial.tools.list_ports

com_handler = serial.Serial()
com_handler.timeout = 0.2

def open(port, baudrate):
    if com_handler.isOpen() == False:
        com_handler.port = "COM" + str(port)
        com_handler.baudrate = baudrate
        com_handler.open()

def close():
    if com_handler.isOpen() == True:
        com_handler.close()

def get_com_port_list():
    ports = []
    for port in (serial.tools.list_ports.comports()):
        ports.append(int((str(port)[3:]).split(" ", 1)[0]))
    return ports

def print(message):
    com_handler.write(message.encode("iso-8859-1"))

def println(message):
    com_handler.write((message + "\r\n").encode("iso-8859-1"))

def read(amount):
    return com_handler.read(amount).decode("iso-8859-1")

def read_line():
    return com_handler.readline().decode("iso-8859-1")