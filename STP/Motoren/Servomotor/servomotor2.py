import RPi.GPIO as GPIO 
import time

servo_pin = 17
# servo_pin = 19
null_deg = 0.5
oneeightnull_deg = 2.5

frequency = 50.0
# frequency = 1000.0

# frequency: 50 Hz
period = 1000/frequency

# frequency: 1000 Hz
# period = 20000/frequency

k = 100/period
null_deg_duty = null_deg*k
pulse_range = oneeightnull_deg-null_deg
duty_range = pulse_range*k 


GPIO.setmode(GPIO.BCM) 
GPIO.setup(servo_pin,GPIO.OUT) 
pwm=GPIO.PWM(servo_pin, frequency) 
pwm.start(0) 


def set_angle(angle): 
    duty_cycle=null_deg+(angle/180.0)*duty_range
    pwm.ChangeDutyCycle(duty_cycle) 


try: 
    while True: 
        angle = input("Angle 0 to 180: ")
        set_angle(angle) 

finally: 
    print("Cleaning up") 
    GPIO.cleanup()  
