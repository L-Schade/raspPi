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


pwm.set_frequency(10000)        # 10k Hz
print(pwm.frequency)
print(pwm.get_cycle_length())
print(pwm.get_GPIO_settings(4))
print(pwm.get_GPIO_settings(23))
print(pwm.get_GPIO_settings(24))
print("\n")

##pwm.update()

##pwm.set_pulse_start_and_length_in_fraction(4,0,0.75)   
##pwm.set_pulse_start_and_length_in_fraction(23,0.33,0.75)
##pwm.set_pulse_start_and_length_in_fraction(24,0.66,0.75)

##pwm.set_pulse_start_and_length_in_fraction(4,0.33,0.2)     ## 0.2
##pwm.set_pulse_start_and_length_in_fraction(23,0.66,0.2)
##pwm.set_pulse_start_and_length_in_fraction(24,0,0.2)

##time.sleep(0.125)
##time.sleep(2)

# haengt noch manchmal
pwm.set_pulse_start_and_length_in_micros(4,0,80)        # ca 4 Grad
pwm.set_pulse_start_and_length_in_micros(23,0.33,80)
pwm.set_pulse_start_and_length_in_micros(24,0.66,80)


pwm.update()

print(pwm.frequency)
print(pwm.get_cycle_length())
print(pwm.get_GPIO_settings(4))
print(pwm.get_GPIO_settings(23))
print(pwm.get_GPIO_settings(24))

pwm.cancel()

##pwm.set_pulse_length_in_micros(4, 500) 
##pwm.set_pulse_length_in_fraction(4, 0.5)


