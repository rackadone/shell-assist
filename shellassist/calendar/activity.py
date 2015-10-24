class Activity(object):
  def __init__(self, start_time, end_time, description):
    self.start_time = start_time
    self.end_time = end_time
    self.description = description

  def formatted_string(self):
    formatted_string = self.start_time + "|"
    formatted_string += self.end_time + "|"
    formatted_string += self.description
    return formatted_string