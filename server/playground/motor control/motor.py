#!/usr/bin/python
import RPi.GPIO as gpio
from time import sleep
import sys

pin1 = 12 #GPIO 18
pin2 = 16 #GPIO 23
pin3 = 18 #GPIO 24
pin4 = 22 #GPIO 25

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)
gpio.setup(pin3, gpio.OUT)
gpio.setup(pin4, gpio.OUT)

case = 1

def turn():
    global case
    if case == 1:
        gpio.output(pin1, gpio.LOW)
        gpio.output(pin2, gpio.LOW)
        gpio.output(pin3, gpio.LOW)
        gpio.output(pin4, gpio.HIGH)
    if case == 2:
        gpio.output(pin1, gpio.LOW)
        gpio.output(pin2, gpio.LOW)
        gpio.output(pin3, gpio.HIGH)
        gpio.output(pin4, gpio.HIGH)
    if case == 3:
        gpio.output(pin1, gpio.LOW)
        gpio.output(pin2, gpio.LOW)
        gpio.output(pin3, gpio.HIGH)
        gpio.output(pin4, gpio.LOW)
    if case == 4:
        gpio.output(pin1, gpio.LOW)
        gpio.output(pin2, gpio.HIGH)
        gpio.output(pin3, gpio.LOW)
        gpio.output(pin4, gpio.LOW)
    if case == 5:
        gpio.output(pin1, gpio.HIGH)
        gpio.output(pin2, gpio.HIGH)
        gpio.output(pin3, gpio.LOW)
        gpio.output(pin4, gpio.LOW)
    if case == 6:
        gpio.output(pin1, gpio.HIGH)
        gpio.output(pin2, gpio.LOW)
        gpio.output(pin3, gpio.LOW)
        gpio.output(pin4, gpio.LOW)
    if case == 7:
        gpio.output(pin1, gpio.HIGH)
        gpio.output(pin2, gpio.LOW)
        gpio.output(pin3, gpio.LOW)
        gpio.output(pin4, gpio.HIGH)
    else:
        gpio.output(pin1, gpio.LOW)
        gpio.output(pin2, gpio.LOW)
        gpio.output(pin3, gpio.LOW)
        gpio.output(pin4, gpio.LOW)
#    print case
    case = case + 1
    if case>7:
        case = 1
#        print 'LOG: One turn'
    sleep(0.01)

while True:
    turn()
