# coding: utf-8
import wiringpi as pi
from time import sleep
import random
from pynput.keyboard import Listener
import MotorModule as mm


motor1 = mm.Motor(4, 4, 17, 22, 22, 27)




def on_press(key):
    print("Key pressed: {0}".format(key))
    print(key)
    if key == key.up :
        motor1.moveForward(0.8, 0.0, 1)
        sleep(0.1)
    elif key == key.down :
        motor1.moveReverse(0.5, 0.0, 1)
    elif key == key.right :
        motor1.moveForward(0.5, 0.5, 1)
    elif key == key.left :
        motor1.moveForward(0.5, -0.5, 1)
    elif key == key.space :
        motor1.moveForward(0.5, 0.0, 1)
            

def on_release(key):
    drive("Stop")    




dirArray = ["Forward", "Reverse", "Right", "Left", "Stop"]

def drive(direction):
    tireA1 = 17
    tireA2 = 4 #mode
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

#while True:
    #dirArray = ["Forward", "Reverse", "Stop"]
    #n = random.randint(0, 2)
    #drive(dirArray[n])
    #time.sleep(1)

#drive("Stop")


#drive("Right")
#time.sleep(1)
#drive("Forward")
#time.sleep(1)
#drive("Stop")
#time.sleep(1)

# Setup the listener by creating an instance in a with statement and using it's .join() method to join it to the main thread.
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

