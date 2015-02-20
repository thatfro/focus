#!/usr/bin/python
import RPi.GPIO as gpio
from time import sleep
import sys

blue = 12 #GPIO 18
pink = 16 #GPIO 23
yellow = 18 #GPIO 24
orange = 22 #GPIO 25

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(blue, gpio.OUT)
gpio.setup(pink, gpio.OUT)
gpio.setup(yellow, gpio.OUT)
gpio.setup(orange, gpio.OUT)

StepValues = [
    [1,1,0,0,0,0,0,1],
    [0,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,0,0],
    [0,0,0,0,0,1,1,1],
]

def turn():
    for step in StepValues:
        #print(step)
        gpio.output(blue, step[0])
        gpio.output(pink, step[1])
        gpio.output(yellow, step[2])
        gpio.output(orange, step[3])
        sleep(0.01)

while True:
    turn()
