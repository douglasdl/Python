from MotorModule import Motor
import KeyPressModule as kp
from USSensorModule import USSensor
from time import sleep
from ServoMotorModule2 import ServoMotor
from CameraModule import Camera
from Car import Car

#motor1 = Motor(4, 4, 17, 22, 22, 27)
car1 = Car()
camera1 = Camera()


def main():
    
    
    
    if kp.getKey('UP'):
        print('Key UP was pressed')
        #motor1.moveForward(0.9, 0, 0)
        car1.drive("Forward") 
    elif kp.getKey('DOWN'):
        print('Key DOWN was pressed')
        #motor1.moveReverse(0.9, 0, 0)
        car1.drive("Reverse") 
    elif kp.getKey('RIGHT'):
        print('Key RIGHT was pressed')
        #motor1.moveForward(0.5, -0.3, 0)
        car1.drive("Right") 
    elif kp.getKey('LEFT'):
        print('Key LEFT was pressed')
        #motor1.moveForward(0.5, 0.3, 0) 
        car1.drive("Left") 
    elif kp.getKey('0'):
        print('Key 0 was pressed')
        #motor1.moveForward(0.5, 0.3, 0) 
        camera1.streamCamera()  
    else:
        #motor1.stop(0)  
        car1.drive("Stop")      


if __name__ == '__main__':
    kp.init()
    while True:
        main()