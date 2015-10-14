from datetime import date
from datetime import MINYEAR
from datetime import MAXYEAR

def get_today_date():
  """ Return date object of today
  """
  return date.today()

def get_date(day=None, month=None, year=None):
  if day is not None and month is not None and year is not None:
    return date(year, month, day)
  # Not ideal, should handle all edge cases
  # Instead of blanket except here.

def date_string(date):
  """ Returns string formatted date
  param date<datetime.date>
  """
  day = date.day
  month = date.month
  year = date.year
  formatted_string = str(month) + "/" 
  formatted_string += str(day) + "/"
  formatted_string += str(year)
  return formatted_string

def validate_day(raw_day):
  try:
    day = int(raw_day)
    return day >= 1 and day <= 31
  except ValueError:
    return False

def validate_month(raw_month):
  try:
    month = int(raw_month)
    return month >= 1 and month <= 12
  except ValueError:
    return False

def validate_year(raw_year):
  try:
    year = int(raw_year)
    return year >= MINYEAR and year <= MAXYEAR
  except ValueError:
    return False
