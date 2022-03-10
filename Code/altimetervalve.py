import time

import board

import adafruit_mpl3115a2

from gpiozero import AngularServo
from time import sleep

i2c = board.I2C()

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

sensor.sealevel_pressure = 102250

servo =AngularServo(18, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)

while True:
                    
     altitude = sensor.altitude
     print("Altitude: {0:0.3f} meters".format(altitude))

     if altitude > 111:
          servo.angle = 0
          print("0")
          sleep(2)

     else:
          servo.angle = 260
          print ("260")
          sleep(2)
