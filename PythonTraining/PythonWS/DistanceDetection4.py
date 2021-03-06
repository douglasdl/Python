# coding: utf-8
import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setwarnings(False)
GPIO.cleanup()

class USSensor():
    def __init__(self, TRIG, ECHO, LED, BUZZER):
        print("Created new sensor")
        self.TRIG = TRIG
        self.ECHO = ECHO
        self.LED = LED
        self.BUZZER = BUZZER

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.setup(self.LED, GPIO.OUT)
        GPIO.setup(self.BUZZER, GPIO.OUT)
        
        
    def pre_colision(self, cm):
        print("Pre Colision")
        GPIO.output(self.LED, GPIO.HIGH)
        GPIO.output(self.BUZZER, GPIO.HIGH)
        sleep(0.1 * cm)
        GPIO.output(self.LED, GPIO.LOW)
        GPIO.output(self.BUZZER, GPIO.LOW)
        sleep(0.1 * cm)
   
   
    def get_distance(self):
        print("Get Distance")
        GPIO.output(self.TRIG, True)
        sleep(0.0001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO) == False:
            start = time()
            print("start: {}".format(start))
        while GPIO.input(self.ECHO) == True:
            end = time()
            print("end: {}".format(end))        
        sig_time = end - start
        #cm
        distance = sig_time / 0.000058
        print('Distance: {}cm'.format(distance))
        return distance


def main():
    while True:
        distance = sensor1.get_distance()
        sleep(0.05)

    if 10 >= distance > 3:
        sensor1.pre_colision(distance)
    elif distance <= 3:
        sensor1.pre_colision(3)

if __name__ == '__main__':
    sensor1 = USSensor(24, 25, 20, 21)
    main()