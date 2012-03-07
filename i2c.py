__author__ = 'romilly'

import fcntl

IOCTL_I2C_SLAVE = 0x0703

class I2C_device:

    def __init__(self, address):
        self.address = address
        self.fh = None

    def begin_transmission(self):
        if self.fh:
            self.end_transmission()
            raise Exception('already open. (Now closed)')
        self.fh = open('/dev/i2c-3', 'r+', 1)
        fcntl.ioctl(self.fh, IOCTL_I2C_SLAVE, self.address)

    def write(self, bytes):
        if not self.fh:
            raise Exception('must open before write')
        self.fh.write(bytes)
        self.fh.flush()

    def end_transmission(self):
        self.fh.close()
        self.fh = None
  
