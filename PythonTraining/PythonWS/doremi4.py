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
    for i in [DO, SOL, FA, MI, DO, RE, 0, RE, DO, RE, DO, RE, MI, FA, 0, DO, RE, MI, FA, FA, FA, 0, DO, RE, DO, RE, RE, RE, 0, DO, SOL, FA, MI, MI, MI, 0, DO, RE, MI, FA, FA, FA]:
        pi1.hardware_PWM(BUZZER_PIN, hz[i], 500000)
        print(hz[i])
        time.sleep(0.2)
except KeyboardInterrupt:
    pass

#cleanup
pi1.hardware_PWM(BUZZER_PIN, 0, 0)
pi1.set_mode(BUZZER_PIN, pigpio.INPUT)
pi1.stop()