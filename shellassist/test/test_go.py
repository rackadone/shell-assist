import unittest
from datetime import date
from shellassist.application import ShellAssistCmd
from shellassist.shell.go import Go
# from datetime import time
# from shellassist.calendar import time_functions


class ParseArgTestCase(unittest.TestCase):
    def test_validDateArg1_validTime(self):
        shell = ShellAssistCmd()
        target_date = date(2015, 10, 25)
        go = Go(shell, '10/25/2015')
        parsed_time = go.parse()
        self.assertEqual(parsed_time, target_date)

    def test_validDateArg2_validTime(self):
        shell = ShellAssistCmd()
        target_date = date(2015, 5, 25)
        go = Go(shell, '5/25/2015')
        parsed_time = go.parse()
        self.assertEqual(parsed_time, target_date)

    def test_validDateArg3_validTime(self):
        shell = ShellAssistCmd()
        shell.current_date = date(2015, 5, 25)
        target_date = date(2015, 5, 28)
        go = Go(shell, '+3')
        parsed_time = go.parse()
        self.assertEqual(parsed_time, target_date)

    def test_validDateArg4_validTime(self):
        shell = ShellAssistCmd()
        shell.current_date = date(2015, 5, 25)
        target_date = date(2015, 5, 22)
        go = Go(shell, '-3')
        parsed_time = go.parse()
        self.assertEqual(parsed_time, target_date)
