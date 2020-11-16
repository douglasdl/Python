# coding: utf-8
import wiringpi as pi
import time


#morseCode = [["A" ".-"], []
#	N	-.
#B	-...	O	---
#C	-.-.	P	.--.
#D	-..	Q	--.-
#E	.	R	.-.
#F	..-.	S	...
#G	--.	T	-
#H	....	U	..-
#I	..	V	...-
#J	.---	W	.--
#K	-.-	X	-..-
#L	.-..	Y	-.--
#M	--	Z	--..

# RasPi connected GPIO number
pinLED = 4
pinBuzzer = 18

# Pins Setting
pi.wiringPiSetupGpio()
pi.pinMode(pinLED, 1)
pi.pinMode(pinBuzzer, 1)

#pi.digitalWrite(pinLED, 0)
increment = 1
limit = 100
for cnt in range(1, limit + 1):
    pi.digitalWrite(pinLED, 1)
    pi.digitalWrite(pinBuzzer, 1)
    time.sleep(cnt * 0.001)
    pi.digitalWrite(pinLED, 0)
    pi.digitalWrite(pinBuzzer, 0)
    time.sleep(cnt * 0.001)