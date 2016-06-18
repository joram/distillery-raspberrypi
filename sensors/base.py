
class BaseSensor(object):

  def __init__(self, name="basic sensor"):
    self.name = name

  @property
  def value(self):
    raise NotImplemented()

  @property
  def values(self):
    raise NotImplemented()


