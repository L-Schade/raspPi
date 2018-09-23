import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

m1 = GPIO.PWM(4, 10000)  # channel=12 frequency=50Hz
m2 = GPIO.PWM(23, 10000)
m3 = GPIO.PWM(24, 10000)

m1.start(0)
m2.start(0)
m3.start(0)

try:
    while 1:
        for dc in range(0, 101, 5):
            m1.ChangeDutyCycle(dc)
            m2.ChangeDutyCycle(dc)
            m3.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            m1.ChangeDutyCycle(dc)
            m2.ChangeDutyCycle(dc)
            m3.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
m1.stop()
m2.stop()
m3.stop()
GPIO.cleanup()
