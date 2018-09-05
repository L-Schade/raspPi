import RPIO
from RPIO import PWM


# todo
# RuntimeError: No access to /dev/mem. Try running as root!
# im Terminal mit sudo ausfuehren

servo = PWM.Servo()
servo.set_servo(19, 1200)
servo.set_servo(17, 2000)
servo.stop_servo(17)


PWM.setup()
PWM.init_channel(0)
PWM.add_channel_pulse(0, 19, 0, 50)
PWM.add_channel_pulse(0, 19 ,100 ,50)
PWM.clear_channel_gpio(0, 19)
PWM.cleanup()


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
