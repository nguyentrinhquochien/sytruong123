# Closed-loop motor encoder and IMU by Diego C
# distance
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

# Read IMU
import smbus

# Power management registers
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
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
    
    
def dist(a,b):
    return math.sqrt((a*a)+(b*b))


def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)


def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards

address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)



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
        self.goc_encoder = (self.xung_left - self.xung_right) * 0.0005
        self.quangduong = (self.xung_left + self.xung_right) * 0.0005
        self.w_goc = self.goc_encoder / 0.05
        return self.goc_encoder, self.quangduong, self.w_goc

    def readimu():
        global goc_x
        global goc_y
        global goc_z
        global goc_x_1
        global goc_y_1
        global goc_z_1
        global goc_x_2
        global goc_y_2
        global goc_z_2
        global goc_x_3
        global goc_y_3
        global goc_z_3
        global goc_x_4
        global goc_y_4
        global goc_z_4
        global goc_x_5
        global goc_y_5
        global goc_z_5
        global goc_x_6
        
        
    def __init__(self):
        self.goc_x = 0
        self.goc_y = 0
        self.goc_z = 0
        self.goc_x_1 = 0
        self.goc_y_1 = 0
        self.goc_z_1 = 0
        self.goc_x_2 = 0
        self.goc_y_2 = 0
        self.goc_z_2 = 0
        self.goc_x_3 = 0
        self.goc_y_3 = 0
        self.goc_z_3 = 0
        self.goc_x_4 = 0
        self.goc_y_4 = 0
        self.goc_z_4 = 0
        self.goc_x_5 = 0
        self.goc_y_5 = 0
        self.goc_z_5 = 0
        self.goc_x_6 = 0
        
        bus.write_byte_data(address, power_mgmt_1, 0)
        self.goc_x = read_word_2c(0x3b)
        self.goc_y = read_word_2c(0x3d)
        self.goc_z = read_word_2c(0x3f)
        self.goc_x_1 = read_word_2c(0x43)
        self.goc_y_1 = read_word_2c(0x45)
        self.goc_z_1 = read_word_2c(0x47)
        self.goc_x_2 = read_word_2c(0x4b)
        self.goc_y_2 = read_word_2c(0x4d)
        self.goc_z_2 = read_word_2c(0x4f)
        self.goc_x_3 = read_word_2c(0x53)
        self.goc_y_3 = read_word_2c(0x55)
        self.goc_z_3 = read_word_2c(0x57)
        self.goc_x_4 = read_word_2c(0x5b)
        self.goc_y_4 = read_word_2c(0x5d)
        self.goc_z_4 = read_word_2c(0x5f)
        self.goc_x_5 = read_word_2c(0x63)
        self.goc_y_5 = read_word_2c(0x65)
        self.goc_z_5 = read_word_2c(0x67)
        self.goc_x_6 = read_word_2c(0x6b)   
        return self.goc_x, self.goc_y, self.goc_z, self.goc_x_1, self.goc_y_1, self.goc_z_1, self.goc_x_2, self.goc_y_2, self.goc_z_2, self.goc_x_3, self.goc_y_3, self.goc_z_3, self.goc_x_4, self.goc_y_4, self.goc_z_4, self.goc_x_5, self.goc_y_5, self.goc_z_5, self.goc_x_6
    
    def readgps():
        global lat
        global long
        global alt
        global speed
        global time
        global date
        global fix
        global sat
        
        
    def __init__(self):
        self.lat = 0
        self.long = 0
        self.alt = 0
        self.speed = 0
        self.time = 0
        self.date = 0
        self.fix = 0
        self.sat = 0
        
        ser = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout = 0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata = ser.readline()
        if newdata[0:6] == '$GPGGA':
            newmsg = pynmea2.parse(newdata)
            self.lat = newmsg.latitude
            self.long = newmsg.longitude
            self.alt = newmsg.altitude
            self.speed = newmsg.spd_over_grnd
            self.time = newmsg.timestamp
            self.date = newmsg.datestamp
            self.fix = newmsg.gps_qual
            self.sat = newmsg.num_sats
        return self.lat, self.long, self.alt, self.speed, self.time, self.date, self.fix, self.sat
    
    
    def readtemp():
        global temp
        global hum
        
        
    def __init__(self):
        self.temp = 0
        self.hum = 0
        
        self.temp, self.hum = Adafruit_DHT.read_retry(11, 4)
        return self.temp, self.hum
    
    
    def readlight():
        global light
        
        
        
    def __init__(self):
        self.light = 0
        
        self.light = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
        
        
        return self.light

            
    def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
            return -1
        GPIO.output(cspin, True)
    
        GPIO.output(clockpin, False)
        
        GPIO.output(cspin, False)
        
        
        
        commandout = adcnum
        commandout |= 0x18
        commandout <<= 3
        for i in range(5):
            if (commandout & 0x80):
                GPIO.output(mosipin, True)
            else:
                GPIO.output(mosipin, False)
            commandout <<= 1
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)
            
            
        adcout = 0
        for i in range(13):
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)
            adcout <<= 1
            if (GPIO.input(misopin)):
                adcout |= 0x1
        GPIO.output(cspin, True)
        adcout >>= 1
        return adcout
     
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
        


