import RPi.GPIO as GPIO
import time

# configurate
m1 = 19
m2 = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)

pwm1 = GPIO.PWM(m1, 1000)
pwm1.start(0)
pwm2 = GPIO.PWM(m2, 100)
pwm2.start(0)
print("ready")


def move():
    GPIO.output(m1, True)
    pwm1.ChangeDutyCycle(7)
    GPIO.output(m2, True)
    pwm2.ChangeDutyCycle(7)
    print("move")


def stop():
    GPIO.output(m1, False)
    pwm1.ChangeDutyCycle(0)
    GPIO.output(m2, False)
    pwm2.ChangeDutyCycle(0)
    print("stop")


try:
    move()
    time.sleep(7)
    stop()
except KeyboardInterrupt:
    print("End")
    GPIO.output(19, False)
    GPIO.output(17, False)
    pwm1.stop()
    pwm2.stop()

GPIO.cleanup()
exit()
