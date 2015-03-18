#!/usr/bon/python
from __future__ import division
import RPi.GPIO as GPIO
from time import sleep
import sys
import math

x = 0 #delay time
acc = 0 #fake bool [1/-1]

delaymax = 0.1      #
delaymin = 0.001    # standard values for motor
motorsteps = 20     #

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

def turn(d):
    global x
    if d == True:
        for step in StepValues:
            # Loop through steps to turn
            GPIO.output(motor_1, step[0])
            # print "#15"
            GPIO.output(motor_2, step[1])
            # print "#18"
            GPIO.output(motor_3, step[2])
            # print "#8"
            GPIO.output(motor_4, step[3])
            # print "#7"
            sleep(x) # Delay between rotations


    if d == False:
        # Hold position
        for step in StepValues:
            GPIO.output(motor_1, 0)
            GPIO.output(motor_2, 0)
            GPIO.output(motor_3, 0)
            GPIO.output(motor_4, 0)
            sleep(1)

def accelerate(i,s):
    global x
    global delaymax
    global delaymin
    global motorsteps

    if i == "inc":
        acc = 1
    if i == "dec":
        acc = -1

    x = ((delaymax-delaymin)/2)*math.sin(((1/motorsteps)*math.pi*s)+(0.5*math.pi*acc))+((delaymax-delaymin)/2)+delaymin
    print x
    print s

def main():
    global delaymax
    global delaymin
    global motorsteps

    # For variable input
    """
    dmax = raw_input("Maximales Delay: ")
    delaymax = float(dmax)
    dmin = raw_input("Maximales Delay: ")
    delaymin = float(dmin)
    stp = raw_input("Anzahl steps bis minimum: ")
    motorsteps = int(stp)
    """

    print "Transporting"
    # Set enable pins to HIGH
    GPIO.output(enable_1, GPIO.HIGH)
    GPIO.output(enable_2, GPIO.HIGH)

    #perform one ransport
    for i in range(0,motorsteps+1):
        accelerate("inc",i)
        turn(True)
    for i in range(0,100+1):
        turn(True)
    for i in range(0,motorsteps+1):
        accelerate("dec",i)
        turn(True)
    turn(False)
    print "Finished"

    GPIO.output(enable_1, GPIO.LOW)
    GPIO.output(enable_2, GPIO.LOW)

while True:
    main()
