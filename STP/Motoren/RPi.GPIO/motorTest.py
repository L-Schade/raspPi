import RPi.GPIO as GPIO
import time


ind = 0

servoPIN = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 19 als PWM mit 50Hz
p.start(0) # Initialisierung

# time.sleep(5)
# p.stop()
# GPIO.cleanup()


# p.ChangeDutyCycle(10)
# time.sleep(0.5)
# p.ChangeDutyCycle(9)
# time.sleep(5)
# p.stop()

# time.sleep(10)

try:
    print("try")
    while True:
        if ind == 2:
            print("stop")
            p.stop()
            GPIO.cleanup()
            exit()
        else:
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(7)
            time.sleep(0.5)
            p.ChangeDutyCycle(6)
            time.sleep(0.5)
            ind += 1

            print("sleep")
            time.sleep(3)


except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
