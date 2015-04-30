import RPi.GPIO as GPIO	#import GPIO library
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN)

while True:
    print GPIO.input(23)
    sleep(1)
