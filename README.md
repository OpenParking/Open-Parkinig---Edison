#Open Parking -Edison

## Hardware Requirements
Intel Edison Arduino Breakout
Grove - Starter Kit Plus
One microUSB.

To learn the basic of intel Edison enter to:
intel.com/edison/getstarted

For the initial configuration enter to:
https://theiotlearninginitiative.gitbooks.io/

========================

To start developing in your Edison, you need have the initial configuration that is in the link above and you'll also need the following extra requirements.

##Software Requirements
Install PIP
Install Git
###Install the packages
Requests
Json

##Initial setup
Connect the Edison whit Grove - Starter Kit Plus
Connect the bottom sensor Pin - 8 
Connect the touch sensor Pin - 4
Connect the lcd Pin I2C - 4

You need to clone our code from our git: 
https://github.com/OpenParking/Open-Parkinig---Edison.git

And access the directory Open-Parking--Edison and source

In our code, you can modify the pin´s that allow you to configure the sensors, for default we put the pin 4 with the touch sensor and the pin 8 with the button sensor.

Finally you have compile the file ParkingV7.py in wich you need to modify the url’s. 
In the initial configuration you'll have input the name of the zone that edison will be working on.

