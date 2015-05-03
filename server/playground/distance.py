import RPi.GPIO as GPIO	#import GPIO library
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.IN)

while True:
    print GPIO.input(18)
    sleep(1)
