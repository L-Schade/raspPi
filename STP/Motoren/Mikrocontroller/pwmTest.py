import wavePWM
import pigpio
import time
import os
from subprocess import Popen, PIPE

sudo_password = '220513'
command = 'pigpiod'.split()

p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE,
          universal_newlines=True)
sudo_prompt = p.communicate(sudo_password + '\n')[1]

pi=pigpio.pi()
pwm=wavePWM.PWM(pi)


pwm.set_frequency(1000)
print(pwm.frequency)
print(pwm.get_cycle_length())
print(pwm.get_GPIO_settings(4))
print(pwm.get_GPIO_settings(23))
print(pwm.get_GPIO_settings(24))
print("\n")

##pwm.update()

pwm.set_pulse_start_and_length_in_fraction(4,0,0.6)     ## 0.2
pwm.set_pulse_start_and_length_in_fraction(23,0.33,0.6)
pwm.set_pulse_start_and_length_in_fraction(24,0.66,0.6)

##pwm.set_pulse_length_in_micros(4, 500) 
##pwm.set_pulse_length_in_fraction(4, 0.5)

##pwm.set_pulse_start_and_length_in_micros(4,0,12)
##pwm.set_pulse_start_and_length_in_micros(23,0.33,12)
##pwm.set_pulse_start_and_length_in_micros(24,0.66,12)


pwm.update()

print(pwm.frequency)
print(pwm.get_cycle_length())
print(pwm.get_GPIO_settings(4))
print(pwm.get_GPIO_settings(23))
print(pwm.get_GPIO_settings(24))


time.sleep(0.125)
##time.sleep(2)
pwm.cancel()