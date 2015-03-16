#!/usr/bon/python
import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
enable_1 = 8 #GPIO 14
motor_1 = 10 #GPIO 15
motor_2 = 12 #GPIO 18
enable_2 = 22 #GPIO 25
motor_3 = 24 #GPIO 8
motor_4 = 26 #GPIO 7

GPIO.setup(motor_1, GPIO.OUT)
GPIO.setup(motor_2, GPIO.OUT)
GPIO.setup(motor_3, GPIO.OUT)
GPIO.setup(motor_4, GPIO.OUT)
GPIO.setup(enable_1, GPIO.OUT)
GPIO.setup(enable_2, GPIO.OUT)

StepValues =   [[0,1,1,0], #Step 1
                [0,1,0,1], #Step 2
                [1,0,0,1], #Step 3
                [1,0,1,0]] #Step 4

def turn(f):
    if f == True:
        for step in StepValues:
            # Loop through steps to turn
            GPIO.output(motor_1, step[0])
            GPIO.output(motor_2, step[1])
            GPIO.output(motor_3, step[2])
            GPIO.output(motor_4, step[3])
            sleep(0.01) # Delay between rotations
    if f == False:
        # Hold position
        for step in StepValues:
            GPIO.output(motor_1, 0)
            GPIO.output(motor_2, 0)
            GPIO.output(motor_3, 0)
            GPIO.output(motor_4, 0)
            sleep(1)

def main():
    print "Running!"
    # Set enable pins to HIGH
    GPIO.output(enable_1, GPIO.HIGH)
    GPIO.output(enable_2, GPIO.HIGH)
    # Perform infinite turns
    while True:
        turn(True)
