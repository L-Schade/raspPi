from time import sleep
import pigpio
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pi = pigpio.pi()

m1 = 17
pi.set_servo_pulsewidth(m1, 2000)
sleep(2)
pi.set_servo_pulsewidth(m1, 1000)
sleep(2)

pi.set_servo_pulsewidth(m1, 0)
pi.stop()
