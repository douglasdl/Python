#from MotorModule import Motor
from time import sleep
import KeyPressModule as kp
from threading import Thread
#from Car import Car
from ServoMotorModule import ServoMotor

#motor = Motor(2, 3, 4, 17, 22, 27)
#motor = Motor(2, 3, 4, 17, 22, 27)

kp.init()
#robot = Car()
cameraServo = ServoMotor(23)
#usServoR = ServoMotor(12)
#usServoL = ServoMotor(18)
#headLightR = 20
#headLightL = 6
#tailLightR = 2
#tailLightL = 3
#motorA1 = 4
#motorA2 = 17
#motorB1 = 27
#motorB2 = 22
#US_TRIG = 24
#US_ECHO1 = 25
#US_ECHO2 = 5
#US_ECHO3 = 26
#alarm_Off = 16
#horn = 21



def streamCamera():
    while True:
        print("Live Streaming!")
        sleep(1)
            

def secondFunction():
    cameraServo.autoRotate(1)


def main():
    t1 = Thread(target = streamCamera)
    t1.start()
    t2 = Thread(target = secondFunction)
    t2.start()
    #t3 = Thread(target = robot.getPosition)
    #t3.start()
    #t4 = Thread(target = robot.getCameraInfo)
    #t4.start()
    #t5 = Thread(target = usServoR.autoRotate(1))
    #t5.start()
    #t6 = Thread(target = usServoL.autoRotate(1))
    #t6.start()


    if kp.getKey('UP'):
        print("UP")
        #robot.move("Forward")
        
        #motor.move(0.6, 0, 0.1)
    elif kp.getKey('DOWN'):
        print("DOWN")
        #robot.move("Backward")
        
        #motor.move(-0.6, 0, 0.1)
    elif kp.getKey('RIGHT'):
        print("RIGHT")
        #motor.move(0.5, -0.3, 0.1)
        robot.move("Right")
    elif kp.getKey('LEFT'):
        print("LEFT")
        #robot.move("Left")
    elif kp.getKey('w'):
        print("w")
        #robot.moveCamera("Up")
    elif kp.getKey('s'):
        print("s")
        #robot.moveCamera("Down")
    elif kp.getKey('a'):
        print("a")
        #robot.moveCamera("Left")
    elif kp.getKey('d'):
        print("d")
        #robot.moveCamera("Right")            
    elif kp.getKey('SPACE'):
        print("Quit!")
        sleep(1)
            
    else:
        print("STOP")
        #motor.stop(0.1)      


if __name__ == '__main__':
    while True:
        main()