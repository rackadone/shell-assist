from shellassist.shell.exceptions import InvalidUserInputError
from shellassist.calendar.calendar import Calendar


class Remove(object):
    """ Remove command class
    Remove an activity of a certain day
    Usage (short hand): rm <# of activity to delete>
    Usage (standard): rm
    """

    def __init__(self, shell, arg):
        self.shell = shell
        self.arg = arg

    def parse(self):
        if self.arg:
            print("there is an argument")
        else:
            print("there is no argument")

    def validate(self):
        """ Don't validate yet.
        """
        pass

    def execute(self):
        try:
            if self.arg:
                self.execute_shorthand()
            else:
                self.execute_full()
        except InvalidUserInputError as err:
            print(err)
        except:
            raise

    def execute_shorthand(self):
        try:
            # Get number
            choice = int(self.arg)

            # Query events of current day
            current_year_number = self.shell.current_date.year
            current_month_number = self.shell.current_date.month
            current_day_number = self.shell.current_date.day

            current_year = Calendar.load_year(current_year_number)
            current_month = current_year.get_month(current_month_number)
            current_day = current_month.get_day(current_day_number)
            activities = current_day.activities

            if len(activities) <= 0:
                print("There are no activities this day")
                # End execution
            elif choice >= 1 and choice <= len(activities):
                if current_day.remove_activity(choice - 1):
                    Calendar.save_year(current_year)
                    print("You removed event # " + str(choice))
                else:
                    raise InvalidUserInputError("Invalid number")
            else:
                print("No activity # " + str(choice))
        except InvalidUserInputError as err:
            print(err)
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
            activities = current_day.activities

            if len(activities) <= 0:
                print("No activities on this day")
                # End execution
            else:
                print("Enter number of activity you would like to remove:")

                for i in range(0, len(activities)):
                    print(str(i + 1) + '. ' + activities[i].formatted_string())

                choice = input(">> ")

                while int(choice) < 1 or int(choice) > len(activities):
                    print("Invalid number, please re enter a number")
                    choice = input(">> ")

                if current_day.remove_activity(int(choice) - 1):
                    Calendar.save_year(current_year)
                    print("You removed event # " + str(choice))
                else:
                    raise InvalidUserInputError("Invalid number")

        except InvalidUserInputError as err:
            print(err)
        except:
            raise
