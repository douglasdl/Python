# coding: utf-8
import RPi.GPIO as GPIO
from time import sleep, time

# GPIO
GPIO.setmode(GPIO.BCM)

US_TRIG = 24
US_ECHO = 25

#GPIO Setup
GPIO.setup(US_TRIG, GPIO.OUT)
GPIO.setup(US_ECHO, GPIO.IN)

GPIO.output(US_TRIG, True)
sleep(0.0001)
GPIO.output(US_TRIG, False)

while GPIO.input(US_ECHO) == False:
    start = time()
    #print("start: {}".format(start))
while GPIO.input(US_ECHO) == True:
    end = time()
    print("end: {}".format(end))        
sig_time = end - start
#cm
distance = sig_time / 0.000058
print('Distance: {}cm'.format(distance))

GPIO.cleanup()                