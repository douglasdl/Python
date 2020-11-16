#from MotorModule import Motor
import KeyPressModule as kp

#motor = Motor(2, 3, 4, 17, 22, 27)

kp.init()

def main():
    # Wheels Control
    if kp.getKey('UP'):
        print("Forward")
        #motor.move(0.6, 0, 0.1)
    elif kp.getKey('DOWN'):
        print("Backward")
        #motor.move(-0.6, 0, 0.1)
    elif kp.getKey('RIGHT'):
        print("Turning Right")
        #motor.move(0.5, -0.3, 0.1)
    elif kp.getKey('LEFT'):
        print("Turning Left")
        #motor.move(0.5, 0.3, 0.1)        
    else:
        print("Stopping")
        #motor.stop(0.1)      


if __name__ == '__main__':
    while True:
        main()