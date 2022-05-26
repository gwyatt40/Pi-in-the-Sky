import time # time libraries

import board # board libraries 

import adafruit_mpl3115a2 # altimeter libraries 

from gpiozero import AngularServo # angular servo libraries 
from time import sleep # sleep function libraries 

i2c = board.I2C() # sets I2c transaction 

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

sensor.sealevel_pressure = 102250 # sets sea level pressure (for Charlottesville, VA) 

servo1=AngularServo(18, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025) # first servo, pin 18, controls valve

servo2=AngularServo(13, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025) # second servo, pin 13, controls drop
                    
while True:

     altitude = sensor.altitude # reads sensor for altitude variable 

     print("Altitude: {0:0.3f} meters".format(altitude)) # converts altitude to meters and prints 


     if altitude > 104: # this value may change depending on the initial reading of the altimeter and the desired drop height 
          servo1.angle =100
          servo2.angle =100
          print("100")
          sleep(2)


     if altitude < 104:
          servo1.angle =160 # servo angles can be adjusted depending on project requirements 
          servo2.angle =160
          print ("160")
          sleep(2)
