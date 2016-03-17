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

touch1 = ttp223.TTP223(4)

# Create the button object using GPIO pin 0
button = grove.GroveButton(8)
myLcd = lcd.Jhd1313m1(4, 0x3E, 0x62)
valor = checkCapacity("Z1", urlzone)
myLcd.setCursor(0, 0)
myLcd.setColor(53, 39, 249)
myLcd.write(str(valor))

def exit(touch, tId, url):
    global valor
    if touch.isPressed():
        valor += 1
        myLcd.setCursor(0, 0)
        myLcd.write(str(valor))
        r = requests.put(url+"/"+tId)

def enter(button, tId, url):
    global valor
    if(button.value() != 0):
        valor -= 1
        myLcd.setCursor(0, 0)
        myLcd.write(str(valor))
        r = requests.put(url+"/"+tId)

while True:
    exit(touch1,"Z1", urlSalida)
    enter(button,"Z1", urlEntrada)
    time.sleep(0.2)

del touch1
del button
# Delete the buzzer object
# del buzzer
