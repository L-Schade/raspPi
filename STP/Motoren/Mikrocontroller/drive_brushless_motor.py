import RPi.GPIO as GPIO

levels[48] = [127, 144, 160, 176, 191, 205, 217, 228, 237, 245, 250, 253, 255, 253, 250, 245, 237, 228, 217, 205, 191, 176, 160, 144, 127, 110, 94, 78, 63, 49, 37, 26, 17, 9, 4, 1, 0, 1, 4, 9, 17, 26, 37, 49, 63, 78, 94, 110]

# These are the pins used to drive the motor.
pinA = 4
pinB = 23
pinC = 24

step = 0            # Keeps track of what pulse width to use
lastTime = 0		# the time in micros since last step
period = 5000    	# set motor speed by defining time between steps

def setup():
  	# Set pins as digital outputs
  	GPIO.setup(pinA, GPIO.OUT)
	GPIO.setup(pinB, GPIO.OUT)
	GPIO.setup(pinC, GPIO.OUT)

  	# Set all the pins LOW
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.LOW)
    GPIO.output(pinC, GPIO.LOW)

def loop():
    # Check if it is time for the next step
    if lastTime >= period:        # if (micros() - lastTime) >= period:
        # Next three lines send pulse width value for this step.
        GPIO.output(pinA, levels[step])
        GPIO.output(pinB, levels[(step + 16) % 48])
        GPIO.output(pinC, levels[(step + 32) % 48])

    # Add one to set (% 48 rolls step back to 0 after it fits 47)
    step = (step + 1) / 48

    # make note of current time
    lastTime +=2;

    # ramps up the speed
    if period > 500:
        period -= 1 # make speed faster (the period between steps smalled)
