import unittest
from datetime import time
from shellassist.calendar import time_functions


class ParseTimeTestCase(unittest.TestCase):
    def test_validTimeArg1_validTime(self):
        correct_time = time(8, 45)
        parsed_time = time_functions.parse_time('08:45')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg2_validTime(self):
        correct_time = time(8, 45)
        parsed_time = time_functions.parse_time('8:45')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg3_validTime(self):
        correct_time = time(8)
        parsed_time = time_functions.parse_time('8')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg4_validTime(self):
        correct_time = time(18)
        parsed_time = time_functions.parse_time('18')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg5_validTime(self):
        correct_time = time(1, 15)
        parsed_time = time_functions.parse_time('0115')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg6_validTime(self):
        correct_time = time(1, 15)
        parsed_time = time_functions.parse_time('115')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg7_validTime(self):
        correct_time = time(0, 15)
        parsed_time = time_functions.parse_time('12:15am')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg8_validTime(self):
        correct_time = time(13, 15)
        parsed_time = time_functions.parse_time('1:15pm')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg9_validTime(self):
        correct_time = time(1, 15)
        parsed_time = time_functions.parse_time('1:15am')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg10_validTime(self):
        correct_time = time(0, 15)
        parsed_time = time_functions.parse_time('0:15am')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg11_validTime(self):
        correct_time = time(13, 15)
        parsed_time = time_functions.parse_time('13:15pm')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg12_validTime(self):
        correct_time = time(12, 15)
        parsed_time = time_functions.parse_time('1215pm')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg13_validTime(self):
        correct_time = time(14, 15)
        parsed_time = time_functions.parse_time('215pm')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg14_validTime(self):
        correct_time = time(13, 15)
        parsed_time = time_functions.parse_time('1315pm')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg15_validTime(self):
        correct_time = time(13, 15)
        parsed_time = time_functions.parse_time('1315am')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg16_validTime(self):
        correct_time = time(13)
        parsed_time = time_functions.parse_time('13am')
        self.assertEqual(parsed_time, correct_time)

    def test_validTimeArg17_validTime(self):
        correct_time = time(1)
        parsed_time = time_functions.parse_time('1am')
        self.assertEqual(parsed_time, correct_time)
