from time import sleep

class Car():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cameraAngle = 0
        self.cameraStatus = "Off"

    def getPosition(self):
        print("x: {} y: {}".format(self.x, self.y))
        sleep(0.1)
        #return { self.x, self.y }

    def getCameraInfo(self):
        print("Camera Angle: {} Status: {}".format(self.cameraAngle, self.cameraStatus))
        sleep(0.1)
    

    def moveCamera(self, direction):
        if direction == "Up":
            self.cameraAngle = 0
        elif direction == "Down":
            print("Take picture or turn OFF the camera!")
        elif direction == "Right":
            if self.cameraAngle <= 90:
                self.cameraAngle += 1
            else:
                self.cameraAngle = 90    
        elif direction == "Left":
            if self.cameraAngle >= -90:
                self.cameraAngle -= 1
            else:
                self.cameraAngle = -90    
        else:
            print("Camera Stopped!")
       

    def move(self, direction):
        if direction == "Forward":
            self.y += 1
        elif direction == "Backward":
            self.y -= 1
        elif direction == "Right":
            self.x += 1
        elif direction == "Left":
            self.x -= 1
        else:
            print("Stopped!")
            
def main():
    carro = Car()
    carro.getPosition()
    carro.getCameraInfo()

if __name__ == '__main__':
    main()