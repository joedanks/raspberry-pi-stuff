import time
import board
import busio
import adafruit_lsm303
import adafruit_gps
import math

### GPS
#   circuit python
RX = board.RX
TX = board.TX
uart = busio.UART(TX, RX, baudrate=9600, timeout=30)
#   raspberry pi
#import serial
#uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)

gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
gps.send_command(b'PMTK220,1000')

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm303.LSM303(i2c)

last_print = time.monotonic()
current_fix = False
print('Searching for satellites...')
while True:
    gps.update()

    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current

        acc_x, acc_y, acc_z = sensor.acceleration
        mag_x, mag_y, mag_z = sensor.magnetic

        if not gps.has_fix and current_fix:
            print('Lost GPS fix')
            continue
        else if gps.has_fix and not current_fix:
            print('GPS fix established')
            current_fix = True


