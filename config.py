# connect setting
IP = '192.168.1.127'
PORT = 1621
ADDRESS = (IP, PORT)
BUFFER_SIZE = 1024

# command for card reader
CMD_CLEAR_ALL = [0x7E, 0x04, 0x01, 0x2D, 0xD3, 0x01]
CMD_READ_LAST = [0x7E, 0x04, 0x01, 0x25, 0xDB, 0x01]
CMD_CLEAR_LAST = [0x7E, 0x04, 0x01, 0x37, 0xC9, 0x01]
