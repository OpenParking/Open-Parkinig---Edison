import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd

# Create the button object using GPIO pin 0
button = grove.GroveButton(8)
myLcd = lcd.Jhd1313m1(4, 0x3E, 0x62)
valor = 223
myLcd.setCursor(0, 0)
myLcd.setColor(53, 39, 249)
myLcd.write(str(valor))

while True:
    if (button.value() != 0):
        valor -= 1
        myLcd.setCursor(0,0)
        myLcd.write(str(valor))
        time.sleep(0.1)

del button
# Delete the buzzer object
# del buzzer
