class Year(object):

  def __init__(self, number):
    self.number = number
    self.months = {}

  def add_month(self, month):
    self.months[month.number] = month