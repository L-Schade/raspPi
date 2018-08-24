# import RPIO
from RPIO import PWM
# from RPi.GPIO import PWM



# todo
# RuntimeError: No access to /dev/mem. Try running as root!

servo = PWM.Servo()
servo.set_servo(17, 1200)
servo.set_servo(17, 2000)
servo.stop_servo(17)

# RPIO.setup(4, RPIO.OUT)
# RPIO.

##import  time
##from  RPIO import  PWM
##servo =  PWM.Servo ()
##servo.set_servo ( 17 , 900 )
##try :
##        while  True :
##                servo.set_servo ( 17 , 750 )
##                time.sleep ( 1 )
##                servo.set_servo ( 17 , 1200 )
##                time.sleep ( 1 )
##                servo.set_servo ( 17 , 2500 )
##                time.sleep ( 1 )
##except KeyboardInterrupt:
##        servo.stop_servo ( 17 )
