#! /usr/bin/python

import smbus
import math

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c


def read_byte(adr):
    return bus.read_byte_data(address, adr)


def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val


def read_word_2c(adr):
    val = read_word(adr)
    if val >= 0x8000:
        return -((65535 - val) + 1)
    else:
        return val


def dist(a, b):
    return math.sqrt((a*a) + (b*b))


def get_y_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degress(radians)


bus = smbus.SMBus(1)
address = 0x68

bus.write_byte_data(address, power_mgmt_1, 0)


gyro_xout = read_word_2c(0x43)
gyro_yout = read_word_2c(0x45)
gyro_zout = read_word_2c(0x47)

print("x: %f, y:%f, z:%f" % (gyro_xout, gyro_yout, gyro_zout))
