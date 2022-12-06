# Locate Lidar
# beaglebone black
import serial
import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import math

class Lidar:
    def __init__(self, top_stepper, tfluna):
        self.top_stepper = top_stepper
        self.tfluna = tfluna

        self.TOP_STEPPER_CALIBRATION_DISTANCE_CM = 10  # manually determined
        self.TOP_STEPPER_CALIBRATION_OFFSET = 48       # manually determined
        
        
        
    def _get_distance(self):
        # get distance from lidar
        self.tfluna.write('R')
        time.sleep(0.1)
        data = self.tfluna.read(9)
        if data[0] == 'R':
            distance = (ord(data[1]) << 8) + ord(data[2])
            return distance
        else:
            return None

    def _get_angle(self, distance):
        # get angle from lidar
        angle = math.atan2(distance, 10)
        angle = math.degrees(angle)
        return angle
        
        
    def _get_stepper_angle(self, angle):
        # get stepper angle
        stepper_angle = angle + self.TOP_STEPPER_CALIBRATION_OFFSET
        return stepper_angle
    
    def _get_stepper_pulse(self, stepper_angle):
        # get stepper pulse
        stepper_pulse = (stepper_angle / 180.0) + 0.5
        return stepper_pulse
    
    def _get_stepper_pulse_ms(self, stepper_pulse):
        # get stepper pulse in ms
        stepper_pulse_ms = stepper_pulse * 20
        return stepper_pulse_ms
    

    def get_lidar_data(self):
        # get lidar data
        distance = self._get_distance()
        angle = self._get_angle(distance)
        stepper_angle = self._get_stepper_angle(angle)
        stepper_pulse = self._get_stepper_pulse(stepper_angle)
        stepper_pulse_ms = self._get_stepper_pulse_ms(stepper_pulse)
        return distance, angle, stepper_angle, stepper_pulse, stepper_pulse_ms
    
    
    def calibrate(self):
        # calibrate lidar
        print ("Calibrating lidar...")
        distance = self._get_distance()
        while distance > self.TOP_STEPPER_CALIBRATION_DISTANCE_CM:
            self.top_stepper.step(1)
            time.sleep(0.1)
            distance = self._get_distance()
        print ("Lidar calibrated.")
        return distance, angle, stepper_angle, stepper_pulse, stepper_pulse_ms
