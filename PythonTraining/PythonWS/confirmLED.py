# coding: utf-8
import wiringpi as pi
import time

pinLED = 4

pi.wiringPiSetupGpio()
pi.pinMode(pinLED, 1)

for cnt in range(1, 5 + 1):
    pi.digitalWrite(pinLED, 1)
    time.sleep(0.3)
    pi.digitalWrite(pinLED, 0)
    time.sleep(0.3)
