#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
from datetime import timedelta, datetime

class FlowMeter(object):

	def __init__(self, pin, ml_per_pulse=49, max_history_length=100, max_history_delta=timedelta(minutes=1)):
		self.pin = pin
		self.max_history_length = max_history_length
		self.max_history_delta = max_history_delta
		self.ml_per_pulse = ml_per_pulse
		self.pulse_history = []

		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(pin, GPIO.FALLING, callback=self._pulse, bouncetime=30)

	def _pulse(self, channel):
		print channel
		self.pulse_history.append(datetime.now())
		self._trim_history()

	def _trim_history(self):
		if len(self.pulse_history) > self.max_history_length:
			self.pulse_history = self.pulse_history[self.max_history_length:]

		while len(self.pulse_history) > 0:
			delta = datetime.now() - self.pulse_history[0]
			if delta < self.max_history_delta:
				break
			del self.pulse_history[0]

	def flow(self):
		self._trim_history()
		return self.ml_per_pulse * len(self.pulse_history)

if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	pins = [13, 19]
	flow_meters = [FlowMeter(pin) for pin in pins]
	while True:
		for fm in flow_meters:
			print "FlowMeter(%d) at %sml/min" % (fm.pin, fm.flow())
		sleep(3)

