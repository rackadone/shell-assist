from shellassist.shell.exceptions import InvalidUserInputError
from shellassist.calendar.activity import Activity
from shellassist.calendar.calendar import Calendar
from shellassist.calendar import time_functions


class Add(object):

  """ Add command class
  Usage (short hand): add <start time> <end time> <event>
  Usage (standard): add
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
    # try:
    #   start_time = time_functions.parse_time(self.start_time)
    #   end_time = time_functions.parse_time(self.end_time)
    # except ValueError as err:
    #   print err
    pass

  def execute(self):
    try:
      if self.arg:
        self.execute_shorthand()
      else:
        self.execute_full()
    except InvalidUserInputError as err:
      print err
    except:
      raise

  def execute_shorthand(self):
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

      Calendar.save_year(current_year)
      print "Activity successfuly added."

    except InvalidUserInputError as err:
      print err
    except:
      raise

  def execute_full(self):
    try:
      # Query events of current day
      current_year_number = self.shell.current_date.year
      current_month_number = self.shell.current_date.month
      current_day_number = self.shell.current_date.day

      current_year = Calendar.load_year(current_year_number)
      current_month = current_year.get_month(current_month_number)
      current_day = current_month.get_day(current_day_number)

      start_time = raw_input("Enter start time: ")
      end_time = raw_input("Enter end time: ")
      description = raw_input("Enter activity description: ")

      new_activity = Activity(
          start_time,
          end_time,
          description)

      current_day.add_activity(new_activity)
      Calendar.save_year(current_year)
      print "Activity successfuly added."

    except InvalidUserInputError as err:
      print err
    except:
      raise
