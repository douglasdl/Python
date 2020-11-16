#from MotorModule import Motor
from time import sleep
import KeyPressModule as kp
from threading import Thread
from Car import Car
#from ServoModule import ServoMotor

#motor = Motor(2, 3, 4, 17, 22, 27)
#motor = Motor(2, 3, 4, 17, 22, 27)

kp.init()
robot = Car()
#cameraServo = ServoMotor()

def streamCamera():
    while True:
        #print("Live Streaming!")
        sleep(1)
            

def secondFunction():
    while True:
        for i in range(2):
            #print(i*i)
            sleep(1)



def main():
    t1 = Thread(target = streamCamera)
    t1.start()
    t2 = Thread(target = secondFunction)
    t2.start()
    t3 = Thread(target = robot.getPosition)
    t3.start()
    t4 = Thread(target = robot.getCameraInfo)
    t4.start()

    
    
    #print(kp.getKey('s'))
    #motor.move(0.5, 0.3, 2)
    #motor.stop(2)

    if kp.getKey('UP'):
        print("UP")
        robot.move("Forward")
        
        #motor.move(0.6, 0, 0.1)
    elif kp.getKey('DOWN'):
        print("DOWN")
        robot.move("Backward")
        
        #motor.move(-0.6, 0, 0.1)
    elif kp.getKey('RIGHT'):
        print("RIGHT")
        #motor.move(0.5, -0.3, 0.1)
        robot.move("Right")
    elif kp.getKey('LEFT'):
        print("LEFT")
        robot.move("Left")
    elif kp.getKey('w'):
        print("w")
        robot.moveCamera("Up")
    elif kp.getKey('s'):
        print("s")
        robot.moveCamera("Down")
    elif kp.getKey('a'):
        print("a")
        robot.moveCamera("Left")
    elif kp.getKey('d'):
        print("d")
        robot.moveCamera("Right")            
    elif kp.getKey('SPACE'):
        print("Quit!")
        sleep(1)
            
    else:
        print("STOP")
        #motor.stop(0.1)      


if __name__ == '__main__':
    while True:
        main()