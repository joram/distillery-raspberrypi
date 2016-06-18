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

    thread.start_new_thread(self._poll_temps, ())

  def _poll_temps(self):
    time.sleep(self.poll_sleep)
    while True:
      self.read_values()
      time.sleep(self.poll_sleep)


  def read_values(self):
    # read raw values from arduino
    self.serial.write("values".encode())
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
      print e

    
  def register(self, sensor):
    self.sensors[sensor.name] = sensor

global TEMP_CONTROLLER
TEMP_CONTROLLER = TemperatureSensorController()

class TemperatureSensor(BaseSensor):

  def __init__(self, name="A0", max_values=10, calib=[(0,0), (1,1)]):
    super(TemperatureSensor, self).__init__(name)
    self._values = []
    self.max_values = max_values

    # break the datapoints apart into its base parts
    [(x1, y1), (x2, y2)] = calib
    rise = y2-y1
    run = x2-x1
    self.slope = rise/run
    self.y_intercept = y1 - self.slope*x1
    global TEMP_CONTROLLER
    TEMP_CONTROLLER.register(self)  

  def celcius(self, val):
    return self.slope*val + self.y_intercept

  def add_value(self, v):
    if v > 0 and v < 1023:
      c = self.celcius(v)
      self._values.append(c)
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
