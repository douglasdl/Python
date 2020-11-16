#sudo pigpiod

# coding: utf-8
import wiringpi as pi
from time import sleep
import random
from pynput.keyboard import Listener
import pigpio
from Car import Car
from gpiozero import Button
button = Button(16)
   

robot = Car("Xplorer", 0)
robot.myfunc()

def init_controls(self):
        """Define keys and add listener"""
        self.controls = {
            'w': 'forward',
            's': 'backward',
            'a': 'left',
            'd': 'right',
            'Key.space': 'up',
            'Key.shift': 'down',
            'Key.shift_r': 'down',
            'q': 'forward',
            'e': 'forward',
            'i': 'forward',
            'k': 'forward',
            'j': 'forward',
            'l': 'forward',
            # arrow keys 
            'Key.left': 'forward',
            'Key.right': 'forward',
            'Key.up': 'forward',
            'Key.down': 'forward',
            'Key.tab': 'forward',
            'Key.backspace': 'forward',
            'p': 'forward',
            't': 'forward',
            'r': 'forward',
            'z': 'forward',
            'Key.enter': 'forward'
        }
        
robot.alarmStatus = False
while robot.alarmStatus == True:
    robot.runAlarm()
    if button.is_pressed:
        print("Button Pressed")
        if robot.alarmStatus == True:
            robot.alarmStatus = False
        else:
            robot.alarmStatus = True    
    else:
        print("Idle")

robot.isCheckingDistance = True
while robot.isCheckingDistance:
    d1 = robot.USSensor1.get_distance()
    d2 = robot.USSensor2.get_distance()
    d3 = robot.USSensor3.get_distance()
    if d1 <= 20:
        robot.USSensor1.pre_colision(1)
    if d2 <= 20:
        robot.USSensor2.pre_colision(1)
    if d3 <= 20:
        robot.USSensor3.pre_colision(1)        


""" 
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

"""
def on_press(key):
    print("Key pressed: {0}".format(key))
    
    if key == 'z' :
        pass
        #robot.drive("OFF")
    elif key == 'q' :
        robot.ignitionON()
    elif key == key.up and robot.driveMode == "Manual Drive" :
        robot.drive("Forward")
    elif key == key.down and robot.driveMode == "Manual Drive" :
        robot.drive("Reverse")
    elif key == key.right and robot.driveMode == "Manual Drive" :
        robot.drive("Right")
    elif key == key.left and robot.driveMode == "Manual Drive" :
        robot.drive("Left")

    elif key == 'w' and robot.driveMode == "Manual Drive" :
        print("W")    
    elif key == 's' and robot.driveMode == "Manual Drive" :
        print("S")
    elif key == 'a' and robot.driveMode == "Manual Drive" :
        print("A")
    elif key == 'd' and robot.driveMode == "Manual Drive" :
        print("D")

    elif key == key.ctrl_r :
        robot.honkTheHorn()    
    elif key == key.alt :
        if robot.headLightStatus == 0 :
            robot.turnHeadLights(1)
        else:
            robot.turnHeadLights(0)      
    elif key == key.ctrl :
        robot.setDriveMode("Manual Drive")
        robot.manualDrive()
    elif key == key.shift :
        robot.setDriveMode("Autonumous Drive")
        #robot.autonumousDrive()
    elif key == key.space :
        robot.setDriveMode("Smart Drive")
        #robot.smartDrive()
        
    else:
        robot.drive("OFF")        


def on_release(key):
    print('{0} released'.format(key))
    if key == key.esc:
        # Stop listener
        return False

"""
def on_release(key):
    if robot.driveMode == "Manual Drive" :
        if key == key.up or key == key.down or key == key.right or key == key.left :
            robot.drive("Stop")  
"""

# Setup the listener by creating an instance in a with statement and using it's .join() method to join it to the main thread.
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()