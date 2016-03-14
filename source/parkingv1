import time
#Import button and touch sensor
import pyupm_ttp223 as ttp223 #Touch Sensor
import pyupm_grove as grove # Grove button
import requests
import json

#
url = "http://requestb.in/1mj62581?inspect"
#Format for the request
headers = {'content-type': 'application/json'}

#Create a touch sensor object using GPIO pin 4
touch = ttp223.TTP223(4)
#Create a button object using GPIO pin 8
button = grove.GroveButton(8)


#Function to read the input from the touch sensor on the entrance and send the data
def sendInfo(touch, tId, aID):
    if touch.isPressed():
    	print "Send Info"
            data = {"Id": aID, "Espacio": tId, "Disponible": False}
            data = json.dumps(data)
            requests.post(url, params=data, headers=headers)
    return Pressed

#Function to read the input from the button in the exit and send the data
def enter(button, tID, aID):
	if(button.value()!= 0):
		data = {"Id": "AI", "Espacio": tId, "Disponible": True}
		data = json.dumps(data)
		requests.post(url, params=data, headers=headers)
	return Pressed


while True:
    touchPressed = sendInfo(touch, 1)
    buttonPressed = enter(button, 1)
    time.sleep(1)

del touch1
del touch2
