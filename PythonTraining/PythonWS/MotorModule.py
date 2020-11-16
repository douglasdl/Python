#pip3 install RPi.GPIO
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, EnableA, Input1A, Input2A, EnableB, Input1B, Input2B):
        self.EnableA = EnableA
        self.Input1A = Input1A
        self.Input2A = Input2A
        self.EnableB = EnableB
        self.Input1B = Input1B
        self.Input2B = Input2B
        
        GPIO.setup(self.EnableA, GPIO.OUT)
        GPIO.setup(self.Input1A, GPIO.OUT)
        GPIO.setup(self.Input2A, GPIO.OUT)
        GPIO.setup(self.EnableB, GPIO.OUT)
        GPIO.setup(self.Input1B, GPIO.OUT)
        GPIO.setup(self.Input2B, GPIO.OUT)
        
        self.pwmA = GPIO.PWM(self.EnableA, 100)
        self.pwmA.start(0)
        self.pwmB = GPIO.PWM(self.EnableB, 100)
        self.pwmB.start(0)


    def moveForward(self, speed = 0.5, turn = 0, time = 0):
        speed *= 100
        turn *= 100
        leftSpeed = speed - turn
        rightSpeed = speed + turn
        if leftSpeed > 100:
            leftSpeed = 100
        elif leftSpeed < -100:
            leftSpeed = -100
        if rightSpeed > 100:
            rightSpeed = 100
        elif rightSpeed < -100:
            rightSpeed = -100

        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))
        
        if leftSpeed > 0:
            GPIO.output(self.Input1A, GPIO.HIGH)
            GPIO.output(self.Input2A, GPIO.LOW)
        else:
            GPIO.output(self.Input1A, GPIO.LOW)
            GPIO.output(self.Input2A, GPIO.HIGH)
        
        if rightSpeed > 0:
            GPIO.output(self.Input1B, GPIO.HIGH)
            GPIO.output(self.Input2B, GPIO.LOW)
        else:
            GPIO.output(self.Input1B, GPIO.LOW)
            GPIO.output(self.Input2B, GPIO.HIGH)    
        
        sleep(time)


    def stop(self, time = 0):   
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)

    def moveReverse(self, speed = -0.5, turn = 0, time = 0):
        speed *= 100
        turn *= 100
        leftSpeed = speed - turn
        rightSpeed = speed + turn
        if leftSpeed > 100:
            leftSpeed = 100
        elif leftSpeed < -100:
            leftSpeed = -100
        if rightSpeed > 100:
            rightSpeed = 100
        elif rightSpeed < -100:
            rightSpeed = -100

        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))
        
        if leftSpeed > 0:
            GPIO.output(self.Input1A, GPIO.HIGH)
            GPIO.output(self.Input2A, GPIO.LOW)
        else:
            GPIO.output(self.Input1A, GPIO.LOW)
            GPIO.output(self.Input2A, GPIO.HIGH)
        
        if rightSpeed > 0:
            GPIO.output(self.Input1B, GPIO.HIGH)
            GPIO.output(self.Input2B, GPIO.LOW)
        else:
            GPIO.output(self.Input1B, GPIO.HIGH)
            GPIO.output(self.Input2B, GPIO.LOW)    
        
        sleep(time)
 

    def move(speed, turn, time):
        pass

    

# 4 17 22 27
def main():
    motor1.moveForward(0.5, 0.0, 1)
    sleep(0.1)
    motor1.moveForward(0.6, 0.0, 2)
    sleep(0.1)
    motor1.moveForward(0.8, 0.0, 2)
    sleep(0.1)
    motor1.moveForward(1, -1, 1)
    sleep(0.1)
    motor1.moveForward(0.5, 0.0, 2)
    sleep(0.1)
    motor1.stop(20)


if __name__ == '__main__':
    #motor1 = Motor(13, 4, 17, 19, 22, 27)
    motor1 = Motor(4, 4, 17, 22, 22, 27)
    main()