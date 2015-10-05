""" Calendar class

Class used to manage persistent data
Relies on pickle to serialize data.

"""

import os
import errno
import pickle
from shellassist.calendar.year import Year
from shellassist.calendar.month import Month
from shellassist.calendar.day import Day

class Calendar(object):

  @staticmethod
  def load_year(year_number):
    """ Returns year object
    param year<int>: number used to identify
    year to return
    """
    file_path = 'saves/' + str(year_number) + '.p'
    if os.path.isfile(file_path):
      year = pickle.load(open(file_path, 'rb'))
    else:
      year = Year(year_number)
      Calendar.create_folder_if_not_exists('saves')
      pickle.dump(year, open(file_path, 'wb'))
    return year

  @staticmethod
  def save_year(year):
    """ Save year object
    param year<int>: number used to identify
    year to return
    """
    file_path = 'saves/' + str(year.number) + '.p'
    Calendar.create_folder_if_not_exists("saves")
    pickle.dump(year, open('saves/' + str(year.number) + '.p', 'wb'))

  @staticmethod
  def create_folder_if_not_exists(path):
    try:
      os.makedirs('saves')
    except OSError as exception:
      if exception.errno != errno.EEXIST:
        raise
