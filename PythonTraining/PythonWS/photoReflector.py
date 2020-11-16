# coding: utf-8
import wiringpi as pi
import time

pinPhoto = 21
pinLED = 26

pi.wiringPiSetupGpio()
pi.pinMode(pinPhoto, 0)
pi.pinMode(pinLED, 1)
pi.pullUpDnControl(pinPhoto, pi.GPIO.PUD_OFF)

for cnt in range(1, 10 + 1):
    if pi.digitalRead(pinPhoto) == 1:
        print("chech")
        pi.digitalWrite(pinLED, 0)
    else:
        print("Ignore")
        pi.digitalWrite(pinLED, 1)
    time.sleep(1)

pi.digitalWrite(pinLED, 0)

