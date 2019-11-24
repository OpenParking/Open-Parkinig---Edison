# Open Parking -Edison

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

## Adding repositories
type:
```
echo "src intel-iotdk  http://iotdk.intel.com/repos/1.1/intelgalactic"  > /etc/opkg/intel-iotdk.conf
```
open the base-feeds.conf file:
```
vi /etc/opkg/base-feeds.conf
```
and add the following lines:
```
src/gz all http://repo.opkg.net/edison/repo/all
src/gz edison http://repo.opkg.net/edison/repo/edison
src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32
```


## Software Requirements
1. Enable [uvm webcams](https://software.intel.com/en-us/articles/opencv-300-ipp-tbb-enabled-on-yocto-with-intel-edison).
2. Install PIP.
3. Install Git.
4. Compile and install [openalpr](https://github.com/openalpr/openalpr/wiki/Compilation-instructions-%28Ubuntu-Linux%29) and its dependencies.
5. Install [pytesser](https://code.google.com/p/pytesser/downloads/detail?name=pytesser_v0.0.1.zip&can=2&q=).

### Install the packages:
```
opkg install python-numpy opencv python-opencv

```

### Install the python packages (with pip):
1. requests
2. json
3. pil


## Initial setup
1. Connect the Edison whit Grove - Starter Kit Plus
2. Connect the bottom sensor Pin - 8
3. Connect the touch sensor Pin - 4
4. Connect the lcd Pin I2C - 4

### Configure files
1. open configure.txt and add the names of your zones.
2. in object_detect.py change the p1 and p2 values to fit the street of your parking lot.

## Runing the program
```
python source/anpr.py
python source/ParkingV7.py
python object_detect.py cars2.xml 180 1 Z1

```

You need to clone our code from our git:
https://github.com/OpenParking/Open-Parkinig---Edison.git

And access the directory Open-Parking--Edison and source

In our code, you can modify the pin´s that allow you to configure the sensors, for default we put the pin 4 with the touch sensor and the pin 8 with the button sensor.

Finally you have compile the file ParkingV7.py in wich you need to modify the url’s.
In the initial configuration you'll have input the name of the zone that edison will be working on.
