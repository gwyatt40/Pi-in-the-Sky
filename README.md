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
- [Website to Buy Weather Balloons](https://www.scientificsales.com/Meteorological-Weather-Sounding-Balloon-s/25.htm)
- [Weight info for Weather Balloons](https://stratostar.com/how-much-weight-can-a-high-altitude-weather-balloon-carry/)
- [Height, Pressure, and Temp Sensing with Raspberry Pi](https://www.instructables.com/Personal-Electronics-Altimeter-Using-Raspberry-Pi-/) 
- [Balloon Performance Calculator](https://www.highaltitudescience.com/pages/balloon-performance-calculator)

### Weight:  
- The average weight of a small Cookout hamburger is [82.5 grams](https://cookout.com/wp-content/uploads/2018/05/Nutrition_Website-1.pdf)
- The weight of a Raspberry Pi 0 is about [9 grams](https://www.tomshardware.com/features/raspberry-pi-zero)
- According to this [balloon selling website](https://www.scientificsonline.com/product/professional-weather-balloon-6555) a balloon of size 3 ft in diameter has a lift potential of about 113 g (1/4 lb), a balloon of size 8 ft diameter has a lift potential of about 283 g (10 oz) and a balloon of size 16 ft in diameter has a lift potential of about 1097 g (2.42 lb). 
- If this website is correct, for our purposes it would make sense to select an 8 ft balloon to ensure that the weight limitations are flexible enough to allow us to add any neccessary equipment. 
- On most balloon websites, 8 ft weather balloons sell for about $30. [Website 1](https://www.scientificsales.com/8237-Weather-Balloon-300-Grams-Natural-p/8237.htm); [Website 2](https://www.scientificsonline.com/product/professional-weather-balloon-6555)

### Flight (Descent): 
- Balloon will be filled with helium. Need about 250 cu ft of helium for an 8ft balloon according to according to [this website](http://balloonmagic.com/charts.php?ChartType=3). Other websites state that most rental tanks at party stores should have a capacity of about 250 cu ft, so we can rent a helium tank from Party City, hopefully for less than $50. 
- The height of the balloon will be determined by a height sensor. Height sensors can be [bought online](https://www.adafruit.com/product/1893) for about $10 each. Here is a link to a [website with Raspberry Pi altitude sensor instructions](hhttps://www.instructables.com/Personal-Electronics-Altimeter-Using-Raspberry-Pi-/).
- After the balloon reaches a certain height (determined by height sensor) it will release helium to descend. 
- Bob has a helium valve from a previous project that we will use to accomplish this. 
- This valve will be controlled by a servo, which will start off closed (at a certain angle) and then turn to open the valve and allow helium to escape. 
- I created a very basic code for this servo control (need to upload to github) and here is a website for [servo control with a raspberry pi](https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/) 

### Dropping Mechanism (+ height sensor):  

### Materials 
- 8 ft weather balloon
- Raspberry Pi 0
- Helium valve
- Helium tank  
- Height sensor
- Servo(s
- Height sensor 
- Wires and other components (buttons, LEDs, etc) 
- Battery 
- Plastic CAD components for dropping mechanism

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
- Mar 18- COntinue work on CAD mechanism (first prototype?), continue work on code (sensor code and valve code + dropping mechanism code) 
- Mar 25- Test prototype of dropping mechanism with dropping mechanism code
- Apr 1- Refine dropping mechanism prototype, refine and troubleshoot initial code
- Apr 8- Test dropping mechanism version 2 with code, height sensor, and helium valve
- Apr 15- Source helium for balloon, start testing balloon with helium valve (just air initially) 
- Apr 22- SPRING BREAK ? 
- Apr 29 - Combine balloon (still air only), helium valve, dropping mechanism, and height sensor
- May 6 - First test flights (with helium and real burger) 
- May 13- Final flight, complete documentation, PROJECT FINISHED 

