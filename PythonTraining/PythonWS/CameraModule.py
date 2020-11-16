# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

class Camera():
    def __init__(self):
        #self.EnableA = EnableA

        # initialize the camera and grab a reference to the raw camera capture
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
        # allow the camera to warmup
        time.sleep(0.1)

    def streamCamera(self):    
        # capture frames from the camera
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
	        # grab the raw NumPy array representing the image, then initialize the timestamp
	        # and occupied/unoccupied text
	        self.image = frame.array
	        # show the frame
	        cv2.imshow("Frame", self.image)
	        key = cv2.waitKey(1) & 0xFF
	        # clear the stream in preparation for the next frame
	        self.rawCapture.truncate(0)
	        # if the `q` key was pressed, break from the loop
	        if key == ord("q"):
		        break
            
    
    def stopCamera(self, setOff = True):
        pass

def main():
    camera1.streamCamera()

if __name__ == '__main__':
    camera1 = Camera()
    main()