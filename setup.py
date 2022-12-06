# Control the robot according to a given trajectory
import sys
import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.Encoder as Encoder
import math
import numpy as np


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


# Define the robot class
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0
        self.wheel_radius = 0.034
        self.wheel_distance = 0.2
        self.encoder_resolution = 600
        self.encoder1 = 0
        self.encoder2 = 0
        self.temp1 = 0
        self.temp2 = 0
        self.xung_left = 0
        self.xung_right = 0
        self.goc_encoder = 0
        self.quangduong = 0
        self.w_goc = 0
        self.Distance = 0
        self.wheel_distance = 0.2
        self.wheel_radius = 0.034
        self.encoder_resolution = 600
        
        
        
        
    def readEncoder(self):
        self.encoder1 = Encoder.read("P8_15")
        self.encoder2 = Encoder.read("P8_16")
        self.xung_left = self.encoder1 - self.temp1
        self.xung_right = self.encoder2 - self.temp2
        self.goc_encoder = (self.xung_left - self.xung_right) * 2 * math.pi / self.encoder_resolution
        self.quangduong = (self.xung_left + self.xung_right) * math.pi * self.wheel_radius / self.encoder_resolution
        self.w_goc = self.goc_encoder / 0.1
        self.Distance = self.quangduong / 0.1
        self.temp1 = self.encoder1
        self.temp2 = self.encoder2
        return self.goc_encoder, self.quangduong, self.w_goc, self.Distance
    
    def updateOdometry(self):
        self.theta += self.readEncoder()[0]
        self.x += self.readEncoder()[1] * math.cos(self.theta)
        self.y += self.readEncoder()[1] * math.sin(self.theta)
        return self.x, self.y, self.theta
    
    def setMotor(self, left, right):
        if left > 0:
            GPIO.output("P8_8", GPIO.HIGH)
            GPIO.output("P8_10", GPIO.LOW)
            PWM.set_duty_cycle("P9_14", left)
        else:
            GPIO.output("P8_8", GPIO.LOW)
            GPIO.output("P8_10", GPIO.HIGH)
            PWM.set_duty_cycle("P9_14", -left)
        if right > 0:
            GPIO.output("P8_12", GPIO.HIGH)
            GPIO.output("P8_14", GPIO.LOW)
            PWM.set_duty_cycle("P9_16", right)
        else:
            GPIO.output("P8_12", GPIO.LOW)
            GPIO.output("P8_14", GPIO.HIGH)
            PWM.set_duty_cycle("P9_16", -right)
        
        
while True:
    print ("nhap quang duong: ")
    Distance = float(input())
    
    
    robot = Robot()
    robot.setMotor(0, 0)
    time.sleep(1)
    robot.setMotor(50, 50)
    time.sleep(1)
    robot.setMotor(0, 0)
    time.sleep(1)
    robot.setMotor(50, 50)
    time.sleep(1)
    
    
    while robot.readEncoder()[3] < Distance:
        robot.setMotor(50, 50)
        print (robot.readEncoder()[3])
        time.sleep(0.1)
    robot.setMotor(0, 0)
    time.sleep(1)
    robot.setMotor(50, 50)
    time.sleep(1)
   
    x=raw_input()
    if x == "w":
        GPIO.output("P8_8", GPIO.HIGH)
        GPIO.output("P8_10", GPIO.LOW)
        GPIO.output("P8_12", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.LOW)
        PWM.set_duty_cycle("P9_14", 100)
        PWM.set_duty_cycle("P9_16", 100)
        PWM.set_duty_cycle("P8_19", 100)
        PWM.set_duty_cycle("P8_13", 100)
        
    elif x=='s':
        GPIO.output("P8_8", GPIO.LOW)
        GPIO.output("P8_10", GPIO.HIGH)
        GPIO.output("P8_12", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)
        PWM.set_duty_cycle("P9_14", 100)
        PWM.set_duty_cycle("P9_16", 100)
        PWM.set_duty_cycle("P8_19", 100)
        PWM.set_duty_cycle("P8_13", 100)
        
    elif x=='a':
        GPIO.output("P8_8", GPIO.LOW)
        GPIO.output("P8_10", GPIO.HIGH)
        GPIO.output("P8_12", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.LOW)
        PWM.set_duty_cycle("P9_14", 100)
        PWM.set_duty_cycle("P9_16", 100)
        PWM.set_duty_cycle("P8_19", 100)
        PWM.set_duty_cycle("P8_13", 100)
        
        
    elif x=='d':
        GPIO.output("P8_8", GPIO.HIGH)
        GPIO.output("P8_10", GPIO.LOW)
        GPIO.output("P8_12", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)
        PWM.set_duty_cycle("P9_14", 100)
        PWM.set_duty_cycle("P9_16", 100)
        PWM.set_duty_cycle("P8_19", 100)
        PWM.set_duty_cycle("P8_13", 100)
        
    elif x=='q':
        GPIO.output("P8_8", GPIO.LOW)
        GPIO.output("P8_10", GPIO.LOW)
        GPIO.output("P8_12", GPIO.LOW)
        GPIO.output("P8_14", GPIO.LOW)
        PWM.set_duty_cycle("P9_14", 0)
        PWM.set_duty_cycle("P9_16", 0)
        PWM.set_duty_cycle("P8_19", 0)
        PWM.set_duty_cycle("P8_13", 0)
        
        
    elif x == 'l':
        print ("Small")
        PWM.set_duty_cycle("P9_14", 50)
        PWM.set_duty_cycle("P9_16", 50)
        PWM.set_duty_cycle("P8_19", 50)
        PWM.set_duty_cycle("P8_13", 50)
        
        
    elif x == 'm':
        print ("medium")
        PWM.set_duty_cycle("P9_14", 100)
        PWM.set_duty_cycle("P9_16", 100)
        PWM.set_duty_cycle("P8_19", 100)
        PWM.set_duty_cycle("P8_13", 100)
        
        
    elif x == 'h':
        print ("high")
        PWM.set_duty_cycle("P9_14", 150)
        PWM.set_duty_cycle("P9_16", 150)
        PWM.set_duty_cycle("P8_19", 150)
        PWM.set_duty_cycle("P8_13", 150)
        
        
    elif x == 'f':
        print ("full")
        PWM.set_duty_cycle("P9_14", 200)
        PWM.set_duty_cycle("P9_16", 200)
        PWM.set_duty_cycle("P8_19", 200)
        PWM.set_duty_cycle("P8_13", 200)