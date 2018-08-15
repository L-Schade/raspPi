import RPIO
from RPIO import PWM
import RPi.GPIO

# todo
# RuntimeError: No access to /dev/mem. Try running as root!

servo = PWM.Servo()
servo.set_servo(17, 1200)
servo.set_servo(17, 2000)
servo.stop_servo(17)

# RPIO.setup(4, RPIO.OUT)
# RPIO.