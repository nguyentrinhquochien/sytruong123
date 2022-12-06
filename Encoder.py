# Wheel diameter: Dn = 6.5mm
# pi = 3.14
# Wheel circumference: Dn*pi=6.5*3.14=20.41cm
# Encoder resolution 600 pulses/rev
# Number of cm/1 pulse=204.1/600=0.03401666667cm

# Initialize class to access eQEP2 channel and initialize only that channel
# Write a program to read the encoder to measure the distance

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time


# Set the GPIO pins:
GPIO.setup("P8_8", GPIO.OUT)
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_12", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)


# Set the PWM pins:
PWM.start("P9_14", 0)
PWM.start("P9_16", 0)
PWM.start("P8_19", 0)
PWM.start("P8_13", 0)


# Read encoder
encoder1 = 0
encoder2 = 0

GPIO.setup("P8_15", GPIO.IN)
GPIO.setup("P8_16", GPIO.IN)


while True:
    