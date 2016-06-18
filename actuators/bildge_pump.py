from sensors import FloatSensor
from actuators import Pump

def float_change(sensor):
  print "flaot changed"

class BildgePump(object):

  def __init__(self, name="", float_pin=21, pump_pin=16, min_duration=1, on_when_floating=True):
    self.name = name
    self.float_pin = float_pin
    self.pump_pin = pump_pin
    self.min_duration = min_duration
    self.on_when_floating = on_when_floating
    self.float_sensor = FloatSensor(name="{name} Sensor".format(name=name), pin=float_pin, callback_func=self.float_change)
    self.pump = Pump(self.pump_pin)
    self.float_change(self.float_sensor)

  @property
  def uid(self):
    return self.name.lower().replace(" ", "_")

  def float_change(self, sensor):
    if self.float_state == self.on_when_floating:
      self.pump.on()
    else:
      self.pump.off()

  @property
  def float_state(self):
    return self.float_sensor.value == 0

  @property
  def pump_state(self):
    return self.pump.state
