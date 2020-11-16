#sudo pigpiod

# coding: utf-8
import wiringpi as pi
from time import sleep
import random
from pynput.keyboard import Listener
import pigpio



def drive(direction, rotate):
    tireA1 = 17
    tireA2 = 4
    tireB1 = 22
    tireB2 = 27

    FREQ = 60
    RANGE = 100

    pi = pigpio.pi()

    if direction == "Forward":
        pi.set_mode(tireA1, pigpio.OUTPUT)
        pi.set_mode(tireB1, pigpio.OUTPUT)
        pi.set_PWM_frequency(tireA1, FREQ)
        pi.set_PWM_frequency(tireB1, FREQ)
        pi.set_PWM_range(tireA1, RANGE)
        pi.set_PWM_range(tireB1, RANGE)
    elif direction == "Reverse":
        pi.set_mode(tireA2, pigpio.OUTPUT)
        pi.set_mode(tireB2, pigpio.OUTPUT)
        pi.set_PWM_frequency(tireA2, FREQ)
        pi.set_PWM_frequency(tireB2, FREQ)
        pi.set_PWM_range(tireA2, RANGE)
        pi.set_PWM_range(tireB2, RANGE)
    elif direction == "Stop":
        pass    


    d = 0
    r = 150
    #rotate = False
    while rotate:
        if direction == "Forward":
            pi.set_PWM_dutycycle(tireA1, d)
            pi.set_PWM_dutycycle(tireB1, d)
        elif direction == "Reverse":    
            pi.set_PWM_dutycycle(tireA2, d)
            pi.set_PWM_dutycycle(tireB2, d)
        elif direction == "Stop":
            pass  
        
        sleep(0.01)
        d += r
        if d >= RANGE or d <= 0:
            r = 10
            #r *= -1
            rotate = False
            
    if direction == "Forward":
        pi.set_mode(tireA1, pigpio.INPUT)
        pi.set_mode(tireB1, pigpio.INPUT)
    elif direction == "Reverse": 
        pi.set_mode(tireA2, pigpio.INPUT)
        pi.set_mode(tireB2, pigpio.INPUT)
    elif direction == "Stop":
        pass     
    pi.stop()


def on_press(key):
    print("Key pressed: {0}".format(key))
    print(key)
    if key == key.up :
        drive("Forward", True)
    elif key == key.down :
        drive("Reverse", True)
    elif key == key.right :
        drive("Right", True)
    elif key == key.left :
        drive("Left", True)
    elif key == key.space :
        drive("Stop", False)
    elif key == key.esc :
        drive("OFF", False)    
            

def on_release(key):
    drive("Stop", False)    




dirArray = ["Forward", "Reverse", "Right", "Left", "Stop"]




#while True:
    #dirArray = ["Forward", "Reverse", "Stop"]
    #n = random.randint(0, 2)
    #drive(dirArray[n])
    #time.sleep(1)

#drive("Stop")




# Setup the listener by creating an instance in a with statement and using it's .join() method to join it to the main thread.
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

