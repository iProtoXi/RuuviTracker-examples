import array, time
from array import array

currentLimit = array('B', [0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01])
logDimm = array('B', [0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20])
dataPage0 = array('B', [0x00, 0x9F, 0xA0, 0x40, 0x00, 0x9F, 0xA1, 0x04, 0xFF, 0x9D, 0x07, 0x03, 0x05, 0x9D, 0x04, 0x02, 0x05, 0xB9, 0x84, 0x9D, 0x02, 0x03, 0x05, 0x9D, 0x03, 0x02, 0x05, 0xB9, 0x89, 0x9D, 0x04, 0x03, 0x05])
dataPage1 = array('B', [0x01, 0x9D, 0x05, 0x02, 0x05, 0xB9, 0x8E, 0x9D, 0x03, 0x03, 0x05, 0x9D, 0x09, 0x02, 0x05, 0xB9, 0x93, 0x9D, 0x05, 0x03, 0xFF, 0x9D, 0x09, 0x05, 0xFF])
dataPage2 = array('B', [0x02, 0x01, 0xFF, 0x00, 0x42])
i2c.mem_write(0xFF, 0x34, 0x3D) #reset board
i2c.mem_write(0x40, 0x34, 0x00) #enable
i2c.mem_write(0x10, 0x34, 0x01) #load
i2c.mem_write(0x5B, 0x34, 0x36) #auto increment, cp auto, internal clock
i2c.mem_write(currentLimit[:], 0x34, 0x26) #current limit 0.1mA
i2c.mem_write(logDimm[:], 0x34, 0x06)
time.sleep(0.001)
i2c.mem_write(dataPage0[:31], 0x34, 0x4F) 
i2c.mem_write(dataPage0[31:33], 0x34, 0x6E)
i2c.mem_write(dataPage1[:], 0x34, 0x4F)
i2c.mem_write(dataPage2[:], 0x34, 0x4F)
i2c.mem_write(0x20, 0x34, 0x01) #run engine 1
i2c.mem_write(0x60, 0x34, 0x00) #free run engine 1
