import RPi.GPIO as GPIO
import time

servoPIN = 17
servoPin1 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPin1, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung

p1 = GPIO.PWM(servoPin1, 1000) # GPIO 17 als PWM mit 50Hz
p1.start(2.5) # Initialisierung
try:
    while True:
        p.ChangeDutyCycle(5)
        p1.ChangeDutyCycle(5)
        time.sleep(0.05)
        p.ChangeDutyCycle(7.5)
        p1.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        p1.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(12.5)
        p1.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        p1.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        p1.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(5)
        p1.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(2.5)
        p1.ChangeDutyCycle(10)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
