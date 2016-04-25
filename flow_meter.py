#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count_13 = 0
count_19 = 0
def my_callback_19(channel):  
	global count_19
	count_19 += 1
	print "pin_19:%d, pin_13:%d" % (count_19, count_13)

def my_callback_13(channel):  
	global count_13
	count_13 += 1
	print "pin_19:%d, pin_13:%d" % (count_19, count_13)

GPIO.add_event_detect(19, GPIO.FALLING, callback=my_callback_19, bouncetime=300)
GPIO.add_event_detect(13, GPIO.FALLING, callback=my_callback_13, bouncetime=300)

# Set relay pins as output
while True:
	sleep(10)

