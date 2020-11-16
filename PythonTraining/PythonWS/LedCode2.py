from gpiozero import LED
from time import sleep
 
led = LED(20)
 
for i in range(10):
    led.on()
    sleep(0.1 * (10-i))
    led.off()
    sleep(0.1 * (10-i))
 
#led.toggle()