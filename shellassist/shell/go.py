from shellassist.calendar import date_functions
from shellassist.shell.exceptions import InvalidUserInputError

class Go(object):

  """ Go command class
  Purpose is to change context to a certain day.
  go <date>
  """

  def __init__(self, shell, arg):
    self.shell = shell
    self.arg = arg

  def parse(self):
    split_arg = self.arg.split()
    
    if len(split_arg) == 0:
      raise InvalidUserInputError("ERROR: No arguments received")

    if len(split_arg) > 1:
      raise InvalidUserInputError("ERROR: More than one argument received")

    # Check if user entered date is in correct format
    date_string = split_arg[0]
    split_date_string = date_string.split('/')

    if len(split_date_string) != 3:
      raise InvalidUserInputError("ERROR: Invalid date argument")
  
    # save parsed argument
    self.raw_day = split_date_string[1]
    self.raw_month = split_date_string[0]
    self.raw_year = split_date_string[2]

  def validate(self):
    """ Validate user arguments
    raise exceptions when user arguments
    are invalid
    """
    if not date_functions.validate_day(self.raw_day):
      raise InvalidUserInputError("ERROR: Invalid day: " + self.raw_day)
    if not date_functions.validate_month(self.raw_month):
      raise InvalidUserInputError("ERROR: Invalid month: " + self.raw_month)
    if not date_functions.validate_year(self.raw_year):
      raise InvalidUserInputError("ERROR: Invalid year: " + self.raw_year)

  def execute(self):
    try:
      # First parse arguments
      self.parse()
    
      # Then validate arguments
      self.validate()

      # Then Execute command
      day = int(self.raw_day)
      month = int(self.raw_month)
      year = int(self.raw_year)

      self.shell.current_date = date_functions.get_date(day=day,month=month,year=year)

    except InvalidUserInputError as err:
      print err
    except:
      raise

    

    
