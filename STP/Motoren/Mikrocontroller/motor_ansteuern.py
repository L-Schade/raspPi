import RPi.GPIO as GPIO
import time

global ind
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_pin = 4 # gelb
coil_B_pin = 23 # gruen
coil_C_pin = 24 # blau
 
# Sequenz
ind = 0
##StepCount = 6
Seq = list(range(0, 6))
Seq[0] = [1,1,0]
Seq[1] = [1,0,0]
Seq[2] = [1,0,1]
Seq[3] = [0,0,1]
Seq[4] = [0,1,1]
Seq[5] = [0,1,0]
Seq[5] = [0,1,0]

 
1#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_pin, GPIO.OUT)
GPIO.setup(coil_B_pin, GPIO.OUT)
GPIO.setup(coil_C_pin, GPIO.OUT)
 
#GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3):
    GPIO.output(coil_A_pin, w1)
    GPIO.output(coil_B_pin, w2)
    GPIO.output(coil_C_pin, w3)

 
def forward(delay, steps):
    global ind
    for i in range(0, steps, 1):
            setStep(Seq[ind][0], Seq[ind][1], Seq[ind][2])
            time.sleep(delay)
            print(ind)
            ind += 1
            ind = ind % 6
##            print(ind)

 
def backwards(delay, steps):
    global ind
    for i in range(0, steps, 1):
            setStep(Seq[ind][0], Seq[ind][1], Seq[ind][2])
            time.sleep(delay)
            print(ind)
            ind -= 1
            ind = ind % 6
            print(ind)


def reference_point():
    # TODO
    # Warnung das nichts im Weg steht 
    GPIO.cleanup() 				# move to reference point


def move(x_angle, y_angle, delay):
    if x_angle > 0:
        forward((float(delay) / 1000.0), int(steps))
    else:
        backwards((float(delay) / 1000.0), int(steps))
    if y_angle > 0:
        forward((float(delay) / 1000.0), int(steps))
    else:
        backwards((float(delay) / 1000.0), int(steps))

              
if __name__ == '__main__':
    try:
        delay = raw_input("Zeitverzoegerung (ms)?")
        while True:
            ##        delay = raw_input("Zeitverzoegerung (ms)?")
            steps = raw_input("Wie viele Schritte vorwaerts? ")
            forward((float(delay) / 1000.0),int(steps))
            steps = raw_input("Wie viele Schritte rueckwaerts? ")
            backwards((float(delay) / 1000.0), int(steps))
    except KeyboardInterrupt:
        GPIO.cleanup()
