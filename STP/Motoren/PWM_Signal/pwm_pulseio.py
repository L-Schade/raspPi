import pulseio
import board
import time


pwm = pulseio.PWMOut(board.D13, frequency=50)
pwm.duty_cycle = 2 ** 15                  # Cycles the pin with 50% duty cycle (half of 2 ** 16) at 50hz

# variable frequency
pwm = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=440, variable_frequency=True)
time.sleep(0.2)
pwm.frequency = 880
time.sleep(0.1)


# pwm-Pin check
# import board
# import pulseio
#
# for pin_name in dir(board):
#     pin = getattr(board, pin_name)
#     try:
#         p = pulseio.PWMOut(pin)
#         p.deinit()
#         print("PWM on:", pin_name)  # Prints the valid, PWM-capable pins!
#     except ValueError:  # This is the error returned when the pin is invalid.
#         print("No PWM on:", pin_name)  # Prints the invalid pins.
#     except RuntimeError:  # Timer conflict error.
#         print("Timers in use:", pin_name)  # Prints the timer conflict pins.
#     except TypeError:  # Error returned when checking a non-pin object in dir(board).
#         pass  # Passes over non-pin objects in dir(board).
