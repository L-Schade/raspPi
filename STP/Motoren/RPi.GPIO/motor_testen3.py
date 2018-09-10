def motor(mag): # Run Motor
    pulse = 1
    speed = int(mag * 3 + 20)  # Min 20 max 50
    duration = int(10 - mag)    # 2 sec to 20 sec
    sec = 0.1
    
    p = GPIO.PWM(MOTORPIN, 50)  # channel=MOTORPIN frequency=50Hz
    p.start(0)
    p.ChangeDutyCycle(speed)
    time.sleep(0.1)
    for dc in range(speed, 10, -(duration)):
         p.ChangeDutyCycle(dc)
         time.sleep(pulse)
         pulse = pulse + sec
    p.stop()
    return 
