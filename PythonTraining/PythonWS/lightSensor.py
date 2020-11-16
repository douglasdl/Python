# coding: utf-8
import wiringpi as pi

# RasPi connected GPIO number
pinLED = 4
pinCdS = 23

# Pins Setting
pi.wiringPiSetupGpio()
pi.pinMode(pinLED, 1)
pi.pinMode(pinCdS, 0)

#pi.digitalWrite(pinLED, 0)

if(pi.digitalRead(pinCdS) == 1):
    pi.digitalWrite(pinLED, 0)
    print("LED OFF")
else:
    pi.digitalWrite(pinLED, 1)
    print("LED ON")