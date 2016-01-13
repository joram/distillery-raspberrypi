
class BaseSensor(object):

  def __init__(self, name="basic sensor", callback_func=None, poll_sleep=0.5):
    self.name = name
    self.callback_func = callback_func
    self.poll_sleep = poll_sleep

  @property
  def value(self):
    raise NotImplemented()

  @property
  def values(self):
    raise NotImplemented()


