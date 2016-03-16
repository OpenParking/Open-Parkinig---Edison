import time
import pyupm_ttp223 as ttp223
import requests
import json
import pyupm_grove as grove
import pyupm_i2clcd as lcd

urlEntrada = "http://secure-badlands-53433.herokuapp.com/enterzone/Z2"
urlSalida = "http://secure-badlands-53433.herokuapp.com/leavezone/Z2"
urlzone = "http://secure-badlands-53433.herokuapp.com/zones/Z2"

def checkCapacity():
    global valor
    r = requests.get(urlzone)
    data = r.json()
    return data["capacity"] - data["full"]

touch1 = ttp223.TTP223(4)

# Create the button object using GPIO pin 0
button = grove.GroveButton(8)
myLcd = lcd.Jhd1313m1(4, 0x3E, 0x62)
valor = checkCapacity()
myLcd.setCursor(0, 0)
myLcd.setColor(53, 39, 249)
myLcd.write(str(valor))

def sendInfo(touch, tId):
    global valor
    if touch.isPressed():
        valor += 1
        myLcd.setCursor(0, 0)
        myLcd.write(str(valor))
        r = requests.put(urlSalida)

def enter(button, tID):
    global valor
    if(button.value() != 0):
        valor -= 1
        myLcd.setCursor(0, 0)
        myLcd.write(str(valor))
        r = requests.put(urlEntrada)

while True:
    sendInfo(touch1,2)
    enter(button,2)
    time.sleep(0.2)

del touch1
del button
# Delete the buzzer object
# del buzzer
