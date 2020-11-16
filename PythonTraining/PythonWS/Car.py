# coding: utf-8
import wiringpi as pi
import random
from time import sleep, time
from USSensorModule import USSensor


class Car:
    def __init__(self):
        self.driveMode = "Manual Drive"
        self.speed = 0
        self.acceleration = 0
        self.direction = "Stop"
        self.headLightStatus = 0
        self.alarmStatus = True
        self.isCheckingDistance = False
        

        # GPIO
        self.motor1A = 4
        self.motor2A = 17
        self.motor1B = 27
        self.motor2B = 22

        self.US_TRIG = 24
        self.US_ECHO1 = 25
        self.US_ECHO2 = 5
        self.US_ECHO3 = 26
        
        self.head_light_R = 20
        self.head_light_L = 6
        
        self.tail_light_R = 2
        self.tail_light_L = 3

        self.alarmOff = 16
        
        self.horn = 21
        
        self.servo1 = 23
        
        #PWM
        self.servo2 = 12
        self.servo3 = 18
        self.pwm1_13 = 13  
        self.pwm1_19 = 19

        # US Sensors
        self.USSensor1 = USSensor(self.US_TRIG, self.US_ECHO1, self.horn, self.head_light_R)
        self.USSensor2 = USSensor(self.US_TRIG, self.US_ECHO2, self.horn, self.head_light_L)
        self.USSensor3 = USSensor(self.US_TRIG, self.US_ECHO3, self.horn, self.tail_light_R)
        
        #GPIO Setup
        pi.wiringPiSetupGpio()
        pi.pinMode(self.head_light_R, 1)
        pi.pinMode(self.head_light_L, 1)
        pi.pinMode(self.tail_light_R, 1)
        pi.pinMode(self.tail_light_L, 1)
        pi.pinMode(self.horn, 1)
        pi.pinMode(self.US_ECHO1, 0)
        pi.pinMode(self.US_TRIG, 1)
        

    def ignitionON(self):
        self.alarmStatus = 0

    def detectColision1(self):
        print("Detect colision!\n")
        self.USSensor1.TRIG = True
        sleep(0.0001)
        self.USSensor1.ECHO = False

        while self.USSensor1.ECHO == False:
            start = time()
            #print("start: {}".format(start))
        while self.USSensor1.ECHO == True:
            end = time()
            print("end: {}".format(end))        
        sig_time = end - start
        #cm
        distance = sig_time / 0.000058
        print('Distance 1: {}cm'.format(distance))

        self.USSensor1.TRIG = True
        sleep(0.0001)
        self.USSensor1.ECHO = False  
        return distance 

    def detectColision(self):
        print("Detect colision!\n")
        self.US_TRIG = True
        sleep(0.0001)
        self.US_ECHO1 = False

        while self.US_ECHO1 == False:
            start = time()
            #print("start: {}".format(start))
        while self.US_ECHO1 == True:
            end = time()
            print("end: {}".format(end))        
        sig_time = end - start
        #cm
        distance = sig_time / 0.000058
        print('Distance: {}cm'.format(distance))

        self.US_TRIG = True
        sleep(0.0001)
        self.US_ECHO1 = False  
        return distance  

    def drive1(self, direction):
        self.direction = direction
        print("Driving " + self.direction)

    def setDriveMode(self, driveMode):
        self.driveMode = driveMode
        print("DRIVE MODE: " + self.driveMode)    

    def accelerate(self,speed):
        print("Accelerating")    

    def turnHeadLights(self, status):
        self.headLightStatus = status
        pi.digitalWrite(self.head_light_R, self.headLightStatus)
        pi.digitalWrite(self.head_light_L, self.headLightStatus)
        pi.digitalWrite(self.tail_light_R, self.headLightStatus)
        pi.digitalWrite(self.tail_light_L, self.headLightStatus)                
        
    def honkTheHorn(self):
        pi.digitalWrite(self.horn, 1)
        sleep(0.1)
        pi.digitalWrite(self.horn, 0)
        sleep(0.1)
        pi.digitalWrite(self.horn, 1)
        sleep(0.1)
        pi.digitalWrite(self.horn, 0) 
        #print("BEEP BEEP!!!")

    def runAlarm(self):
        self.alarmStatus = True
        for beeps in range(3):
            if self.alarmStatus == True :
                self.honkTheHorn()
                self.turnHeadLights(1)
                sleep(0.1)
                self.turnHeadLights(0)
                sleep(0.1)





    def drive(self, direction):
        tireA1 = 17
        tireA2 = 4
        tireB1 = 22
        tireB2 = 27

        pi.wiringPiSetupGpio()
        pi.pinMode(tireA1, 1)
        pi.pinMode(tireA2, 1)
        pi.pinMode(tireB1, 1)
        pi.pinMode(tireB2, 1)

        if direction == "Forward":
            print("Forward")
            pi.digitalWrite(tireA1, 1)
            pi.digitalWrite(tireB1, 1)
            pi.digitalWrite(tireA2, 0)
            pi.digitalWrite(tireB2, 0)
            #time.sleep(1)
        elif direction == "Reverse":
            print("Reverse")
            pi.digitalWrite(tireA1, 0)
            pi.digitalWrite(tireB1, 0)
            pi.digitalWrite(tireA2, 1)
            pi.digitalWrite(tireB2, 1)
            #time.sleep(1)
        elif direction == "Right":
            print("Right")
            pi.digitalWrite(tireA1, 1)
            pi.digitalWrite(tireB1, 0)
            pi.digitalWrite(tireA2, 0)
            pi.digitalWrite(tireB2, 1)
            #time.sleep(1)
        elif direction == "Left":
            print("Left")
            pi.digitalWrite(tireA1, 0)
            pi.digitalWrite(tireB1, 1)
            pi.digitalWrite(tireA2, 1)
            pi.digitalWrite(tireB2, 0)
            #time.sleep(1)     
        else:
            print("Stop")
            pi.digitalWrite(tireA1, 1)
            pi.digitalWrite(tireB1, 1)
            pi.digitalWrite(tireA2, 1)
            pi.digitalWrite(tireB2, 1)
            #time.sleep(1)

    def manualDrive(self):
        pass

    def autonumousDrive(self):
        while self.driveMode == "Autonumous Drive":
            dirArray = ["Forward", "Reverse", "Right", "Left", "Stop"]
            n = random.randint(0, 4)
            self.drive(dirArray[n])
            sleep(0.5)
            
            on_press(key)
            if key == key.ctrl :
                self.setDriveMode("Manual Drive")
            elif key == key.space :
                self.setDriveMode("Smart Drive")        
        
        self.drive("Stop")

    def smartDrive(self):
        pass        


def main():
    car1.runAlarm()
    car1.drive("Stop")
    #car1.head_light_R(1)

    #car1.turnHeadLights(1)
    #car1.honkTheHorn()
    
    #sleep(0.1)
    #sensor1 = USSensor(24, 25, 20, 21)

    #distance = 100

    #while True:
        #distance = sensor1.get_distance()
        #sleep(0.05)

        #if 200 >= distance > 10:
            #car1.drive("Forward")
            #sleep(0.1)
        #elif distance <= 10:
            #car1.drive("Reverse")
            #sleep(0.1)

    #car1.drive("Stop")
    #sleep(0.1)

if __name__ == '__main__':
    car1 = Car()
    while True:
        main()