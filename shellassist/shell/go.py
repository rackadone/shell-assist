from shellassist.shell.exceptions import InvalidUserInputError
from datetime import date
from datetime import timedelta
import re


class Go(object):
    """ Go command class
    Purpose is to change context to a certain day.
    Usage: go <date>
    """

    def __init__(self, shell, arg):
        self.shell = shell
        self.arg = arg

    def parse(self):
        try:
            standard_format = re.compile(r"""
                (^\d\d/\d\d/\d\d\d\d$)|
                (^\d\d/\d/\d\d\d\d$)|
                (^\d/\d\d/\d\d\d\d$)|
                (^\d/\d/\d\d\d\d$)""", re.VERBOSE)

            relative_format = re.compile(r"""
                (^\+\d)|(^\-\d)""", re.VERBOSE)

            if standard_format.match(self.arg):
                split_arg = self.arg.split('/')
                month = int(split_arg[0])
                day = int(split_arg[1])
                year = int(split_arg[2])
                return date(year, month, day)
            elif relative_format.match(self.arg):
                op = self.arg[0]
                day_count = int(self.arg[1:])
                if op == '+':
                    return self.shell.current_date + timedelta(day_count)
                else:
                    return self.shell.current_date - timedelta(day_count)
            else:
                raise InvalidUserInputError('Invalid time input')
        except ValueError:
            raise

    def execute(self):
        try:
            # First parse arguments
            self.shell.current_date = self.parse()
        except InvalidUserInputError as err:
            print(err)
        except:
            raise
