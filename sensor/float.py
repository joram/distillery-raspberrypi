import RPi.GPIO as GPIO
import time
import thread
from base import BaseSensor

class FloatSensor(BaseSensor):

  def __init__(self, name="float sensor", callback_func=None, poll_sleep=0.5, pin=21):
    super(FloatSensor, self).__init__(name, callback_func, poll_sleep)
    self.pin = pin
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    self._value = GPIO.input(self.pin)
    thread.start_new_thread (self._poll, ())

  def _poll(self):
    while True:
      new_value = GPIO.input(self.pin)
      if self.callback_func and new_value != self._value:
        self._value = new_value
        self.callback_func(self)
      time.sleep(self.poll_sleep)

  @property
  def value(self):
    return self._value

  @property
  def values(self):
    return [self._value]


if __name__ == "__main__":
  
  GPIO.setmode(GPIO.BCM)  

  def example_func(sensor):
    print "%s is now: %s" % (sensor.name, sensor.value)

  sensor = FloatSensor("mr.Floaty", example_func, pin=21)

  while True:
    time.sleep(1)
