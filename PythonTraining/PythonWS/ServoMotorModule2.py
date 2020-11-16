# coding: utf-8
import pigpio
from time import sleep


class ServoMotor():
    def __init__(self, SIGNAL):
        print("Created new Servo Motor")
        self.SIGNAL = SIGNAL
        self.FREQ = 50
        self.RANGE = 255
        
        self.pi = pigpio.pi()
        self.pi.set_mode(self.SIGNAL, pigpio.OUTPUT)
        # Set pwm pin to 50Hz
        self.pi.set_PWM_frequency(self.SIGNAL, self.FREQ)
        
        self.pi.set_PWM_range(self.SIGNAL, self.RANGE)     


    def setAngle(self, angle):
        duty = angle / 18 + 2
        self.pi.set_PWM_dutycycle(self.SIGNAL, 2)
        print("Camera: " + str(duty) + " graus!")
        sleep(0.1)
        self.pi.set_mode(self.SIGNAL, pigpio.INPUT)
        self.pi.stop()


def main():
    print("main")
    servo1.setAngle(180)


if __name__ == '__main__':
    servo1 = ServoMotor(23)
    main()