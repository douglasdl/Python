# coding: utf-8
import pigpio
import math
import random
import time

# RasPi connected GPIO number
BUZZER_PIN = 18

DO = 40
RE = 42
MI = 44
FA = 45
SOL = 47
LA = 49
SI = 52

pi1 = pigpio.pi()
pi1.set_mode(BUZZER_PIN, pigpio.OUTPUT)
pi1.hardware_PWM(BUZZER_PIN, 0, 0)

hz=[0]

for i in range(120):
    hz += [int(27.5*(1.05946364**i))]

try:
    #for i in [40, 42, 44, 45, 47, 49, 51, 52]:
    for i in [RE, RE, SI, SOL, SOL, 0, SI, RE, RE, RE, SI, 0, SI, DO, DO, DO, LA, RE, RE, 0, MI, RE, DO, SI, LA, SOL]:
        pi1.hardware_PWM(BUZZER_PIN, hz[i], 500000)
        print(hz[i])
        time.sleep(0.2)
except KeyboardInterrupt:
    pass

#cleanup
pi1.hardware_PWM(BUZZER_PIN, 0, 0)
pi1.set_mode(BUZZER_PIN, pigpio.INPUT)
pi1.stop()