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
- Balloon will be filled with helium. How much helium and source? 
- After the balloon reaches a certain height (determined by height sensor) it will release helium to descend. 
- Bob has a helium valve from a previous project that we will use to accomplish this. 
- This valve will be controlled by a servo, which will start off closed (at a certain angle) and then turn to open the valve and allow helium to escape. 
- I created a very basic code for this servo control (need to upload to github) and here is a website for [servo control with a raspberry pi](https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/) 

### Dropping Mechanism (+ height sensor):  
