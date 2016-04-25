#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

class Pump(object):

	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)

	def on(self):
		GPIO.output(self.pin, GPIO.LOW)

	def off(self):
		GPIO.output(self.pin, GPIO.HIGH)

if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	pins = [16, 20]
	pump = Pump(16)
	while True:
		pump.on()
		sleep(5)
		pump.off()
		sleep(5)
