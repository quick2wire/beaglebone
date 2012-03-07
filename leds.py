__author__ = 'romilly'

import i2c, time


EXTENDER_SLAVE_ADDRESS = 0x20

extender = i2c.I2C_device(0x20)
extender.begin_transmission()
extender.write(bytearray([0,0]))

for count in range(0,255):
    extender.write(bytearray([9,count]))
    time.sleep(0.1)

extender.end_transmission()
