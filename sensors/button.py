import RPi.GPIO as GPIO


class Button(object):

  def __init__(self, pin, callback_func=None):
    self.pin = pin
    GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self._state_change_callback)  
    self.change_callback = callback_func

  def _state_change_callback(self, channel):
    print "Button(%s) changed to %s" % (self.pin, self.pressed)
    if self.change_callback != None:
      self.change_callback(self)

  @property
  def pressed(self):
    return GPIO.input(self.pin) == 1


if __name__ == "__main__":
  GPIO.setmode(GPIO.BOARD)
  import time
  b = Button(22)
  while True:
    O.add_event_detecttime.sleep(5)
