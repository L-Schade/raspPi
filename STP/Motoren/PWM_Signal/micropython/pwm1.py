from machine import Timer

tim1 = Timer(1, mode=Timer.ONE_SHOT)                               # initialize it in one shot mode
tim2 = Timer(2, mode=Timer.PWM)                                    # initialize it in PWM mode
tim1_ch = tim1.channel(Timer.A, freq=10, polarity=Timer.POSITIVE)  # start the event counter with a frequency of 10Hz and triggered by positive edges
tim2_ch = tim2.channel(Timer.B, freq=10000, duty_cycle=5000)       # start the PWM on channel B with a 50% duty cycle
tim2_ch.freq(20)                                                   # set the frequency (can also get)
tim2_ch.duty_cycle(3010)                                           # set the duty cycle to 30.1% (can also get)
tim2_ch.duty_cycle(3020, Timer.NEGATIVE)                           # set the duty cycle to 30.2% and change the polarity to negative
tim2_ch.period(2000000)                                            # change the period to 2 seconds