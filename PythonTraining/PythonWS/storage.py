# coding: utf-8
import wiringpi as pi
import datetime
import os
import smtplib
from email.mime.text import MIMEText

# Check Inventory
def checkInventory():
    

# RasPi connected GPIO number
pinLED = 4
pinLED2 = 26
pinCdS = 17
pinCdS2 = 16

slot1 = "False"
slot2 = "False"



# Pins Setting
pi.wiringPiSetupGpio()
pi.pinMode(pinLED, 1)
pi.pinMode(pinLED2, 1)
pi.pinMode(pinCdS, 0)
pi.pinMode(pinCdS2, 0)

#pi.digitalWrite(pinLED, 0)
while True:
    if(pi.digitalRead(pinCdS) == 1):
        pi.digitalWrite(pinLED, 0)
        print("LED1 OFF")
        slot1 = "False"
    else:
        pi.digitalWrite(pinLED, 1)
        print("LED1 ON")
        slot1 = "True"

    if(pi.digitalRead(pinCdS2) == 1):
        pi.digitalWrite(pinLED2, 0)
        print("LED2 OFF")
        slot2 = "False"
    else:
        pi.digitalWrite(pinLED2, 1)
        print("LED2 ON")
        slot2 = "True"    

    writeReport(slot1, slot2)


def writeReport(slot1, slot2):
    dir_path = '/home/pi/Desktop'
    filename = 'test'

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    f = open(dir_path + '/' + filename + '.csv', 'a')
    f.write("'" + str(1) + ", " + slot1 + ", " + slot2 + "\n")
    f.close()