# http://www.hobby-werkstatt-blog.de/arduino/357-schrittmotor-28byj48-am-arduino.php
import RPi.GPIO as GPIO
import time

motorPin1 = 4       # yellow  - In 1
motorPin2 = 23      # green   - In 2
motorPin3 = 24      # blue - In 3

lowSpeed  = 10000   # Notabene: nicht über 16000
highSpeed =  1000

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motorPin1, GPIO.OUT)
    GPIO.setup(motorPin2, GPIO.OUT)
    GPIO.setup(motorPin3, GPIO.OUT)


def loop(n):
    # n = millis() / 3000     # 3 Sekunden

    if n == 0:
        stop()
    elif n == 1:
        # rechtsrum(lowSpeed)
        rechts(lowSpeed)
    elif n == 2:
        stop()
    elif n == 3:
        # linksrum(lowSpeed)
        links(lowSpeed)
    elif n == 4:
        stop()
    elif n == 5:
        # rechtsrum(highSpeed)
        rechts(highSpeed)
    elif n == 6:
        stop()
    elif n == 7:
        # linksrum(highSpeed)
        links(highSpeed)

    # switch(n % 8)
    # { case 0: stop();               break;
    #   case 1: rechtsrum(lowSpeed);  break;
    #   case 2: stop();               break;
    #   case 3: linksrum(lowSpeed);   break;
    #   case 4: stop();               break;
    #   case 5: rechtsrum(highSpeed); break;
    #   case 6: stop();               break;
    #   case 7: linksrum(highSpeed);  break;
    # }

# halfstep
def rechtsrum(motorSpeed):
    # 1
    GPIO.output(motorPin3, GPIO.HIGH)
    GPIO.output(motorPin2, GPIO.LOW)
    GPIO.output(motorPin1, GPIO.LOW)
    time.sleep(motorSpeed)

    # 2
    GPIO.output(motorPin3, GPIO.HIGH)
    GPIO.output(motorPin2, GPIO.HIGH)
    GPIO.output(motorPin1, GPIO.LOW)
    time.sleep(motorSpeed)

    # 3
    GPIO.output(motorPin3, GPIO.LOW)
    GPIO.output(motorPin2, GPIO.HIGH)
    GPIO.output(motorPin1, GPIO.LOW)
    time.sleep(motorSpeed)

    # 4
    GPIO.output(motorPin3, GPIO.LOW)
    GPIO.output(motorPin2, GPIO.HIGH)
    GPIO.output(motorPin1, GPIO.HIGH)
    time.sleep(motorSpeed)

    # 5
    GPIO.output(motorPin3, GPIO.LOW)
    GPIO.output(motorPin2, GPIO.LOW)
    GPIO.output(motorPin1, GPIO.HIGH)
    time.sleep(motorSpeed)

    # 6
    GPIO.output(motorPin3, GPIO.HIGH)
    GPIO.output(motorPin2, GPIO.LOW)
    GPIO.output(motorPin1, GPIO.HIGH)
    time.sleep(motorSpeed)


def rechts(motorSpeed):
    # 1
    GPIO.output(motorPin3, 1)
    GPIO.output(motorPin2, 0)
    GPIO.output(motorPin1, 0)
    time.sleep(motorSpeed)

    # 2
    GPIO.output(motorPin3, 1)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin1, 0)
    time.sleep(motorSpeed)

    # 3
    GPIO.output(motorPin3, 0)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin1, 0)
    time.sleep(motorSpeed)

    # 4
    GPIO.output(motorPin3, 0)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin1, 1)
    time.sleep(motorSpeed)

    # 5
    GPIO.output(motorPin3, 0)
    GPIO.output(motorPin2, 0)
    GPIO.output(motorPin1, 1)
    time.sleep(motorSpeed)

    # 6
    GPIO.output(motorPin3, 1)
    GPIO.output(motorPin2, 0)
    GPIO.output(motorPin1, 1)
    time.sleep(motorSpeed)


def linksrum(motorSpeed):
    # 1
    GPIO.output(motorPin1, GPIO.HIGH)
    GPIO.output(motorPin2, GPIO.LOW)
    GPIO.output(motorPin3, GPIO.LOW)
    time.sleep(motorSpeed)

    # 2
    GPIO.output(motorPin1, GPIO.HIGH)
    GPIO.output(motorPin2, GPIO.HIGH)
    GPIO.output(motorPin3, GPIO.LOW)
    time.sleep(motorSpeed)

    # 3
    GPIO.output(motorPin1, GPIO.LOW)
    GPIO.output(motorPin2, GPIO.HIGH)
    GPIO.output(motorPin3, GPIO.LOW)
    time.sleep(motorSpeed)

    # 4
    GPIO.output(motorPin1, GPIO.LOW)
    GPIO.output(motorPin2, GPIO.HIGH)
    GPIO.output(motorPin3, GPIO.HIGH)
    time.sleep(motorSpeed)

    # 5
    GPIO.output(motorPin1, GPIO.LOW)
    GPIO.output(motorPin2, GPIO.LOW)
    GPIO.output(motorPin3, GPIO.HIGH)
    time.sleep(motorSpeed)

    # 6
    GPIO.output(motorPin1, GPIO.HIGH)
    GPIO.output(motorPin2, GPIO.LOW)
    GPIO.output(motorPin3, GPIO.HIGH)
    time.sleep(motorSpeed)


def links(motorSpeed):
    # 1
    GPIO.output(motorPin1, 1)
    GPIO.output(motorPin2, 0)
    GPIO.output(motorPin3, 0)
    time.sleep(motorSpeed)

    # 2
    GPIO.output(motorPin1, 1)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin3, 0)
    time.sleep(motorSpeed)

    # 3
    GPIO.output(motorPin1, 0)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin3, 0)
    time.sleep(motorSpeed)

    # 4
    GPIO.output(motorPin1, 0)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin3, 1)
    time.sleep(motorSpeed)

    # 5
    GPIO.output(motorPin1, 0)
    GPIO.output(motorPin2, 0)
    GPIO.output(motorPin3, 1)
    time.sleep(motorSpeed)

    # 6
    GPIO.output(motorPin1, 1)
    GPIO.output(motorPin2, 0)
    GPIO.output(motorPin3, 1)
    time.sleep(motorSpeed)


# fullstep
def rechtsF(motorSpeed):
    # 1
    GPIO.output(motorPin3, 1)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin1, 0)
    time.sleep(motorSpeed)

    # 2
    GPIO.output(motorPin3, 0)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin1, 1)
    time.sleep(motorSpeed)

    # 3
    GPIO.output(motorPin3, 1)
    GPIO.output(motorPin2, 0)
    GPIO.output(motorPin1, 1)
    time.sleep(motorSpeed)

def linksF(motorSpeed):
    # 1
    GPIO.output(motorPin1, 1)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin3, 0)
    time.sleep(motorSpeed)

    # 2
    GPIO.output(motorPin1, 0)
    GPIO.output(motorPin2, 1)
    GPIO.output(motorPin3, 1)
    time.sleep(motorSpeed)

    # 3
    GPIO.output(motorPin1, 1)
    GPIO.output(motorPin2, 0)
    GPIO.output(motorPin3, 1)
    time.sleep(motorSpeed)


def stop():
    GPIO.output(motorPin3, GPIO.LOW)
    GPIO.output(motorPin2, GPIO.LOW)
    GPIO.output(motorPin1, GPIO.LOW)


def stop1():
    GPIO.output(motorPin3, 0)
    GPIO.output(motorPin2, 0)
    GPIO.output(motorPin1, 0)


setup()
n = raw_input()
loop(n)
stop()
