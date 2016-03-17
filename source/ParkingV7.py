#File: Parking-Edison-V6

# ----- Seccion Import ---
import time
import pyupm_ttp223 as ttp223
import requests
import json
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import os.path

#Function Detecte Url
#Detected if the url is balid
#This function recive the zone and the url page and return True or False
def inputDetection(zone,url):
    r = requests.get(url + "/" +zone)
    if (r.status_code == 404):
        return False
    else:
        return True

#Funtion checkCapacity
#This function send request.get for obtain,
#the total cars that the zone have in the moment
def checkCapacity(tId,url):
    r = requests.get(url+"/"+tId)
    data = r.json()
    return data["capacity"] - data["full"]

#Function checkMax
#This function to get the capacity of the zone from json
def checkMax(tId,url):
    r = requests.get(url+"/"+tId)
    data = r.json()
    return data["capacity"]

#Function checkZone
#This function to get the zone of name from the json
def checkZone(tId,url):
    r = requests.get(url+"/"+tId)
    data = r.json()
    return data["name"]

#Function cheangeLCD
#Function to change the color of the LCD depending on the spaces available
def changeLCD(value, cap):
    percentage = float(value) / capacity
    if (percentage <= 0.25):
        myLcd.setColor(255,0,0)
    elif(percentage <= 0.50):
        myLcd.setColor(255,165,0)
    elif(percentage<= 0.75):
        myLcd.setColor(255,255,0)
    elif(percentage <= 1):
        myLcd.setColor(0,255,0)
    myLcd.setCursor(1, 0)
    if(value < 10):
        myLcd.write("Available: " +"0"+str(currentCapacity))
    else:
        myLcd.write("Available: " +str(currentCapacity))
    
def exit(touch, tId, url):
    global currentCapacity
    global capacity
    if touch.isPressed():
        if (currentCapacity < capacity):
            currentCapacity += 1
            changeLCD(currentCapacity, capacity)
            r = requests.put(url+"/"+tId)    
                
def enter(button, tId, url):
    global currentCapacity
    global capacity
    if(button.value() != 0):
        if (currentCapacity > 0):
            currentCapacity -= 1
            changeLCD(currentCapacity, capacity)
            r = requests.put(url+"/"+tId)


#URL from the app
urlEntrada = "http://198.199.119.166/enterzone"
urlSalida = "http://198.199.119.166/leavezone"
urlzone = "http://198.199.119.166/zones"

if(os.path.isfile("configure.txt")):
    fo = open("configure.txt")
    zone = fo.read()
    fo.close()
else:
    zone = raw_input("Zone ID: ")
    Correct = inputDetection(zone,urlzone)
    fo = open("configure.txt", "w")
    fo.write(zone)
    fo.close()

zone = raw_input("Zone ID: ")
Correct = inputDetection(zone,urlzone)

#Create the lcd object
myLcd = lcd.Jhd1313m1(4, 0x3E, 0x62)
#Values from the db
currentCapacity = checkCapacity(zone, urlzone)
capacity = checkMax( zone ,urlzone)

#LCD first display
myLcd.setCursor(0, 0)
myLcd.write("zone: " +str(checkZone(zone ,urlzone)))
changeLCD(currentCapacity, capacity)

# Create the touch object using GPIO pin 4    
touch1 = ttp223.TTP223(4)
# Create the button object using GPIO pin 8
button = grove.GroveButton(8)

while Correct:
    exit(touch1, zone , urlSalida)
    enter(button, zone, urlEntrada)
    time.sleep(0.2)

del touch1
del button
