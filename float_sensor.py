import RPi.GPIO as GPIO
import time


class FloatSensor(object):

  def __init__(self, pin=21):
    self.pin = pin
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  @property
  def floating(self):
    return GPIO.input(self.pin)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    float_sensor = FloatSensor(21)
    while True:
        print 'Floating' if float_sensor.floating else "Not floating"
        time.sleep(0.2)
