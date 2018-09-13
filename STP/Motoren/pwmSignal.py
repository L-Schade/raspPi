import numpy as np
import matplotlib.pyplot as plt

percent = 30.0
TimePeriod = 1.0
Cycles = 10
dt = 0.01

t = np.arange(0,Cycles*TimePeriod,dt);
pwm = t%TimePeriod<TimePeriod*percent/100
m = plt.plot(t,pwm)
plt.show(m)