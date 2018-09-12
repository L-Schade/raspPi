import RPi.GPIO as GPIO
# import time

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style


pin_in = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_in, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)	# Pull-Down-Widerstand

ind = 0

while True:
    print("GPIO:")
    print(GPIO.input(pin_in))
    ind += 1
    if ind == 50:
        exit()

# style.use('fivethirtyeight')
#
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
#
#
# def animate(i):
#     graph_data = open('example.txt','r').read()
#     lines = graph_data.split('\n')
#     xs = []
#     ys = []
#     for line in lines:
#         if len(line) > 1:
#             x, y = line.split(',')
#             xs.append(x)
#             ys.append(y)
#     ax1.clear()
#     ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
