import time
import pyupm_ttp223 as ttp223
import requests
import json
import pyupm_grove as grove
import pyupm_i2clcd as lcd



#URL from the app
urlEntrada = "http://secure-badlands-53433.herokuapp.com/enterzone"
urlSalida = "http://secure-badlands-53433.herokuapp.com/leavezone"
urlzone = "http://secure-badlands-53433.herokuapp.com/zones"

def inputDetection(zone,url):
	r = requests.get(url + "/" +zone)
	if (r.status_code == 404):
		return False
	else:
		return True

#Funtion to get the available spaces on the zone
def checkCapacity(tId,url):
    r = requests.get(url+"/"+tId)
    data = r.json()
    return data["capacity"] - data["full"]

#Function to get the capacity of the zone from json
def checkMax(tId,url):
    r = requests.get(url+"/"+tId)
    data = r.json()
    return data["capacity"]

#Function to get the zone of name from the json
def checkZone(tId,url):
    r = requests.get(url+"/"+tId)
    data = r.json()
    return data["name"]
    
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
		

	
# Create the touch object using GPIO pin 4    
touch1 = ttp223.TTP223(4)
# Create the button object using GPIO pin 8
button = grove.GroveButton(8)
#Create the lcd object
myLcd = lcd.Jhd1313m1(4, 0x3E, 0x62)
#Values from the db
currentCapacity = checkCapacity("Z2", urlzone)
capacity = checkMax(zone,urlzone)

#LCD first display
myLcd.setCursor(0, 0)
myLcd.write("zone: " +str(checkZone("Z2",urlzone)))
changeLCD(currentCapacity, capacity)

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


while Correct:
    exit(touch1, "Z2", urlSalida)
    enter(button, "Z2", urlEntrada)
    time.sleep(0.2)

del touch1
del button
