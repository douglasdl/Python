#from MotorModule import Motor
import KeyPressModule as kp




class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.steering = 0
        self.rigth_acceleration = 0
        self.left_acceleration = 0
        self.right_speed = 0
        self.left_speed = 0
        self.velocity = 0
        self.angular_velocity = 0
        self.gear = 0


    def ringAlarm(self):
        print("tocando alarm")

    def ignition(self, ignition_ON = False):
        if ignition_ON:
            print("Ignition ON")
        else:
            print("Ignition OFF")

    def accelerate(self, right_acceleration = 0.5, left_acceleration = 0.5):
        print("Accelerating")
        self.right_acceleration = right_acceleration
        self.left_acceleration = left_acceleration

    def breakPedal(self):
        print("breaking")
        self.acceleration = 0

    def shiftGears(self, gear = 0):
        if gear == self.gear + 1:
            print("▲ Gear: " + self.gear)
        elif gear == self.gear - 1:
            print("▼ Gear: " + self.gear)
        elif gear < 0:
            print("Reverse Gear")
        elif gear == 0:
            print("Park")
        else:
            print("Wrong Gear!")

kp.init()


def main():
    crz = Car("Honda", "CR-Z")
    
    # Wheels Control
    if kp.getKey('SPACE'):
        crz.ignition(True)
    elif kp.getKey('w'):
        crz.accelerate(0.6)        
    elif kp.getKey('s'):
        crz.accelerate(-0.6)
    elif kp.getKey('a'):
        crz.accelerate(0.5, 0.3)        
    elif kp.getKey('d'):
        crz.accelerate(0.3, 0.5)        
    
    # Pedal Shift
    elif kp.getKey('e'):
        crz.shiftGears("UP")        
    elif kp.getKey('q'):
        crz.shiftGears("DOWN")        
  
    


if __name__ == '__main__':
    while True:
        main()