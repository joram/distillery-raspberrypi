import RPi.GPIO as GPIO
import time
from base import BaseSensor

global FLOAT_SENSORS
FLOAT_SENSORS = []

def global_callback(channel):
  global FLOAT_SENSORS
  for sensor in FLOAT_SENSORS:
    if sensor.pin == channel:
      sensor.changed()

class FloatSensor(BaseSensor):

  def __init__(self, name="float sensor", callback_func=None, pin=21):
    super(FloatSensor, self).__init__(name)
    self.pin = pin
    self.callbacks = []
    self.add_callback(callback_func)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=global_callback, bouncetime=300) 
    global FLOAT_SENSORS
    FLOAT_SENSORS.append(self)

  def add_callback(self, func):
    self.callbacks.append(func)

  def changed(self):
    for func in self.callbacks:
      func(self)

  @property
  def value(self):
    a = GPIO.input(self.pin)
    time.sleep(0.1)
    b = GPIO.input(self.pin)
    time.sleep(0.1)
    c = GPIO.input(self.pin)
    if a == b == c:
      return a
    return self.value

  @property
  def values(self):
    return [self.value]

if __name__ == "__main__":
  GPIO.setmode(GPIO.BOARD)
  b = FloatSensor(pin=22)
  while True:
    time.sleep(0.5)
    print b.value
