#Setup the distance given to the robot
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
quangduong = 0


while True: 
  

# Control the robot to turn direction
  print ("nhap huong quay: ")
  huongquay = input()
  if huongquay == w:
      GPIO.output(8, GPIO.HIGH)
      GPIO.output(10, GPIO.LOW)
      GPIO.output(12, GPIO.HIGH)
      GPIO.output(14, GPIO.LOW)
      PWM.set_duty_cycle("P9_14", 100)
      PWM.set_duty_cycle("P9_16", 100)
      PWM.set_duty_cycle("P8_19", 100)
      PWM.set_duty_cycle("P8_13", 100)
      time.sleep(0.5)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(10, GPIO.LOW)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(14, GPIO.LOW)
      PWM.set_duty_cycle("P9_14", 0)
      PWM.set_duty_cycle("P9_16", 0)
      PWM.set_duty_cycle("P8_19", 0)
      PWM.set_duty_cycle("P8_13", 0)
      
  if huongquay == s:
      GPIO.output(8, GPIO.LOW)
      GPIO.output(10, GPIO.HIGH)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(14, GPIO.HIGH)
      PWM.set_duty_cycle("P9_14", 100)
      PWM.set_duty_cycle("P9_16", 100)
      PWM.set_duty_cycle("P8_19", 100)
      PWM.set_duty_cycle("P8_13", 100)
      time.sleep(0.5)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(10, GPIO.LOW)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(14, GPIO.LOW)
      PWM.set_duty_cycle("P9_14", 0)
      PWM.set_duty_cycle("P9_16", 0)
      PWM.set_duty_cycle("P8_19", 0)
      PWM.set_duty_cycle("P8_13", 0)
      
  if huongquay == a:
      GPIO.output(8, GPIO.LOW)
      GPIO.output(10, GPIO.HIGH)
      GPIO.output(12, GPIO.HIGH)
      GPIO.output(14, GPIO.LOW)
      PWM.set_duty_cycle("P9_14", 100)
      PWM.set_duty_cycle("P9_16", 100)
      PWM.set_duty_cycle("P8_19", 100)
      PWM.set_duty_cycle("P8_13", 100)
      time.sleep(0.5)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(10, GPIO.LOW)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(14, GPIO.LOW)
      PWM.set_duty_cycle ("P9_14", 0)
      PWM.set_duty_cycle("P9_16", 0)
      PWM.set_duty_cycle("P8_19", 0)
      PWM.set_duty_cycle("P8_13", 0)
      
      
  if huongquay == d:  
      GPIO.output(8, GPIO.HIGH)
      GPIO.output(10, GPIO.LOW)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(14, GPIO.HIGH)
      PWM.set_duty_cycle("P9_14", 100)
      PWM.set_duty_cycle("P9_16", 100)
      PWM.set_duty_cycle("P8_19", 100)
      PWM.set_duty_cycle("P8_13", 100)
      time.sleep(0.5)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(10, GPIO.LOW)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(14, GPIO.LOW)
      PWM.set_duty_cycle("P9_14", 0)
      PWM.set_duty_cycle("P9_16", 0)
      PWM.set_duty_cycle("P8_19", 0)
      PWM.set_duty_cycle("P8_13", 0)
      
  if huongquay == q:
      GPIO.output(8, GPIO.LOW)
      GPIO.output(10, GPIO.LOW)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(14, GPIO.LOW)
      PWM.set_duty_cycle("P9_14", 0)
      PWM.set_duty_cycle("P9_16", 0)
      PWM.set_duty_cycle("P8_19", 0)
      PWM.set_duty_cycle("P8_13", 0)
      
      break
    
    
  

   
    