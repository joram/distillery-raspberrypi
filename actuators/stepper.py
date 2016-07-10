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
    self._min_tick = None
    self._max_tick = None
    self._stop = False
    self._stepper = self.mhat.getStepper(200, self.motor_id)
    atexit.register(self.turnOffMotors)
    
    thread.start_new_thread(self._tick_thread, tuple())

  def tick_to(self, target):
    self._desired_tick = self._clamp_tick(target)

  def _clamp_tick(self, t):
    _old_t = t
    if self._max_tick is not None:
      t = min(self._max_tick, t)
    if self._min_tick is not None:
      t = max(self._min_tick, t)
    return t

  def stop(self):
    self._stop = True

  def start(self):
    self._stop = False

  def set_bounds(self, min_tick, max_tick):
    self._min_tick = min_tick
    self._max_tick = max_tick
    self._desired_tick = self._clamp_tick(self._desired_tick)

  def _tick_thread(self):
    while True:
      if self._stop:
        print "STEPPER IS HARD STOPPED"
        time.sleep(1)
      elif self._current_tick != self._desired_tick:
        self._tick()
        time.sleep(0)
      else:
        time.sleep(0.5)

  def _tick(self):
    ticks = self._desired_tick - self._current_tick
    ticks = min(self.MAX_TICK_SIZE, max(-self.MAX_TICK_SIZE, ticks))
    direction = Adafruit_MotorHAT.BACKWARD if ticks > 0 else Adafruit_MotorHAT.FORWARD  
    self._stepper.step(abs(ticks), direction, Adafruit_MotorHAT.INTERLEAVE)
    self._current_tick += ticks

  def turnOffMotors(self):
    self.mhat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    self.mhat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    self.mhat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    self.mhat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

