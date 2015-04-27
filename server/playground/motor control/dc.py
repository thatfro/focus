import RPi.GPIO as GPIO
from time import sleep
import sys
import math


GPIO.setmode(GPIO.BOARD)
pin = 15
GPIO.setup(pin, GPIO.OUT)

while True:
    GPIO.output(pin, 1)
    sleep(.1)
    GPIO.output(pin, 0)
