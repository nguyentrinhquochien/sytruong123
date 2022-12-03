#write a program to read raspberry encoder motor
import RPi.GPIO as GPIO
import time
import numpy as np
from gpiozero import RotaryEncoder
from time import sleep
prr = 300
pstop = 20
tsamte = 0.01
tdisp = 0.5
encoder = RotaryEncoder(17, 18)
encoder.max_steps = 1000
encoder.steps = 0
encoder.when_rotated = lambda steps: encoder.steps
print ("Encoder Test")
anglecurr = 0
angleprev = 0
angle = 0
while True:
    anglecurr = encoder.steps
    angle = anglecurr - angleprev
    angleprev = anglecurr
    print (angle)
    sleep(0.1)
    