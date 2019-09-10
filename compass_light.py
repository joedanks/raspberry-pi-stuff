""" Display both accelerometer and magnetometer data once per second """

import time
import board
import busio
import adafruit_lsm303
import math
from express import cpx

cpx.pixels.brightness = 0.3
cpx.pixels.fill((0, 0, 0))

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm303.LSM303(i2c)

def computeDirectionPixel (degrees):
    if degrees >= 342 or degrees < 18:
        return [7]
    if 324 <= degrees < 342:
        return [7,8]
    if 306 <= degrees < 324:
        return [8]
    if 288 <= degrees < 306:
        return [8,9]
    if 252 <= degrees < 288:
        return [9,0]
    if 234 <= degrees < 252:
        return [0,1]
    if 216 <= degrees < 234:
        return [1]
    if 198 <= degrees < 216:
        return [1,2]
    if 162 <= degrees < 198:
        return [2]
    if 144 <= degrees < 162:
        return [2,3]
    if 126 <= degrees < 144:
        return [3]
    if 108 <= degrees < 126:
        return [3,4]
    if 72 <= degrees < 108:
        return [4,5]
    if 54 <= degrees < 72:
        return [5,6]
    if 36 <= degrees < 54:
        return [6]
    if 18 <= degrees < 36:
        return [6,7]

def turnPixelOn(index):
    cpx.pixels[index] = (255,0,0)

while True:
    acc_x, acc_y, acc_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic

    print('Acceleration (m/s^2): ({0:10.3f}, {1:10.3f}, {2:10.3f})'.format(acc_x, acc_y, acc_z))
    print('Magnetometer (gauss): ({0:10.3f}, {1:10.3f}, {2:10.3f})'.format(mag_x, mag_y, mag_z))

    if mag_x is not 0:
        deg = math.atan2(mag_y,mag_x) * (180/math.pi)
        if deg < 0:
            deg = deg + 360
        if deg > 360:
            deg = deg - 360
        cpx.pixels.fill((0, 0, 0))
        directions = computeDirectionPixel(deg)
        for x in directions:
            turnPixelOn(x)
        print('Degrees: {}'.format(deg))

    print('')
    time.sleep(1.0)