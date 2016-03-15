import time
import pyupm_ttp223 as ttp223
import requests
import json
import pyupm_grove as grove
import pyupm_i2clcd as lcd

url = "http://requestb.in/1mj62581?inspect"
headers = {'content-type': 'application/json'}

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
        valor += 1
        myLcd.setCursor(0, 0)
        myLcd.write(str(valor))
        data = {"Id": "AI", "Espacio": tId, "Estado": "Entro"}
        data = json.dumps(data)
        requests.post(url, params=data, headers=headers)


def enter(button, tID):
    global valor
    if(button.value() != 0):
        valor -= 1
        myLcd.setCursor(0, 0)
        myLcd.write(str(valor))
        data = {"Id": "AI", "Espacio": tID, "Estado": "Salio"}
        data = json.dumps(data)
        requests.post(url, params=data, headers=headers)

while True:
    sendInfo(touch1, 1)
    enter(button, 1)
    time.sleep(0.1)

del touch1
del button
# Delete the buzzer object
# del buzzer
