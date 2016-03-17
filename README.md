#Open Parking -Edison

## Hardware Requirements
1. Intel Edison Arduino Breakout
2. Grove - Starter Kit Plus
3. One microUSB.

To learn the basic of intel Edison enter to:
https://software.intel.com/es-es/iot/library/edison-getting-started

For the initial configuration enter to:
https://theiotlearninginitiative.gitbooks.io/

========================

To start developing in your Edison, you need have the initial configuration that is in the link above and you'll also need the following extra requirements.

##Software Requirements
1. Install PIP
2. Install Git

###Install the packages:
1. Requests
2. Json

##Initial setup
1. Connect the Edison whit Grove - Starter Kit Plus
2. Connect the bottom sensor Pin - 8 
3. Connect the touch sensor Pin - 4
4. Connect the lcd Pin I2C - 4

You need to clone our code from our git: 
https://github.com/OpenParking/Open-Parkinig---Edison.git

And access the directory Open-Parking--Edison and source

In our code, you can modify the pin´s that allow you to configure the sensors, for default we put the pin 4 with the touch sensor and the pin 8 with the button sensor.

Finally you have compile the file ParkingV7.py in wich you need to modify the url’s. 
In the initial configuration you'll have input the name of the zone that edison will be working on.

