import time
import pyupm_ttp223 as ttp223
import requests
import json
import pyupm_grove as grove
import pyupm_i2clcd as lcd

urlEntrada = "10.43.36.225:3000/enter"
urlSalida = "10.43.36.225:3000/leave"

touch1 = ttp223.TTP223(4)

# Create the button object using GPIO pin 0
button = grove.GroveButton(8)
myLcd = lcd.Jhd1313m1(4, 0x3E, 0x62)
valor = 223
myLcd.setCursor(0, 0)
myLcd.setColor(53, 39, 249)
myLcd.write(str(valor))


def sendInfo(touch, tId):
    global valor
    if touch.isPressed():
        print touch.name()
        valor += 1
        myLcd.setCursor(0, 0)
        myLcd.write(str(valor))
        requests.get(url+tId)


def enter(button, tID):
    global valor
    if(button.value() != 0):
        valor -= 1
        myLcd.setCursor(0, 0)
        myLcd.write(str(valor))
        requests.get(url + tId)

while True:
    sendInfo(touch1,'Z1')
    enter(button,'Z1')
    time.sleep(0.2)

del touch1
del button
# Delete the buzzer object
# del buzzer
