class Month(object):

  def __init__(self, number):
    self.number = number
    self.days = {}

  def add_day(self, day):
    self.days[day.number] = day