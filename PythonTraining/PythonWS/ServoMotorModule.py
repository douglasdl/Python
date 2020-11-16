# coding: utf-8
import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setwarnings(False)
GPIO.cleanup()

class ServoMotor():
    def __init__(self, SIGNAL):
        print("Created new Servo Motor")
        self.SIGNAL = SIGNAL
        
        
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.SIGNAL, GPIO.OUT)

        # Set pwm pin to 50Hz
        self.pwm = GPIO.PWM(self.SIGNAL, 50)

        # Set initial angle to 0
        self.pwm.start(0)       


    def setAngle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(self.SIGNAL, True)
        self.pwm.changeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.SIGNAL, False)
        self.pwm.changeDutyCycle(0)

    def rotate(self, angle):
        print("Rotating")
        GPIO.input(self.SIGNAL, GPIO.HIGH)
        sleep(0.1)   








   



def main():
    #servo1.setAngle(90)
    #servo1.pwm.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    servo1 = ServoMotor(23)
    servo1.setAngle(30)
    main()