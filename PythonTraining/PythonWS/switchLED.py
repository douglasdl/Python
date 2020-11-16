# coding: utf-8
import wiringpi as pi

# RasPi connected GPIO number
pinLED = 4
pinSW = 17

# Pins Setting
pi.wiringPiSetupGpio()
pi.pinMode(pinLED, 1)
pi.pinMode(pinSW, 0)

#pi.digitalWrite(pinLED, 0)

try:
    while True:
        if(pi.digitalRead(pinSW) == 1):
            pi.digitalWrite(pinLED, 1)
        else:
            pi.digitalWrite(pinLED, 0)
except KeyboardInterrupt:
    pass