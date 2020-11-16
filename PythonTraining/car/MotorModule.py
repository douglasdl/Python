#pip3 install RPi.GPIO
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, Ena, In1, In2):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
        self.pwmA = GPIO.PWM(self.Ena, 100)
        self.pwmA.start(0)


    def moveF(self, speed = 50, t = 0):
        self.pwmA.ChangeDutyCycle(speed)
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(selfIn2, GPIO.HIGH)
        sleep(t)

   
    def Motor(a, b, c, d, e, f):
        pass

    def move(speed, turn, time):
        pass

    def stop(time):
        pass


#############

pwmA.ChangeDutyCycle(60)
GPIO.output(In1, GPIO.LOW)
GPIO.output(In2, GPIO.HIGH)
sleep(2)
pwmA.ChangeDutyCycle(0)

