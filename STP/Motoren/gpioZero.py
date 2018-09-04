import time
from gpiozero import Servo
from gpiozero import PWMOutputDevice
from gpiozero import OutputDevice
from gpiozero import Motor


m1 = 19
servo = Servo(m1)
##servo.value(1.0)
##servo.mid()



time.sleep(5)

##a = PWMOutputDevice(13)
##a.on()
##a.value = 0.5             # spinning at half speed.
    


##a = OutputDevice(19)
##b = OutputDevice(14)
##
##a.on()


##motor = Motor(13, 34)
##motor.forward()