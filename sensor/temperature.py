import RPi.GPIO as GPIO
import time
import thread
import serial
import json
from base import BaseSensor



class TemperatureSensorController(object):

  def __init__(self, poll_sleep=2):
    self.serial = serial.Serial('/dev/ttyACM0', 9600)
    self.poll_sleep = poll_sleep
    self.sensors = {}
    thread.start_new_thread (self._poll, ())

  def _poll(self):
    while True:
 
      # read raw values from arduino
      data = self.serial.readline().rstrip("\n")
      try:
        data = json.loads(data)

        # hand off values to sensors
        for name in data.keys():
          sensor = self.sensors.get(name)
          if sensor:
            v = data[name]
            if type(v) == int:
              sensor.add_value(v)
            if type(v) == list:
              for val in v:
                sensor.add_value(val)
      
      except Exception as e:
        pass

      time.sleep(self.poll_sleep)
    
  def register(self, sensor):
    self.sensors[sensor.name] = sensor


class TemperatureSensor(BaseSensor):

  def __init__(self, controller, name="A0", max_values=10):
    super(TemperatureSensor, self).__init__(name, None, None)
    self._values = []
    self.max_values = max_values
    controller.register(self)

  def add_value(self, v):
    self._values.append(v)
    if len(self._values) > self.max_values:
      self._values.pop(0)

  @property
  def value(self):
    if len(self._values) > 0:
     return self._values[-1]
    return None

  @property
  def values(self):
    return self._values


if __name__ == "__main__":
  controller = TemperatureSensorController()
  A0 = TemperatureSensor(controller, "A0")
  A1 = TemperatureSensor(controller, "A1")
  while True:
    print "A0: %s" % A0.values
    print "A1: %s" % A1.values
    time.sleep(1)
