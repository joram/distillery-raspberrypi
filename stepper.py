#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


#http://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg
class Stepper(object):

	def __init__(self, step_pin=29, dir_pin=31):
		GPIO.setup(step_pin, GPIO.OUT)
		GPIO.setup(dir_pin, GPIO.OUT)

		self.step_pin = step_pin
		self.dir_pin = dir_pin
		self.pwm = None
		self.frequency = 0
		self.direction = True

	def set_speed(self, frequency):
		self.frequency = frequency

		# stop
		if frequency == 0:
			if self.pwm:
				self.pwm.stop()
			return

		# start		
		if not self.pwm:
			self.pwm = GPIO.PWM(self.step_pin, frequency)
			self.pwm.start(50)
			return

		# change
		self.pwm.ChangeFrequency(frequency)

	def set_direction(self, direction):
		self.direction = direction
		GPIO.output(self.dir_pin, 1 if direction else 0)
