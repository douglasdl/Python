# coding: utf-8
import wiringpi as pi
import time

pinLED = 4
pinLED2 = 26

pi.wiringPiSetupGpio()
pi.pinMode(pinLED, 1)
pi.pinMode(pinLED2, 1)

for cnt in range(1, 5 + 1):
    pi.digitalWrite(pinLED, 1)
    time.sleep(0.3)
    pi.digitalWrite(pinLED, 0)
    time.sleep(0.3)
    pi.digitalWrite(pinLED2, 1)
    time.sleep(0.2)
    pi.digitalWrite(pinLED2, 0)
    time.sleep(0.2
    )
