from MotorModule import Motor
import KeyPressModule as kp
from USSensorModule import USSensor
from time import sleep
from ServoMotorModule2 import ServoMotor

motor = Motor(4, 4, 17, 22, 22, 27)
servoCamera = ServoMotor(23)

us_sensor = USSensor(24, 25, 20, 21)

kp.init()

def main():
    #print(kp.getKey('s'))
    #motor.move(0.5, 0.3, 2)
    #motor.stop(2)

    #motor.moveForward(-0.2, 0, 1)
    #sleep(0.1)
    #distance = us_sensor.get_distance()
    #sleep(0.05)
    #if 50 >= distance > 30:
        #us_sensor.pre_colision(int(distance / 100))
        #sleep(0.05)
    #elif distance <= 30:
        #us_sensor.pre_colision(3)    
        #motor.moveForward(1, 0, 3)
        #sleep(0.05)
    
    # Car Directions
    if kp.getKey('w'):
        motor.moveForward(0.6, 0, 0.1)
    elif kp.getKey('s'):
        motor.moveForward(-0.6, 0, 0.1)
    elif kp.getKey('d'):
        motor.moveForward(0.9, -0.3, 0.1)
    elif kp.getKey('a'):
        motor.moveForward(0.9, 0.3, 0.1)

    # Camera Directions
    elif kp.getKey('UP'):
        servoCamera.setAngle(10)
    elif kp.getKey('DOWN'):
        servoCamera.setAngle(20)
    elif kp.getKey('RIGHT'):
        servoCamera.setAngle(30)
    elif kp.getKey('LEFT'):
        servoCamera.setAngle(0)              
    else:
        motor.stop()      


if __name__ == '__main__':
    while True:
        main()