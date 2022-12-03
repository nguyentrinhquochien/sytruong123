import RPi.GPIO as GPIO
from time import sleep






in1 = 23
in2 = 24
in3 = 5
in4 = 6
en1 = 25
en2 = 26
temp1 = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p1 = GPIO.PWM(en1, 75)
p2 = GPIO.PWM(en2, 50)
p1.start(25)
p2.start(25)

#docencoder///////////////////////////////////////////////
class readencoder:
    def __init__(self):
        self.temp1 = 0
        self.temp2 = 0
        self.xung_left = 0
        self.xung_right = 0
        self.goc_encoder = 0
        self.quangduong = 0
        self.w_goc = 0
    def read(self):
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
        self.goc_encoder = (self.xung_left + self.xung_right) * 0.5
        self.quangduong = self.goc_encoder * 0.0005
        self.w_goc = (self.xung_left - self.xung_right) * 0.0005
        return self.goc_encoder, self.quangduong, self.w_goc
    
   



#//////////////////////////////////////////////////////////////////////////

while(1):
    
    
    readencoder()
    print(readencoder.read())
    
    
    x=raw_input()
    
    if x=='w':
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)


    elif x=='a':
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)

    elif x=='d':
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)

    elif x=='s':
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)

    elif x=='l':
        print("low")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
       

    elif x=='m':
        print("medium")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        

    elif x=='h':
        print("high")
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
       
     
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")