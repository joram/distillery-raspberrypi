#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(21, GPIO.OUT)
while True:
	GPIO.output(21, GPIO.HIGH)
	sleep(5)
	GPIO.output(21, GPIO.LOW)
	sleep(5)
