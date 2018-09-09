import RPIO
from RPIO import PWM
import time

# todo
# RuntimeError: No access to /dev/mem. Try running as root!
# im Terminal mit sudo ausfuehren

servo = PWM.Servo()

servo.set_servo(19, 1200)   # 1.2ms
# servo.set_servo(17, 2000)   # 2.0ms
# servo.stop_servo(17)
time.sleep(10)


# PWM.setup()
# PWM.init_channel(0)
PWM.init_channel(2)

PWM.add_channel_pulse(2, 19, 7, 1000)
print("wait...")
time.sleep(5)

PWM.add_channel_pulse(0, 19 ,100 ,50)
print("wait...")
time.sleep(5)

servo.stop_servo(17)
servo.stop_servo(19)

# PWM.clear_channel_gpio(0, 17)
PWM.clear_channel_gpio(0, 19)
M.cleanup()


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
