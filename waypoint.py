import time
import board
import busio
import adafruit_lsm303
import adafruit_gps
import math
import gps_calc
from express import cpx

##### GPS ####################
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
##### GPS End ################

##### Compass ################
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm303.LSM303(i2c)
##### Compass End ############

cpx.pixels.brightness = 0.3

last_print = time.monotonic()
current_fix = False

waypoint = None
dist = None
bearing = None

def listen_to_set_waypoint():
    if cpx.button_a:
        if gps.has_fix:
            waypoint = (gps.latitude, gps.longitude)
            print('Waypoint set to ({0:.6f},{0:.6f})'.format(gps.latitude, gps.longitude))
        else:
            print('Unable to set waypoint. No GPS fix.')
        while cpx.button_a:
            continue

def turnDistPixelsOn():
    if dist is not None:
        cpx.pixels.fill((0, 0, 0))
        x = math.trunc(dist / 5)
        for n in range(x, 9):
            cpx.pixels[n] = (0,255,0)

def turnBearingPixelOn():
    if bearing is not None:
        cpx.pixels.fill((0,0,0))
        for x in gps_calc.computeDirectionPixel(bearing):
            cpx.pixels[x] = (0,0,255)

def displayPixelsOnSwitch():
    if cpx.switch:
        turnBearingPixelOn()
    else:
        turnDistPixelsOn()

print('Searching for satellites...')
while True:
    gps.update()

    listen_to_set_waypoint()

    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current

        acc_x, acc_y, acc_z = sensor.acceleration
        mag_x, mag_y, mag_z = sensor.magnetic

        if not gps.has_fix and current_fix:
            print('Lost GPS fix')
            current_fix = False
            cpx.pixels.fill((255,0,0))
            continue
        else if gps.has_fix and not current_fix:
            print('GPS fix established')
            current_fix = True

        if current_fix and waypoint is not None:
            (dist, bearing) = gps_calc.calcDistAndBearing((gps.latitude, gps.longitude), waypoint)
            displayPixelsOnSwitch()

            


