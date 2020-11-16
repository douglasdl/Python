# coding: utf-8
import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setwarnings(False)
GPIO.cleanup()

# GPIO
GPIO.setmode(GPIO.BCM)

US_TRIG = 24
US_ECHO = 25
GREEN_LED = 20
YELLOW_LED = 21
RED_LED = 21


#GPIO Setup
GPIO.setup(US_TRIG, GPIO.OUT)
GPIO.setup(US_ECHO, GPIO.IN)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def pre_colision(cm):
    GPIO.output(GREEN_LED, GPIO.HIGH)
    GPIO.output(YELLOW_LED, GPIO.HIGH)
    sleep(0.1 * cm)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    sleep(0.1 * cm)
    
    #GPIO.output(RED_LED, GPIO.LOW)

def get_distance():
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
    return distance

while True:
    distance = get_distance()
    sleep(0.05)

    if 10 >= distance > 3:
        pre_colision(distance)
    elif distance <= 3:
        pre_colision(3)

    #if 10 > distance >= 9:
    #    pre_colision(9)
    #elif 9 > distance > 3:
    #    pre_colision(6)
    #elif distance <= 3:
    #    pre_colision(3)

