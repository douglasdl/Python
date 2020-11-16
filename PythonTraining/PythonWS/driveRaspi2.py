# coding: utf-8
import wiringpi as pi
import time
import random

def drive(direction):
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
    else:
        print("Stop")
        pi.digitalWrite(tireA1, 1)
        pi.digitalWrite(tireB1, 1)
        pi.digitalWrite(tireA2, 1)
        pi.digitalWrite(tireB2, 1)
        #time.sleep(1)

while True:
    dirArray = ["Forward", "Reverse", "Stop"]
    n = random.randint(0, 2)
    drive(dirArray[n])
    time.sleep(1)

drive("Stop")

