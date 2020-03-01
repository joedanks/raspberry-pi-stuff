import time
import board
import busio
import adafruit_lsm303
import adafruit_gps
import math
import gps_calc
import digitalio

##### GPS ####################
#   circuit python
#RX = board.RX
#TX = board.TX
#uart = busio.UART(TX, RX, baudrate=9600, timeout=30)
#   raspberry pi
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)

gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
gps.send_command(b'PMTK220,1000')
##### GPS End ################

##### Compass ################
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm303.LSM303(i2c)
##### Compass End ############

last_print = time.monotonic()
current_fix = False

waypoint = None
dist = None
bearing = None

button = digitalio.DigitalInOut(board.D21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

def listen_to_set_waypoint():
    if not button.value:
        if gps.has_fix:
            global waypoint
            waypoint = (gps.latitude, gps.longitude)
            print(waypoint)
            print('Waypoint set to ({:.6f},{:.6f})'.format(waypoint[0], waypoint[1]))
        else:
            print('Unable to set waypoint. No GPS fix.')
        while not button.value:
            continue

#def turnDistPixelsOn():
#    if dist is not None:
#        pixels.fill((0, 255, 0))
#        x = math.trunc(dist / 5)
#        for n in range(x, 9):
#            pixels[n] = (0,0,0)

#def turnBearingPixelOn():
#    if bearing is not None:
#        pixels.fill((0,0,0))
#        for x in gps_calc.computeDirectionPixel(bearing):
#            pixels[x] = (0,0,255)

#def displayPixelsOnSwitch():
#    if switch.value:
#        turnBearingPixelOn()
#    else:
#        turnDistPixelsOn()

print('Searching for satellites...')
while True:
    gps.update()
    listen_to_set_waypoint()
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        mag_x, mag_y, mag_z = sensor.magnetic
        if gps.has_fix and not current_fix:
            print("Satellites fixed")
            current_fix = True
        if gps.has_fix and waypoint is not None:
            (dist, direction) = gps_calc.calcDistAndBearing((gps.latitude, gps.longitude), waypoint)
            heading = math.atan2(mag_y, mag_x) * (180 / math.pi)
            bearing = math.fabs(heading - direction)
            print("Distance: {}".format(dist))
            print("Bearing: {}".format(bearing))
#            displayPixelsOnSwitch()
