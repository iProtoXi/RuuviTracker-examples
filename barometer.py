import pyb, time
from pyb import I2C

dataBaro = bytearray(3)
dataTemp = bytearray(2)

i2c.mem_write(0xE0, 0x5C, 0x20) #init barometer
while 1:
	i2c.mem_read(dataBaro, 0x5C, 0xA8)
	i2c.mem_read(dataTemp, 0x5C, 0xAB)
	mBar = (dataBaro[2]*16 + dataBaro[1]/16)
	temp = (-(0xFFFF ^ (dataTemp[1]*256 +dataTemp[0])+1))/480+42.5
	print(mBar, '   \t', temp)
	time.sleep(0.1)