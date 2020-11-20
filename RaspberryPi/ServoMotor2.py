# Reference https://www.learnrobotics.org/blog/raspberry-pi-servo-motor/
import RPi.GPIO as GPIO
from time import sleep

servoPIN = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

pwm=GPIO.PWM(servoPIN, 50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(servoPIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    pwm.ChangeDutyCycle(duty)

pwm.ChangeDutyCycle(5) # left -90 deg position
sleep(1)
pwm.ChangeDutyCycle(7.5) # neutral position
sleep(1)
pwm.ChangeDutyCycle(10) # right +90 deg position
sleep(1)


setAngle(45)
sleep(1)

pwm.stop()
GPIO.cleanup()
