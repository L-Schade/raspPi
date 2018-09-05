import RPi.GPIO as GPIO
import time

# configurate
m1 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m1, GPIO.OUT)

pwm = GPIO.PWM(m1, 10000)
pwm.start(0)
print("ready")


def move():
    GPIO.output(m1, True)
    pwm.ChangeDutyCycle(7)
    print("move")


def stop():
    GPIO.output(m1, False)
    pwm.ChangeDutyCycle(0)
    print("stop")


try:
    move()
    time.sleep(7)
    stop()
except KeyboardInterrupt:
    print("End")
    GPIO.output(19, False)
    pwm.stop()

GPIO.cleanup()
exit()
