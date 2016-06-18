from actuators import Stepper
from sensors import FlowMeter
from Adafruit_MotorHAT import Adafruit_MotorHAT


class FlowValve(object):

  def __init__(self, hat_addr=0x60, flow_meter_pin=26):
    self.name = "Wash Input Valve"
    self.flow_meter = FlowMeter(flow_meter_pin)
    motor_hat = Adafruit_MotorHAT(addr=hat_addr)
    self.stepper = Stepper(motor_hat)

  @property
  def uid(self):
    return self.name.lower().replace(" ", "_")    

  @property
  def flow_rate(self):
    return 0

  @property
  def stepper_setting(self):
    return 1
