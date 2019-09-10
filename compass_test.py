""" Display both accelerometer and magnetometer data once per second """

import time
import board
import busio
import adafruit_lsm303
import math

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm303.LSM303(i2c)

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
        print('Degrees: {}'.format(deg))

    print('')
    time.sleep(1.0)