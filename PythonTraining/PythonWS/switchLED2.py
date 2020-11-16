# coding: utf-8
import wiringpi as pi
import time

# RasPi connected GPIO number
pinLED = 4
pinLED2 = 26
pinSW = 17

# Pins Setting
pi.wiringPiSetupGpio()
pi.pinMode(pinLED, 1)
pi.pinMode(pinLED2, 1)
pi.pinMode(pinSW, 0)

#pi.digitalWrite(pinLED, 0)

try:
    while True:
        if(pi.digitalRead(pinSW) == 1):
            
            for cnt in range(1, 5 + 1):
                pi.digitalWrite(pinLED, 1)
                time.sleep(0.3)
                pi.digitalWrite(pinLED, 0)
                time.sleep(0.3)
                pi.digitalWrite(pinLED2, 1)
                time.sleep(0.2)
                pi.digitalWrite(pinLED2, 0)
                time.sleep(0.2)
            else:
                pi.digitalWrite(pinLED, 0)
except KeyboardInterrupt:
    pass