# Pi in the Sky

# Planning 

## Goal

Inspired by Cloudy with a Chance of Meatballs, to launch a hamburger into the air and drop it at the apex of its flight. 

## Resources and Constraints

### Resources: 
- Raspberry Pi
- All available Engineering supplies (CAD, wires, sensors, etc) 
- Hamburger would be bought from Cookout or another fast-food restaurant 
- Model rockets, helicopters, drones, weather balloons, etc could be sourced 
- Bob already has a helium release valve from a prior project 

### Constraints: 
- Time- Time is the biggest constraint on the possibilities for this assignment
- Safety- Safety must be taken into consideration, ex. Building something like a hot air balloon may not be possible. 
- Resources- It may be possible to source some resources, depending on which flight type is chosen but some, such as helium, may be harder to obtain.
- Cost- Components for this project could be pricey, and we shpuld work to make sure that everything we use in our design is affordable  
- Weight- Anything that is going to fly (especially a balloon) has weight constraints. If our goal is to drop a hamburger, it may be too heavy. 

## Brainstorming 

### Links: 
- [Wireless Rocket Launcher](https://learn.pi-supply.com/make/how-to-build-a-wireless-rocket-launcher-with-the-raspberry-pi-and-pijuice-hat/) 
- [Raspberry Pi Blimp](https://github.com/The-Alchemist/raspberrypi-blimp) 
- [Micro Drone Blimp](https://www.youtube.com/watch?v=NXb11NqYD-s) 
- [Raspberry Pi Weather Balloon](https://hackaday.com/2016/05/07/raspberry-pi-balloon-goes-too-high-goes-boom-but-survives/ ) 

### Flight Ideas: 

Balloon - 
   - Advantages: Slow ascent, steady, Bob already has a working helium valve part. 
   - Disadvantages: Lack of direction control, fragile. 
   - Could use helium? Only needs to fly once so helium could be gradually released for descent. 
	
Rocket-
   - Advantages: Easy flight, straight up and down 
   - Disadvantages: Very fast, unsteady, difficult to drop something

Drone-
   - Flightpath control, steady, speed control 
   - Disadvantages: Difficult to build, expensive 
 
## Solution 
Building a helium weather balloon that would ascend to a certain altitude, drop the hamburger, and then descend by releasing helium. The balloon would collect data on its height to determine when to drop the hamburger. 

## Design 

### Design Links: 
Anything linked elsewhere in the design description is also linked here ++ extra resources-
- [Website 1 to Buy Weather Balloons](https://www.scientificsales.com/Meteorological-Weather-Sounding-Balloon-s/25.htm)
- [Website 2 to Buy Weather Balloons](https://www.scientificsonline.com/product/professional-weather-balloon-6555)
- [Weight info for Weather Balloons](https://stratostar.com/how-much-weight-can-a-high-altitude-weather-balloon-carry/)
- [Weight info for Cookout Hamburgers](https://cookout.com/wp-content/uploads/2018/05/Nutrition_Website-1.pdf)
- [Height, Pressure, and Temp Sensing with Raspberry Pi](https://www.instructables.com/Personal-Electronics-Altimeter-Using-Raspberry-Pi-/) 
- [Where to Buy Height Sensor](https://www.adafruit.com/product/1893)
- [Ballon Helium Lift Chart](http://balloonmagic.com/charts.php?ChartType=3)
- [Balloon Performance Calculator](https://www.highaltitudescience.com/pages/balloon-performance-calculator)
- [Basic Servo Control Code](https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/)

### Weight:  
- The average weight of a small Cookout hamburger is [82.5 grams](https://cookout.com/wp-content/uploads/2018/05/Nutrition_Website-1.pdf)
- The weight of a Raspberry Pi 0 is about [9 grams](https://www.tomshardware.com/features/raspberry-pi-zero)
- According to this [balloon selling website](https://www.scientificsonline.com/product/professional-weather-balloon-6555) a balloon of size 3 ft in diameter has a lift potential of about 113 g (1/4 lb), a balloon of size 8 ft diameter has a lift potential of about 283 g (10 oz) and a balloon of size 16 ft in diameter has a lift potential of about 1097 g (2.42 lb). 
- If this website is correct, for our purposes it would make sense to select an 8 ft balloon to ensure that the weight limitations are flexible enough to allow us to add any neccessary equipment. 
- On most balloon websites, 8 ft weather balloons sell for about $30. [Website 1](https://www.scientificsales.com/8237-Weather-Balloon-300-Grams-Natural-p/8237.htm); [Website 2](https://www.scientificsonline.com/product/professional-weather-balloon-6555)

### Flight (Descent): 
- Balloon will be filled with helium. Need about 250 cu ft of helium for an 8ft balloon according to according to [this website](http://balloonmagic.com/charts.php?ChartType=3). Other websites state that most rental tanks at party stores should have a capacity of about 250 cu ft, so we can rent a helium tank from Party City, hopefully for less than $50. 
- The height of the balloon will be determined by a height sensor. Height sensors can be [bought online](https://www.adafruit.com/product/1893) for about $10 each. Here is a link to a [website with Raspberry Pi altitude sensor instructions](https://www.instructables.com/Personal-Electronics-Altimeter-Using-Raspberry-Pi-/).
- After the balloon reaches a certain height (determined by height sensor) it will release helium to descend. 
- Bob has a helium valve from a previous project that we will use to accomplish this. 
- This valve will be controlled by a servo, which will start off closed (at a certain angle) and then turn to open the valve and allow helium to escape. 
- I created a very basic code for this servo control (need to upload to github) and here is a website for [servo control with a raspberry pi](https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/) 

### Dropping Mechanism (+ height sensor):  
Once the balloon has reached the correct height, we shall drop the burger. The ???whopper dropper??? (technical term) can either be like a trap door design or a claw of some sort. The trap door design will involve a thin strip of clear plastic that will be wrapped around the burger and fastened with a 3d printed buckle. When the burger reaches the predetermined drop height, a mechanism (probably some form of servo) will unfasten the burger and it will fall to the ground. See the image fold out below for more design details. 
<details>
  <summary> Whopper Dropper Design </summary>

<img src="https://github.com/gwyatt40/Pi-in-the-Sky/blob/main/Images/whopperdropper.png" alt="Whopper Dropper" width="600" height="800">

</details>

### Code 
- This code will have to combine 3 main functions. Height sensing, valve control, and controlling the dropping mechanism. 
- A basic height sensing code can be found [here](https://www.instructables.com/Personal-Electronics-Altimeter-Using-Raspberry-Pi-/)
- A basic valve control (servo control) code can be found at [this link](https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/) 
- Since the dropping mechanism will be controlled by servos, a code similar to the one found at the link above can be used, with angles adjusted
- Here is a very, incredibly basic mock up code, to demonstrate how the three parts of the code will work together: 

<details>
  <summary> Basic Mock up Code ????????? </summary>

```
set up libraries

assign pins

functions set up: 
	drop.burger = servo.angle == X
	valve.release = servo.angle = X
	
while true(): 
	sense height 
	print (height)
	if height == drop height
		drop.burger()
		valve.release()
   
```
</details>

### Materials 
- 8 ft weather balloon
- Raspberry Pi 0
- Helium valve
- Helium tank  
- Height sensor
- Servo(s)
- Height sensor 
- Wires and other components (on/off buttons, LEDs, etc) 
- Battery 
- Small Cookout hamburger
- Plastic sheet for dropping mechanism 
- Plastic CAD components for dropping mechanism

### Shopping List 
- 8 ft weather balloon
- Height sensor
- Hamburger
- Helium 
- 
## Risk Mitigation 
- Flying the balloon in a wide, open field away from other people to minimize the risk of payload falling and injuring someone.
- Skewering the burger together so that it does not fall apart midflight.
- Dropping the burger at a fairly low height, in order to better ensure a safe drop and a safe balloon descent.
- Helium is a fairly inert gas so we will most likely not have to worry about flammability or toxicity, however it is still a chemical and should be handled with caution. Some party supply stores mix their helium with nitrogen, so we will inquire about this before hand, as nitrogen can cause the balloon to burst at a lower altitude. However, this will probably be a non-issue, since our balloon will not be reaching high altitudes. 
- Safety protection measures such as safety goggles and gloves will be used when necessary.
## Schedule 

- Feb 11- Complete planning/project proposal
- Feb 18- Source all components (order/buy/find), finalized design paper/pencil for CAD dropping mechanism, initial mock-up code
- Feb 25- Gather all components (expt. helium if need to rent), initial work on CAD dropping mechanism, complete wiring, initial work on code (valve close/open)
- Mar 4- Continue work on CAD mechanism, continue work on code (height sensor code)
- Mar 11- Continue work on CAD mechanism, continue work on code (combine sensor code and valve code) 
- Mar 18- Continue work on CAD mechanism (first prototype?), continue work on code (sensor code and valve code + dropping mechanism code) 
- Mar 25- Test prototype of dropping mechanism with dropping mechanism code
- Apr 1- Refine dropping mechanism prototype, refine and troubleshoot initial code
- Apr 8- SPRING BREAK  
- Apr 15- Test dropping mechanism version 2 with code, height sensor, and helium valve
- Apr 22- Source helium for balloon, start testing balloon with helium valve (just air initially) 
- Apr 29 - Combine balloon (still air only), helium valve, dropping mechanism, and height sensor
- May 6 - Source hamburger, first test flights (with helium and real burger) 
- May 13- Final flight, complete documentation, PROJECT FINISHED 

# Documentation 	

#### Links
[Servo Valve Code Site](https://core-electronics.com.au/tutorials/control-servo-raspberry-pi.html)

[MPL3115A2 Altimeter with Circuit Python](https://learn.adafruit.com/using-mpl3115a2-with-circuitpython/circuitpython)

[Altimeter Wiring Image](https://github.com/gwyatt40/Pi-in-the-Sky/blob/main/Images/altimeterwiring.png)

## Code
[altimetervalve.py](https://github.com/gwyatt40/Pi-in-the-Sky/blob/main/Code/altimetervalve.py) 
<details>
  <summary> Final Code ????????? </summary>

```
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
```
</details>
	
### Wiring 
Altimeter - SDA to SDA, SCL to SCL, VIN to 3V, GND to GND 
Servo 1 - PIN to 13, VIN to BATTERY, GND to GND (battery)
Servo 2 - PIN to 18, VIN to BATTERY, GND to GND (battery) 
	

## Progress Checks 

### Week 1 (Feb 11)

#### Georgia 
This week I worked on brainstorming and completing the project plan. I created a schedule, materials list, risk mitigation write-up, and basic code layout. I also planned solutions for the issues of both flight and weight related to this project. Goals for next week: Order all necessary parts, fix Pi/github issues with the folder, start very basic servo control code. 

#### Bob 
I helped Georgia with the project plan, letting her bounce ideas off me. 

### Week 2 (Feb 18) 

#### Georgia 
This week I worked on developing a basic servo control code. I was successful in creating a functioning code, but ran into some issues with the actual valve mechanism. The servo was not stromg enough to entirely close the valve. The valve operates by having a servo move a piece of plastic in order to open/close a piece of plastic tubing, however the tubing was to thick for the servo to close it entirely and air still escaped from the test balloon. I attempted to switch out the servo I was using in the valve for a potentially stronger one, but ended up accidentally cracking part of the valve's lasercut plastic cage. This can easily be fixed but, in the future, solutions will need to be found to allow the valve to fully close with a micro servo. 

#### Bob 
I started work on the "Whopper Dropper" Mechanism, coming up with a basic design and starting an onshape prototype.

### Week 3 (Feb 25)

#### Georgia 
I was only able to attend one class this week, due to having Monday off and being sick Tuesday. Because of this I ended up getting behind on my original plan of having ordered and sourced all the necessary parts by this week. I determined that the two parts we need to order at the moment are an altitude sensor, which is about $10 from adafruit, and a weather balloon, which I found can cost upwards of $40. Because of the high cost of weather balloons, I've been working to brainstorm alternatives, for example, using several smaller balloons. I will talk over this with Bob next class. 

#### Bob
I did not make it to class this week, so I did not progress. 

### Week 4 (Mar 4)

#### Georgia
On Monday we brainstormed weather balloon alternatives and came up with a new, cheaper plan for launching our project. Instead of using one, expensive scientific quality weather baloon, we will use several smaller baloons (about 4 24 inch balloons). To allow the project to descend, we will use the same valve mechanism that we had initially planned, except it will only be attached to one of the balloons. When helium is relesased from one balloon, the project will begin to sink. We may have to adjust payload weight and the amount of helium in the balloons to achieve this, but hopefully this method will provide a more steady descent than using one large balloon. 

I was planning to spend the rest of the week working on controlling multiple servos with a button, until I could order an altimeter sensor, but Mr. Miller informed me that we already have altimeters in the lab. Since I didn't have to order an altimeter, I found and set up an altimeter code and wiring from [this website](https://learn.adafruit.com/using-mpl3115a2-with-circuitpython/hardware). The code that I had found online while planning for this project involved a different type of altimeter and I2C shield, so I couldn't use it. I additionally had to download MPL3115A2 libraries and I followed the instructions [linked here](https://pypi.org/project/adafruit-circuitpython-mpl3115a2/). I also had to download board libraries after receiving a 'board module not found' error and I used 'sudo pip3 install adafruit-blinka' to do so. 

#### Bob

I started working on the Whopper dropper mechanism. I made a prototype to be fabricated.

### Week 5 (Mar 11) 

#### Georgia
This week I worked on combining the altimeter code and the servo valve code. The final combination of the two code is [linked here](https://github.com/gwyatt40/Pi-in-the-Sky/blob/main/Code/servovalve.py). Next week, I plan to add a second servo to this set up. After that, the code should be almost complete, with the exception of adjustments for specific servo angles and drop altitudes. Bob also suggested the addition of a failsafe timer, to ensure that the balloon does not float away, I'll encorporate this into the code next week. I will also need to switch the raspberry pi over to a battery pack from a computer. 

### Week 6 (Mar 18) 

#### Georgia
This week I worked on adding a second servo to my setup, but I ran into errors with this because I could not find a second working PWM pin to connect the servo to. Additionally, when I did hook up two servos to my raspberry pi, it would only run code for a few seconds, before it stopped working. If two servos were connected, for some reason, I couldn't use ctrl+C or ctrl+Z to stop running code, so I had to close out of the program entirely. However, with just one servo, the code ran perfectly and I could use ctrl+c or ctrl+z to stop it. I think some of these issues may be due to the pi not having enough power from the computer to power two servos, so next week I will work to set up a battery for my pi, which I need to do anyway in order for the final setup to work detached from the computer.  

### Week 7 (Mar 25) 

#### Georgia 
This week I added a battery to my setup so that I could run two servos from my raspberry pi. I was right that the problems I encountered last week were because my pi did not have enough power to run two servos, so adding the battery fixed this issue. I connected to ground and power wires of the servos to the battery directly. This setup did not work at first, and I couldn't figure out why until Mr. Miller suggested that I should connect the ground of the battery to the ground of the pi as well. I did this and my servos worked immediately, so thanks Mr. Miller! Next week I will work on adjusting specific angles for the servos and detaching the setup from the computer so that it can run independently.


### Weeks 8-12 

Hiatus for Spring Break and Onshape work. No project progress. 

### Week 13 (May 6) 

#### Georgia 
I was not in class for much of this week due to having morning AP exams, so I did not really get to do much work on thie project, besides going over the schedule. 

### Week 14 (May 13) 

#### Georgia 
When I returned to continue working on this project, it took me some time to get reaqcquqintanced with the project, and to set everything up again. Once I did, I realized that the code I had finished in March was no longer functional. I spent the rest of the week troubleshooting this issue, mostly by checking code and wiring over and over.  
 
### Week 15 (May 20)

#### Georgia 
This week I continued to work on troubleshooting the code. I eventually realized that the issue was with the battery being dead, probably because it had been plugged in for so long over break. I used a voltmeter to test several batteries before I found one that worked, and the code immediately started working again. I also found that the new battery allowed the servos to run more smoothly than they had with the old battery before it died.

### Week 16 (May 27) 

#### Georgia 
This week I realized that we most likely were not going to be able to fully complete the project on time, and decided to focus on improving documentation in order to at least have a packaged final product, even if it was not complete. I worked on the read me documentation, commented the code, and made sure that everything ran smoothly and was as complete as it could be. 

## Conclusion 

We did not get to complete this project, largely due to lack of time. If we were to complete the project, the next step would be to simplify the wiring and to upload the code so that the Pi system is portable. After that, we could print out all of the finished CAD designs and begin to assemble everything. One issue that we may encounter here is with the valve design, the current plastic tubing used in the valve is too stiff for the servo to close it off completely, so we may need to redesign the valve or use weaker tubing. After assembly we would adjust the servo angles and drop altitude and could add a test balloon. Once tests with the non-helium test balloon were complete, we could add helium balloons and a drop object and start to test the final project. Overall, it would probably take us 3-4 more weeks to properly finish and document this project. This is especially true since we have yet to print out CAD designs, and these designs may not turn out well once printed. Additionally, I am not entirely sure how to upload code to a raspberry pi so that it can be detached from a coumputer and I would have to look up how to do that. Finally, getting the project to fly would be significantly difficult, especially if we made any miscalculations in planning about how much our payload would weigh, which is likely. Overall, at least on my part (Georgia) I would say that the biggest issue with our execution of this project was our time management. Personaly I underestimated the time it would take me to complete the code, and failed to account for the four week Onshape break in planning. Other than that, however I was proud of our plan as I felt that it was fairly comprehensive and I believe that we could have completed this project to a higher level of execution if we had more time. 
