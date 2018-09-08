import RPi.GPIO as GPIO
import time

servoPIN = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 1000) # GPIO 19 als PWM mit 50Hz
p.start(5) # Initialisierung
try:
	while True:
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
