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

    


while True:

    def readEncoder(self):
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

    x=raw_input()
    if x=='w':
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
        
        
        
        
        