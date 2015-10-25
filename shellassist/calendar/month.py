from shellassist.calendar.day import Day


class Month(object):
    def __init__(self, number):
        self.number = number
        self.days = {}

    def add_day(self, day):
        self.days[day.number] = day

    def get_day(self, day_number):
        if day_number in self.days:
            return self.days[day_number]
        else:
            new_day = Day(day_number)
            self.add_day(new_day)
            return new_day
