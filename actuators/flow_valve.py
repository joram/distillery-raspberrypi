from actuators import Stepper
from sensors import FlowMeter, Button
from Adafruit_MotorHAT import Adafruit_MotorHAT
import time

class FlowValve(object):

  def __init__(self, hat_addr=0x60, flow_meter_pin=26, calibration_button_pin=22, tick_range=500):
    self.name = "Wash Input Valve"
    self._tick_range = tick_range
    self.flow_meter = FlowMeter(flow_meter_pin)
    self.calibration_button = Button(calibration_button_pin, self.max_range_callback)
    motor_hat = Adafruit_MotorHAT(addr=hat_addr)
    self.stepper = Stepper(motor_hat)
    self._has_calib = False

  @property
  def uid(self):
    return self.name.lower().replace(" ", "_")    

  @property
  def flow_rate(self):
    return 0

  def tick_to(self, tick):
    self.stepper.tick_to(tick)

  def calibrate(self):
    to = 0
    while not self._has_calib:
      self.tick_to(to)
      while self.stepper._current_tick > to and not self._has_calib:
        time.sleep(0.5)
      to -= 5000

    print "calibrated"
    self.stepper.tick_to(self._tick_range)

  def max_range_callback(self, button):
    if self._has_calib:
      return
    self._has_calib = True

    self.stepper.stop()
    self.stepper._current_tick = 0
    self.stepper.set_bounds(0, self._tick_range)
    time.sleep(0.1)
    self.stepper.start()

  @property
  def stepper_setting(self):
    return 1

