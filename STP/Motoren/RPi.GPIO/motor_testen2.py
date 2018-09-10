import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)

try:
	p.start(0)
	for dc in range(0, 101, 5):
	    p.ChangeDutyCycle(dc)
	    time.sleep(0.1)
	for dc in range(100, -1, -5):
	    p.ChangeDutyCycle(dc)
	    time.sleep(0.1)

finally:
	p.stop()
	GPIO.cleanup() 


