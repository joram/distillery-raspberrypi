#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

class Pump(object):

  def __init__(self, pin):
    self.pin = pin
    GPIO.setup(self.pin, GPIO.OUT)
    self._state = False
    self.off()

  def on(self):
    self._state = True
    GPIO.output(self.pin, GPIO.LOW)

  def off(self):
    self._state = False
    GPIO.output(self.pin, GPIO.HIGH)

  @property
  def state(self):
    return self._state

