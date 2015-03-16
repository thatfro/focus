#!/usr/bon/python
import RPi.GPIO as gpio
from time import sleep
import sys

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
enable_1 = 8 #GPIO 14
motor_1 = 10 #GPIO 15
motor_2 = 12 #GPIO 18
enable_2 = 22 #GPIO 25
motor_3 = 24 #GPIO 8
motor_4 = 26 #GPIO 7

gpio.setup(motor_1, gpio.OUT)
gpio.setup(motor_2, gpio.OUT)
gpio.setup(motor_3, gpio.OUT)
gpio.setup(motor_4, gpio.OUT)
gpio.setup(enable_1, gpio.OUT)
gpio.setup(enable_2, gpio.OUT)

StepValues =   [[0,1,1,0], #Step 1
                [0,1,0,1], #Step 2
                [1,0,0,1], #Step 3
                [1,0,1,0]] #Step 4

def turn(f):
    if f == True:
        for step in StepValues:
            # Loop through steps to turn
            gpio.output(motor_1, step[0])
            gpio.output(motor_2, step[1])
            gpio.output(motor_3, step[2])
            gpio.output(motor_4, step[3])
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
    while True:
        print "Running!"
        turn(True)

    
