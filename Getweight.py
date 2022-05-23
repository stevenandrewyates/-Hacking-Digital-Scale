

import serial
import os
import time
from datetime import datetime

ser = serial.Serial(
    port='COM1',
    baudrate=9600,
    timeout=1,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.write(b'DSR')
now = datetime.now()
current_time = now.strftime("%Y:%m:%d %H:%M:%S")
print(current_time , ser.readline())
ser.close()
