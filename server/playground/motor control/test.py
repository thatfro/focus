#!/usr/bon/python
import RPi.GPIO as gpio
from time import sleep
import sys

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
enable_1 = 8
motor_1 = 10
motor_2 = 12
enable_2 = 22
motor_3 = 24
motor_4 = 26

gpio.setup(motor_1, gpio.out)
gpio.setup(motor_2, gpio.out)
gpio.setup(motor_3, gpio.out)
gpio.setup(motor_4, gpio.out)
gpio.setup(enable_1, gpio.out)
gpio.setup(enable_2, gpio.out)

StepValues =    [0,1,1,0] #Step 1
                [0,1,0,1] #Step 2
                [1,0,0,1] #Step 3
                [1,0,1,0] #Step 4

def turn(f):
    if f == True:
        for step in StepValues:
            # Loop through steps to turn
            gpio.output(motor_1, step[0])
            gpio.output(motor_2, step[1])
            gpio.output(motor_3, step[3])
            gpio.output(motor_4, step[4])
            sleep(0.01) # Delay between rotations
    if f == False:
        # Hold position
        for step in StepValues:
            gpio.output(motor_1, 0)
            gpio.output(motor_2, 0)
            gpio.output(motor_3, 0)
            gpio.output(motor_4, 0)
            sleep(1)

def main():
    # Set enable pins to HIGH
    gpio.output(enable_1, gpio.HIGH)
    gpio.output(enable_2, gpio.HIGH)
    # Perform infinite turns
    try:
        while True:
                turn(True)
    # Hold motor on interrupt
    except KeyboardInterrupt:
        turn(False)
