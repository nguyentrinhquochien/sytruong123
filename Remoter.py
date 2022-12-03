# BeagleBone Black Remote-controlled


import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
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
            self.xung_left -= 1
    if GPIO.input(22) != self.temp2:
        self.temp2 = GPIO.input(22)
        if GPIO.input(27) != self.temp2:
            self.xung_right += 1
        else:
            self.xung_right -= 1
    print(self.xung_left)
    print(self.xung_right)
    sleep(0.01)
    
    
    
    
    

def PID_LEFT(self,setpoint,xung):
    vantoc=(xung*2*3.14)/(T*11*45)
    self.xung_left=0
    e_left = setpoint - vantoc
    P=KP*e_left
    esum_left=esum_left+e_left
    I=KI*esum_left*T
    D=KD*(e_left-esau_left)/T
    esau_left=e_left
    Output=P+D+I
    if(Output>255):
        Output=255
    if(Output<-255):
        Output=-255
    return Output
def PID_RIGHT(self,setpoint,xung):
    vantoc=(xung*2*3.14)/(T*11*45)
    self.xung_right=0
    e_right = setpoint - vantoc
    P=KP*e_right
    esum_right=esum_right+e_right
    I=KI*esum_right*T
    D=KD*(e_right-esau_right)/T
    esau_right=e_right
    Output=P+D+I
    if(Output>255):
        Output=255
    if(Output<-255):
        Output=-255
    return Output

while True:
    if GPIO.input("P8_15") == 1:
        encoder1 = encoder1 + 1
    if GPIO.input("P8_16") == 1:
        encoder2 = encoder2 + 1
    print ("Encoder 1: "), encoder1, "Encoder 2: ", encoder2
    time.sleep(0.1)

# Define the functions:
key = raw_input("Press a key to start: ")
if key == "w":
    forward()
elif key == "s":
    backward()
elif key == "a":
    left()
elif key == "d":
    right()
elif key == "x":
    stop()
else:
    print ("Invalid key pressed")



def forward():
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.HIGH)
    GPIO.output("P8_14", GPIO.LOW)
    PWM.set_duty_cycle("P9_14", 100)
    PWM.set_duty_cycle("P9_16", 100)
    PWM.set_duty_cycle("P8_19", 100)
    PWM.set_duty_cycle("P8_13", 100)
    time.sleep(0.1)

def backward():
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_10", GPIO.HIGH)
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.HIGH)
    PWM.set_duty_cycle("P9_14", 100)
    PWM.set_duty_cycle("P9_16", 100)
    PWM.set_duty_cycle("P8_19", 100)
    PWM.set_duty_cycle("P8_13", 100)
    time.sleep(0.1)


def left():
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_10", GPIO.HIGH)
    GPIO.output("P8_12", GPIO.HIGH)
    GPIO.output("P8_14", GPIO.LOW)
    PWM.set_duty_cycle("P9_14", 100)
    PWM.set_duty_cycle("P9_16", 100)
    PWM.set_duty_cycle("P8_19", 100)
    PWM.set_duty_cycle("P8_13", 100)
    time.sleep(0.1)


def right():
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.HIGH)
    PWM.set_duty_cycle("P9_14", 100)
    PWM.set_duty_cycle("P9_16", 100)
    PWM.set_duty_cycle("P8_19", 100)
    PWM.set_duty_cycle("P8_13", 100)
    time.sleep(0.1)


def stop():
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.LOW)
    PWM.set_duty_cycle("P9_14", 0)
    PWM.set_duty_cycle("P9_16", 0)
    PWM.set_duty_cycle("P8_19", 0)
    PWM.set_duty_cycle("P8_13", 0)
    time.sleep(0.1)
    

