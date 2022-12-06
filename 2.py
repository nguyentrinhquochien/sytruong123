# Closed-loop motor encoder and IMU by Diego C
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import smbus
import math


GPIO.setup("P8_8", GPIO.OUT)
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_12", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)
GPIO.setup("P8_15", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P8_16", GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.output("P8_8", GPIO.HIGH)
GPIO.output("P8_10", GPIO.LOW)
GPIO.output("P8_12", GPIO.HIGH)
GPIO.output("P8_14", GPIO.LOW)
GPIO.clearup()

PWM.start("P9_14", 0)
PWM.start("P9_16", 0)
PWM.start("P8_19", 0)
PWM.start("P8_13", 0)

# Read encoder
encoder1 = 0    
encoder2 = 0

# Read IMU
bus = smbus.SMBus(2) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command


# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, 0x6b, 0)

# Power management registers
