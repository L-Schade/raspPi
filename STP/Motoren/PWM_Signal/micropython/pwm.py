import machine
import time

# pins 0, 2, 4, 5, 12, 13, 14 and 15 all support PWM
# the frequency must be between 1Hz and 1kHz

p12 = machine.Pin(12)

pwm12 = machine.PWM(p12)

pwm12.freq(500)
pwm12.duty(512)     # the duty cycle is between 0 (all off) and 1023 (all on), with 512 being a 50% duty


print(pwm12)       # PWM(12, freq=500, duty=512)

time.sleep(6)
pwm12.deinit()


# Servo
servo = machine.PWM(machine.Pin(17), freq=50)
servo.duty(40)
servo.duty(115)
servo.duty(77)