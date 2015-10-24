from datetime import time


def get_time(hour=None, minute=None):
  if hour is not None and minute is not None:
    return time(hour, minute)
  # Not ideal, should handle all edge cases
  # Instead of blanket except here.
  # Maybe use the validation functions below here?


def time_string(time):
  """ Returns string formatted date
  param time<datetime.time>
  """
  hour = time.hour
  minute = time.minute
  formatted_string = str(hour) + ":"
  formatted_string += str(minute)
  return formatted_string


def validate_hour(raw_hour):
  try:
    hour = int(raw_hour)
    return hour >= 0 and hour <= 23
  except ValueError:
    return False


def validate_minute(raw_minute):
  try:
    minute = int(raw_minute)
    return minute >= 0 and minute <= 59
  except ValueError:
    return False
