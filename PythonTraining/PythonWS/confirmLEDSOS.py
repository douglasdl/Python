# coding: utf-8
import wiringpi as pi
import time

pinLED = 4
pinLED2 = 26
S = "..."
O = "---"
palavra = [S, O, S]


pi.wiringPiSetupGpio()
pi.pinMode(pinLED, 1)
pi.pinMode(pinLED2, 1)


for letra in palavra:
    print(letra)
    for cod in letra:
        if cod == ".":
            pi.digitalWrite(pinLED, 1)
            time.sleep(0.9)
            pi.digitalWrite(pinLED, 0)
            time.sleep(0.3)
        elif cod == "-":
            pi.digitalWrite(pinLED, 1)
            time.sleep(0.9)
            pi.digitalWrite(pinLED, 0)
            time.sleep(0.3)

