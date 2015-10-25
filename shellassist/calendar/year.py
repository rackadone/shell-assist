from shellassist.calendar.month import Month


class Year(object):
    def __init__(self, number):
        self.number = number
        self.months = {}

    def add_month(self, month):
        self.months[month.number] = month

    def get_month(self, month_number):
        if month_number in self.months:
            return self.months[month_number]
        else:
            new_month = Month(month_number)
            self.add_month(new_month)
            return new_month
