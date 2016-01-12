#!/usr/bin/python
import RPi.GPIO as GPIO
import time


class Sensor(object):
  
  def __init__(self, pin_a=18, pin_b=23, max_history=10):
    self.pin_a = pin_a
    self.pin_b = pin_b
    self.max_history = max_history
    self.history = []

  def discharge(self):
    GPIO.setup(self.pin_a, GPIO.IN)
    GPIO.setup(self.pin_b, GPIO.OUT)
    GPIO.output(self.pin_b, False)
    time.sleep(0.005)

  def charge_time(self):
    GPIO.setup(self.pin_b, GPIO.IN)
    GPIO.setup(self.pin_a, GPIO.OUT)
    count = 0
    GPIO.output(self.pin_a, True)
    while not GPIO.input(self.pin_b):
      count += 1
    return count

  def analog_read(self):
    self.discharge()
    ct = self.charge_time()
    self.history.append(ct)
    if len(history) > self.max_history:
      self.history.pop(0)
    return ct

if __name__ == "__main__":
  while True:
    GPIO.setmode(GPIO.BCM)
    print("hi")
    print("sensor value: %s" % s1.analog_read())
    time.sleep(1)
