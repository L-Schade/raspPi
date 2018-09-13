# import RPi.GPIO as GPIO
import pigpio
import time

# pigpio.exceptions = False

# GPIO.setmode(GPIO.BCM)
m1 = 19

pi = pigpio.pi()
pi.set_servo_pulsewidth(m1, 1000)


time.sleep(5)

pi.set_servo_pulsewidth(m1, 0)
pi.stop()


# pi = pigpio.pi();    # connect to Pi
# if not pi.connected:
#     print("nicht verbunden")
# else:
#     print("verbunden")
#
# pi.set_mode(17, pigpio.OUTPUT)
# print ("mode: ", pi.get_mode(m1))
# # print("set to: ",pi.get_servo_pulsewidth(4))
#
# # pi.start()
#
# time.sleep(2)
#
# pi.set_servo_pulsewidth(m1, 2000) # 500-2500
# print("set to: ",pi.get_servo_pulsewidth(4))
#
# time.sleep(2)
#
# print("setting to: ",pi.set_servo_pulsewidth(ESC, 1500))
# print("set to: ",pi.get_servo_pulsewidth(ESC))
#
#
# print("waiting ...")
# time.sleep(6)
# pi.set_servo_pulsewidth(m1, 0)
# pi.stop()