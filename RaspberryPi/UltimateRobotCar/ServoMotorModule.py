import RPi.GPIO as GPIO
from time import sleep

class ServoMotor():
  def __init__(self, SIGNAL):
    self.SIGNAL = SIGNAL
    self.FREQ = 50
    self.ANGLE_MAX = 12
    self.ANGLE_MIDDLE = 7
    self.ANGLE_MIN = 2
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.SIGNAL, GPIO.OUT)
    self.pwm = GPIO.PWM(self.SIGNAL, self.FREQ) # GPIO 23 for PWM with 50Hz
    self.pwm.start(self.ANGLE_MIDDLE) # Initialization
    sleep(1)


  def autoRotate(self, speed):
    self.pwm.start(self.ANGLE_MIN) # Initialization
    try:
      while True:
        self.pwm.ChangeDutyCycle(self.ANGLE_MIN)
        sleep(speed)
        self.pwm.ChangeDutyCycle(self.ANGLE_MIDDLE)
        sleep(speed)
        self.pwm.ChangeDutyCycle(self.ANGLE_MAX)
        sleep(speed)
        self.pwm.ChangeDutyCycle(self.ANGLE_MIDDLE)
        sleep(speed)
    except KeyboardInterrupt:
      self.pwm.stop()
      GPIO.cleanup()

  def setAngle(self, angle):
    duty = angle / 18 + 2
    GPIO.output(self.SIGNAL, True)
    self.pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(self.SIGNAL, False)
    self.pwm.ChangeDutyCycle(duty)

  


def main():
  servo1 = ServoMotor(23)
  servo1.autoRotate(0.4)
  print("FR")
  servo1.setAngle(90)
  sleep(1)

  
  for angle in range(0, 190, 45) :
    print(angle)
    servo1.setAngle(angle)
    sleep(0.5)

  print("FR")
  servo1.setAngle(90)
  sleep(1)
    

if __name__ == '__main__':
    main()