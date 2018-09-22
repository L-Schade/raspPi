import RPi.GPIO as GPIO 
import time

servo_pin1 = 4
servo_pin2 = 23
servo_pin3 = 24

null_deg = 0.5
oneeightnull_deg = 2.5

##frequency = 50.0
frequency = 1000.0

# frequency: 50 Hz
##period = 1000/frequency

# frequency: 1000 Hz
period = 20000/frequency

k = 100/period
null_deg_duty = null_deg*k
pulse_range = oneeightnull_deg-null_deg
duty_range = pulse_range*k 


GPIO.setmode(GPIO.BCM) 
GPIO.setup(servo_pin1,GPIO.OUT)
GPIO.setup(servo_pin2,GPIO.OUT) 
GPIO.setup(servo_pin3,GPIO.OUT) 

pwm1 = GPIO.PWM(servo_pin1, frequency)
pwm2 = GPIO.PWM(servo_pin2, frequency)
pwm3 = GPIO.PWM(servo_pin2, frequency) 

pwm1.start(0)
pwm2.start(0)
pwm3.start(0) 


def set_angle(angle): 
    duty_cycle=null_deg+(angle/180.0)*duty_range
    pwm1.ChangeDutyCycle(duty_cycle)
    pwm2.ChangeDutyCycle((duty_cycle+10))
    pwm3.ChangeDutyCycle((duty_cycle+20)) 


try: 
    while True: 
        angle = input("Angle 0 to 180: ")
        set_angle(angle) 

finally: 
    print("Cleaning up") 
    GPIO.cleanup()  
