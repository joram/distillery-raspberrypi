#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT
 
import time
import atexit
import RPi.GPIO as GPIO
import thread

class Stepper(object):

  MAX_TICKS = 100
  MAX_TICK_SIZE = 10
  TICK_TYPE = Adafruit_MotorHAT.INTERLEAVE

  def __init__(self, mhat,  motor_id=1):
    self.mhat = mhat
    self.motor_id = motor_id
    self._current_tick = 0
    self._desired_tick = 0
    self._stepper = self.mhat.getStepper(200, self.motor_id)
    atexit.register(self.turnOffMotors)
    thread.start_new_thread(self._tick_thread, tuple())

  def tick_to(self, target):
    self._desired_tick = target

  def _tick_thread(self):
    while True:
      if self._current_tick != self._desired_tick:
        self._tick()
      else:
        time.sleep(0.5)

  def _tick(self):
    print "at:%s, want:%s" % (self._current_tick, self._desired_tick)
    ticks = self._current_tick - self._desired_tick
    direction = ticks > 0
    ticks_remaining = abs(ticks)
    direction = Adafruit_MotorHAT.FORWARD if direction else Adafruit_MotorHAT.BACKWARD
    ticks = min(self.MAX_TICK_SIZE, ticks_remaining)
    self._stepper.step(ticks, direction, Adafruit_MotorHAT.INTERLEAVE)
    self._current_tick += ticks * (1 if direction else -1)

  def turnOffMotors(self):
    self.mhat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    self.mhat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    self.mhat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    self.mhat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

