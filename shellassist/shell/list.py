from shellassist.shell.exceptions import InvalidUserInputError
from shellassist.calendar.calendar import Calendar


class List(object):

  """ List command class
  """

  def __init__(self, shell, arg):
    self.shell = shell
    self.arg = arg

  def parse(self):
    pass

  def validate(self):
    pass

  def execute(self):
    try:
      # First parse arguments
      self.parse()

      # Then validate arguments
      self.validate()

      # Load activities of current day

      current_year_number = self.shell.current_date.year
      current_month_number = self.shell.current_date.month
      current_day_number = self.shell.current_date.day

      current_year = Calendar.load_year(current_year_number)
      current_month = current_year.get_month(current_month_number)
      current_day = current_month.get_day(current_day_number)

      for activity in current_day.activities:
        print activity.start_time + "|" + activity.end_time + "|" + activity.description

    except InvalidUserInputError as err:
      print err
    except:
      raise