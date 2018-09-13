import time
import RPi.GPIO as GPIO

#a = GPIO.VERSION  
#print(a)
print(GPIO.RPI_INFO)

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)


GPIO.setup(17, GPIO.OUT)    # Servo
GPIO.setup(11, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

m1 = GPIO.PWM(19, 1000) # 1000  GPIO.PWM(pin, frequenz[Hz])
# m1 = GPIO.HARD_PWM(19, 1000)
# m2 = GPIO.PWM(17, 10)
m3 = GPIO.PWM(11, 50)

dc = 5
m1.start(dc)   # start(duty circle [%]) 7-10c
# m2.start(10)
m3.start(0)
print("gestartet")

func = GPIO.gpio_function(19)
print(GPIO.getmode())
print(func)

# m1.ChangeDutyCycle(10)   # 3 - 10
# print m1
time.sleep(10)

print("stop")
m1.stop()
# m2.stop()
m3.stop()

GPIO.output(19, False)
GPIO.output(17, False)
GPIO.output(11, False)
GPIO.cleanup()
# quit()

# try:
#     while True:
#         print("while-Schleife")
#         m1.ChangeDutyCycle(9.5)
#         time.sleep(3)
#         m1.ChangeDutyCycle(1.5)
#         time.sleep(3)
#         m1.ChangeDutyCycle(7.5)
#         time.sleep(3)
#
# except KeyboardInterrupt:
#     print("User Cancelled")
#
# finally:
#     m1.stop()
#     GPIO.cleanup()
#     quit()



# GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
#
# GPIO.setup(4, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port
#
# p = GPIO.PWM(4, 1000)    # create an object p for PWM on port 25 at 50 Hertz
#                         # you can have more than one of these, but they need
#                         # different names for each port
#                         # e.g. p1, p2, motor, servo1 etc.
#
# p.start(50)             # start the PWM on 50 percent duty cycle
#                         # duty cycle value can be 0.0 to 100.0%, floats are OK
#
# time.sleep(10)
# p.ChangeDutyCycle(90)   # change the duty cycle to 90%
#
# p.ChangeFrequency(100)  # change the frequency to 100 Hz (floats also work)
#                         # e.g. 100.5, 5.2
#
# p.stop()                # stop the PWM output
#
# GPIO.cleanup()          # when your program exits, tidy up after yourself
