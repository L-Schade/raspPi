import RPi.GPIO as GPIO

EN1 = 5
EN2 = 6
EN3 = 7

IN1 = 4
IN2 = 23
IN3 = 24


##// SPWM (Sine Wave)
##//const int pwmSin[] = {127, 138, 149, 160, 170, 181, 191, 200, 209, 217, 224, 231, 237, 242, 246, 250, 252, 254, 254, 254, 252, 250, 246, 242, 237, 231, 224, 217, 209, 200, 191, 181, 170, 160, 149, 138, 127, 116, 105, 94, 84, 73, 64, 54, 45, 37, 30, 23, 17, 12, 8, 4, 2, 0, 0, 0, 2, 4, 8, 12, 17, 23, 30, 37, 45, 54, 64, 73, 84, 94, 105, 116 };


##/// SVPWM (Space Vector Wave)
##//const int pwmSin[] = {128, 147, 166, 185, 203, 221, 238, 243, 248, 251, 253, 255, 255, 255, 253, 251, 248, 243, 238, 243, 248, 251, 253, 255, 255, 255, 253, 251, 248, 243, 238, 221, 203, 185, 166, 147, 128, 109, 90, 71, 53, 35, 18, 13, 8, 5, 3, 1, 1, 1, 3, 5, 8, 13, 18, 13, 8, 5, 3, 1, 1, 1, 3, 5, 8, 13, 18, 35, 53, 71, 90, 109};
pwmSin = [128, 132, 136, 140, 143, 147, 151, 155, 159, 162, 166, 170, 174, 178, 181, 185, 189, 192, 196, 200, 203, 207,
          211, 214, 218, 221, 225, 228, 232, 235, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 248, 249, 250,
          250, 251, 252, 252, 253, 253, 253, 254, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
          255, 254, 254, 254, 253, 253, 253, 252, 252, 251, 250, 250, 249, 248, 248, 247, 246, 245, 244, 243, 242, 241,
          240, 239, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 248, 249, 250, 250, 251, 252, 252, 253, 253,
          253, 254, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 254, 254, 253, 253,
          253, 252, 252, 251, 250, 250, 249, 248, 248, 247, 246, 245, 244, 243, 242, 241, 240, 239, 238, 235, 232, 228,
          225, 221, 218, 214, 211, 207, 203, 200, 196, 192, 189, 185, 181, 178, 174, 170, 166, 162, 159, 155, 151, 147,
          143, 140, 136, 132, 128, 124, 120, 116, 113, 109, 105, 101, 97, 94, 90, 86, 82, 78, 75, 71, 67, 64, 60, 56,
          53, 49, 45, 42, 38, 35, 31, 28, 24, 21, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 8, 7, 6, 6, 5, 4, 4, 3, 3,
          3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12,
          13, 14, 15, 16, 17, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 8, 7, 6, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1,
          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
          18, 21, 24, 28, 31, 35, 38, 42, 45, 49, 53, 56, 60, 64, 67, 71, 75, 78, 82, 86, 90, 94, 97, 101, 105, 109,
          113, 116, 120, 124]

currentStepA = None
currentStepB = None
currentStepC = None
sineArraySize
increment = 0
direct = True      # direction true=forward, false=backward


def setup():
    GPIO.setmode(GPIO.BCM)
    # Set pins as digital outputs
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)

    m1 = GPIO.PWM(IN1, 1000)        # Increase PWM frequency to 32 kHz  (make unaudible)
    m2 = GPIO.PWM(IN2, 1000)
    m3 = GPIO.PWM(IN3, 1000)

    GPIO.setup(EN1, GPIO.OUT)       # digitalWrite(EN1, HIGH)
    GPIO.setup(EN2, GPIO.OUT)
    GPIO.setup(EN3, GPIO.OUT)




    sineArraySize = len(pwmSin)         # Find lookup table size    sizeof(pwmSin)/sizeof(int);
    phaseShift = sineArraySize / 3      # Find phase shift and initial A, B C phase values
    currentStepA = 0
    currentStepB = currentStepA + phaseShift
    currentStepC = currentStepB + phaseShift

    sineArraySize -= 1                      # Convert from array Size to last PWM array number


def loop():
    GPIO.(IN1, pwmSin[currentStepA])
    analogWrite(IN2, pwmSin[currentStepB])
    analogWrite(IN3, pwmSin[currentStepC])

    if direct is True:
        increment = 1
    else:
        increment = -1

    currentStepA = currentStepA + increment
    currentStepB = currentStepB + increment
    currentStepC = currentStepC + increment

    ## Check for lookup table overflow and return to opposite end if necessary
    if currentStepA > sineArraySize:
        currentStepA = 0
    if currentStepA < 0:
        currentStepA = sineArraySize

    if currentStepB > sineArraySize:
        currentStepB = 0
    if currentStepB < 0:
        currentStepB = sineArraySize

    if currentStepC > sineArraySize:
        currentStepC = 0
    if currentStepC < 0:
        currentStepC = sineArraySize

    ## /// Control speed by this delay
    delay(10)

