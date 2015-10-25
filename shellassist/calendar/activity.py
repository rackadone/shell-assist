from shellassist.calendar import time_functions


class Activity(object):
    def __init__(self, start_time, end_time, description):
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def formatted_string(self):
        str_start_time = time_functions.time_string(self.start_time)
        str_end_time = time_functions.time_string(self.end_time)
        formatted_string = str_start_time + " ~ "
        formatted_string += str_end_time + " : "
        formatted_string += self.description
        return formatted_string
