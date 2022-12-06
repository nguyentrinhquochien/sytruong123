# Closed-loop motor encoder control of Robot’s trajectory
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
    # Define the functions:
    def readencoder():
        global temp1
        global temp2
        global xung_left
        global xung_right
        global goc_encoder
        global quangduong
        global w_goc
        
    def __init__(self):
        self.temp1 = 0
        self.temp2 = 0
        self.xung_left = 0
        self.xung_right = 0
        self.goc_encoder = 0
        self.quangduong = 0
        self.w_goc = 0

        if GPIO.input(20) == 1:
            if self.temp1 == 0:
                self.xung_left=self.xung_left+1
                self.temp1 = 1
            if GPIO.input(27) != self.temp1:
                self.xung_left += 1
            else:
                self.temp1 = 0
        if GPIO.input(27) == 1:
            if self.temp2 == 0:
                self.xung_right=self.xung_right+1
                self.temp2 = 1
            if GPIO.input(20) != self.temp2:
                self.xung_right += 1
            else:
                self.temp2 = 0

        self.goc_encoder = (self.xung_left - self.xung_right) * 0.0015
        self.quangduong = (self.xung_left + self.xung_right) * 0.0015
        self.w_goc = self.goc_encoder / 0.01

    def setmotor(self, pwm1, pwm2, pwm3, pwm4):
        PWM.set_duty_cycle("P9_14", pwm1)
        PWM.set_duty_cycle("P9_16", pwm2)
        PWM.set_duty_cycle("P8_19", pwm3)
        PWM.set_duty_cycle("P8_13", pwm4)

    def stop(self):
        PWM.set_duty_cycle("P9_14", 0)
        PWM.set_duty_cycle("P9_16", 0)
        PWM.set_duty_cycle("P8_19", 0)
        PWM.set_duty_cycle("P8_13", 0)

    def forward(self, pwm):
        GPIO.output("P8_8", GPIO.HIGH)
        GPIO.output("P8_10", GPIO.LOW)
        GPIO.output("P8_12", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.LOW)
        PWM.set_duty_cycle("P9_14", pwm)
        PWM.set_duty_cycle("P9_16", 0)
        PWM.set_duty_cycle("P8_19", pwm)
        PWM.set_duty_cycle("P8_13", 0)  
        
    def backward(self, pwm):
        GPIO.output("P8_8", GPIO.LOW)
        GPIO.output("P8_10", GPIO.HIGH)
        GPIO.output("P8_12", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)
        PWM.set_duty_cycle("P9_14", 0)
        PWM.set_duty_cycle("P9_16", pwm)
        PWM.set_duty_cycle("P8_19", 0)
        PWM.set_duty_cycle("P8_13", pwm)
        
        
    def turnleft(self, pwm):
        GPIO.output("P8_8", GPIO.LOW)
        GPIO.output("P8_10", GPIO.HIGH)
        GPIO.output("P8_12", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.LOW)
        PWM.set_duty_cycle("P9_14", 0)
        PWM.set_duty_cycle("P9_16", pwm)
        PWM.set_duty_cycle("P8_19", pwm)
        PWM.set_duty_cycle("P8_13", 0)
        
        
    def turnright(self, pwm):
        GPIO.output("P8_8", GPIO.HIGH)
        GPIO.output("P8_10", GPIO.LOW)
        GPIO.output("P8_12", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)
        PWM.set_duty_cycle("P9_14", pwm)
        PWM.set_duty_cycle("P9_16", 0)
        PWM.set_duty_cycle("P8_19", 0)
        PWM.set_duty_cycle("P8_13", pwm)
        
        
    
    
    # Define the variables:
    pwm = 100
    pwm1 = 0
    pwm2 = 0
    pwm3 = 0
    pwm4 = 0
    xung_left = 0
    xung_right = 0
    goc_encoder = 0
    quangduong = 0
    w_goc = 0
    temp1 = 0
    temp2 = 0
    encoder1 = 0
    encoder2 = 0
    
    # Define the main program:
    readencoder()
    print("xung_left = ", xung_left)
    print("xung_right = ", xung_right)
    print("goc_encoder = ", goc_encoder)
    print("quangduong = ", quangduong)
    print("w_goc = ", w_goc)
    print("pwm1 = ", pwm1)
    
    if goc_encoder > 0:
        turnright(pwm)
    elif goc_encoder < 0:
        turnleft(pwm)
    else:
        forward(pwm)
    
    
    time.sleep(0.01)    
    
    
    # Stop the program:
    stop()
    PWM.stop("P9_14")
    PWM.stop("P9_16")
    PWM.stop("P8_19")
    PWM.stop("P8_13")
    PWM.cleanup()
    GPIO.cleanup()
    break
x = raw_input()

if x == "w":
    forward(pwm)
    
elif x == "s":
    backward(pwm)
    
elif x == "a":
    turnleft(pwm)

    
elif x == "d":
    turnright(pwm)
    
elif x == "q":
    stop()
    PWM.stop("P9_14")
    PWM.stop("P9_16")
    PWM.stop("P8_19")
    PWM.stop("P8_13")
    PWM.cleanup()
    GPIO.cleanup()





