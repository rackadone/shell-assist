from shellassist.shell.exceptions import InvalidUserInputError
from shellassist.calendar.activity import Activity
from shellassist.calendar.calendar import Calendar


class Add(object):

  """ Add command class
  Add an activity to a certain day
  add <start time> <end time> <event>
  """

  def __init__(self, shell, arg):
    self.shell = shell
    self.arg = arg

  def parse(self):
    split_arg = self.arg.split()
    if len(split_arg) < 3:
      raise InvalidUserInputError("ERROR: add requires three arguments")
    else:
      self.start_time = split_arg[0]
      self.end_time = split_arg[1]
      self.activity_descr = " ".join(split_arg[2:])

  def validate(self):
    pass

  def execute(self):
    try:
      # First parse arguments
      self.parse()

      # Then validate arguments
      self.validate()

      # Create & Save activity

      new_activity = Activity(
          self.start_time,
          self.end_time,
          self.activity_descr)

      current_year_number = self.shell.current_date.year
      current_month_number = self.shell.current_date.month
      current_day_number = self.shell.current_date.day

      current_year = Calendar.load_year(current_year_number)
      current_month = current_year.get_month(current_month_number)
      current_day = current_month.get_day(current_day_number)
      current_day.add_activity(new_activity)

      print "Activity successfuly added."

    except InvalidUserInputError as err:
      print err
    except:
      raise
