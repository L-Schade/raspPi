import RPi.GPIO as GPIO 
import time

servo_pin = 17
0_deg = 0.5
180_deg = 2.5
frequency = 50.0 

period = 1000/frequency 
k = 100/period 
0_deg_duty = 0_deg*k 
pulse_range = 180_deg-0_deg 
duty_range = pulse_range*k 

GPIO.setmode(GPIO.BCM) 
GPIO.setup(servo_pin,GPIO.OUT) 
pwm=GPIO.PWM(servo_pin, frequency) 
pwm.start(0) 


def set_angle(angle): 
    duty_cycle=0_deg+(angle/180.0)*duty_range 
    pwm.ChangeDutyCycle(duty_cycle) 


try: 
    while True: 
        angle = input("Angle 0⁰ to 180⁰")
        set_angle(angle) 

finally: 
    print("Cleaning up") 
    GPIO.cleanup()  
