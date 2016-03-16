import time
import pyupm_ttp223 as ttp223
import requests
import json
import pyupm_grove as grove
import pyupm_i2clcd as lcd

urlEntrada = "http://secure-badlands-53433.herokuapp.com/enterzone"
urlSalida = "http://secure-badlands-53433.herokuapp.com/leavezone"
urlzone = "http://secure-badlands-53433.herokuapp.com/zones"

def checkCapacity(tId,url):
    global valor
    r = requests.get(url+"/"+tId)
    data = r.json()
    return data["capacity"] - data["full"]

def checkMax(tId,url):
    r = requests.get(url+"/"+tId)
    data = r.json()
    return data["capacity"]

def checkZone(tId,url):
    r = requests.get(url+"/"+tId)
    data = r.json()
    return data["name"]
    
touch1 = ttp223.TTP223(4)

# Create the button object using GPIO pin 0
button = grove.GroveButton(8)
myLcd = lcd.Jhd1313m1(4, 0x3E, 0x62)
valor = checkCapacity("Z2", urlzone)
capacity = checkMax("Z2",urlzone)

myLcd.setCursor(0, 0)
myLcd.write("zone: " +str(checkZone("Z2",urlzone)))
myLcd.setColor(53, 39, 249)
myLcd.setCursor(1, 0)
myLcd.write("Available: " +str(valor))


def exit(touch, tId, url):
    global valor
    global capacity
    if touch.isPressed():
        if (valor < capacity):
            valor += 1
	    if ((valor / capacity) <= 0.25):
		myLcd.setColor(0,255,0)
	    elif((valor / capacity) <= 0.50):
		myLcd.setColor(255,255,0)
	    elif((valor / capacity) <= 0.75):
		myLcd.setColor(255,165,0)
	    elif((valor / capacity) <= 1):
		myLcd.setColor(255,0,0)

            myLcd.setCursor(1, 11)
            myLcd.write(str(valor))
            r = requests.put(url+"/"+tId)    
                

def enter(button, tId, url):
    global valor
    if(button.value() != 0):
        if (valor > 0):
            valor -= 1
            myLcd.setCursor(1,11)
            myLcd.write(str(valor))
            r = requests.put(url+"/"+tId)
        

while True:
    exit(touch1,"Z2", urlSalida)
    enter(button,"Z2", urlEntrada)
    time.sleep(0.2)

del touch1
del button
