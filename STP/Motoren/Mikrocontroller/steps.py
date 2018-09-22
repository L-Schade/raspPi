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
    GPIO.setup(motorPin1, GPIO.OUTPUT)
    GPIO.setup(motorPin2, GPIO.OUTPUT)
    GPIO.setup(motorPin3, GPIO.OUTPUT)


def loop(n):
    # n = millis() / 3000     # 3 Sekunden

    if n == 0:
        stop()
    elif n == 1:
        rechtsrum(lowSpeed)
    elif n == 2:
        stop()
    elif n == 3:
        linksrum(lowSpeed)
    elif n == 4:
        stop()
    elif n == 5:
        rechtsrum(highSpeed)
    elif n == 6:
        stop()
    elif n == 7:
        linksrum(highSpeed)

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


def rechtsrum(motorSpeed):
    # 1
    GPIO.output(motorPin3, HIGH)
    GPIO.output(motorPin2, LOW)
    GPIO.output(motorPin1, LOW)
    time.sleep(motorSpeed)

    # 2
    GPIO.output(motorPin3, HIGH)
    GPIO.output(motorPin2, HIGH)
    GPIO.output(motorPin1, LOW)
    time.sleep(motorSpeed)

    # 3
    GPIO.output(motorPin3, LOW)
    GPIO.output(motorPin2, HIGH)
    GPIO.output(motorPin1, LOW)
    time.sleep(motorSpeed)

    # 4
    GPIO.output(motorPin3, LOW)
    GPIO.output(motorPin2, HIGH)
    GPIO.output(motorPin1, HIGH)
    time.sleep(motorSpeed)

    # 5
    GPIO.output(motorPin3, LOW)
    GPIO.output(motorPin2, LOW)
    GPIO.output(motorPin1, HIGH)
    time.sleep(motorSpeed)

    # 6
    GPIO.output(motorPin3, HIGH)
    GPIO.output(motorPin2, LOW)
    GPIO.output(motorPin1, HIGH)
    time.sleep(motorSpeed)


def linksrum(motorSpeed):
    # 1
    GPIO.output(motorPin1, HIGH)
    GPIO.output(motorPin2, LOW)
    GPIO.output(motorPin3, LOW)
    time.sleep(motorSpeed)

    # 2
    GPIO.output(motorPin1, HIGH)
    GPIO.output(motorPin2, HIGH)
    GPIO.output(motorPin3, LOW)
    time.sleep(motorSpeed)

    # 3
    GPIO.output(motorPin1, LOW)
    GPIO.output(motorPin2, HIGH)
    GPIO.output(motorPin3, LOW)
    time.sleep(motorSpeed)

    # 4
    GPIO.output(motorPin1, LOW)
    GPIO.output(motorPin2, HIGH)
    GPIO.output(motorPin3, HIGH)
    time.sleep(motorSpeed)

    # 5
    GPIO.output(motorPin1, LOW)
    GPIO.output(motorPin2, LOW)
    GPIO.output(motorPin3, HIGH)
    time.sleep(motorSpeed)

    # 6
    GPIO.output(motorPin1, HIGH)
    GPIO.output(motorPin2, LOW)
    GPIO.output(motorPin3, HIGH)
    time.sleep(motorSpeed)


def stop():
    GPIO.output(motorPin3, LOW)
    GPIO.output(motorPin2, LOW)
    GPIO.output(motorPin1, LOW)


setup()
n = raw_input()
loop(n)
stop()
