import smbus
import math

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus = smbus.SMBus(1)
address = 0x68
bus.write_byte_data(address, power_mgmt_1, 0)

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

def gyro_data():
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)
    
    # [x, y, z]
    return [gyro_xout, gyro_yout, gyro_zout]

def accel_data():
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    # [x, y, z]
    return [accel_xout, accel_yout, accel_zout]

def dist(a, b):
    return math.sqrt((a*a) + (b*b))

def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)

def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)

def accel_rotation_data():
    [accel_xout, accel_yout, accel_zout] = accel_data()

    SCALED_FACTOR = 16384.0
    accel_xout_scaled = accel_xout / SCALED_FACTOR
    accel_yout_scaled = accel_yout / SCALED_FACTOR
    accel_zout_scaled = accel_zout / SCALED_FACTOR

    x_rotation = get_x_rotation(accel_xout_scaled, accel_yout_scaled,
                                accel_zout_scaled)
    y_rotation = get_y_rotation(accel_xout_scaled, accel_yout_scaled,
                                accel_zout_scaled)

    # [x, y]
    return [x_rotation, y_rotation]
