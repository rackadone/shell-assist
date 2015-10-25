class Day(object):
    def __init__(self, number):
        self.number = number
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def remove_activity(self, n):
        """ Removes activity from activity list
        param n<int>: Nth activity in list to remove

        Returns true if removal was successful, false
        if otherwise.
        """
        if n < 0:
            return False

        max_index = self.activity_count() - 1
        if n > max_index:
            return False
        else:
            del self.activities[n]
            return True

    def activity_count(self):
        return len(self.activities)
