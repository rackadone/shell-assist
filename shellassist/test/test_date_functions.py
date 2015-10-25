import unittest
from datetime import MINYEAR
from datetime import MAXYEAR
from shellassist.calendar import date_functions


class DateFunctionsTestCase(unittest.TestCase):
    def test_get_date(self):
        nothing = date_functions.get_date()
        self.assertIsNone(nothing)

        no_day = date_functions.get_date(month=1, year=1)
        self.assertIsNone(no_day)

        # Test case demonstrates weaknesses of target
        # function. Function should handle all possible
        # edge cases.


class ValidateDayTestCase(unittest.TestCase):
    def test_validDay_True(self):
        self.assertTrue(date_functions.validate_day(1))
        self.assertTrue(date_functions.validate_day('1'))
        self.assertTrue(date_functions.validate_day(31))
        self.assertTrue(date_functions.validate_day('31'))

    def test_invalidDay_False(self):
        self.assertFalse(date_functions.validate_day(0))
        self.assertFalse(date_functions.validate_day('0'))
        self.assertFalse(date_functions.validate_day(-1))
        self.assertFalse(date_functions.validate_day('-1'))
        self.assertFalse(date_functions.validate_day(32))
        self.assertFalse(date_functions.validate_day('a'))
        self.assertFalse(date_functions.validate_day('32a'))


class ValidateMonthTestCase(unittest.TestCase):
    def test_validMonth_True(self):
        self.assertTrue(date_functions.validate_month(1))
        self.assertTrue(date_functions.validate_month('1'))
        self.assertTrue(date_functions.validate_month(12))
        self.assertTrue(date_functions.validate_month('12'))

    def test_invalidMonth_False(self):
        self.assertFalse(date_functions.validate_month(0))
        self.assertFalse(date_functions.validate_month('0'))
        self.assertFalse(date_functions.validate_month(-1))
        self.assertFalse(date_functions.validate_month('-1'))
        self.assertFalse(date_functions.validate_month(13))
        self.assertFalse(date_functions.validate_month('13'))
        self.assertFalse(date_functions.validate_month('a'))
        self.assertFalse(date_functions.validate_month('32A'))


class ValidateYearTestCase(unittest.TestCase):
    def test_validYear_True(self):
        self.assertTrue(date_functions.validate_year(MINYEAR))
        self.assertTrue(date_functions.validate_year(str(MINYEAR)))
        self.assertTrue(date_functions.validate_year(MAXYEAR))
        self.assertTrue(date_functions.validate_year(str(MINYEAR)))

    def test_invalidYear_False(self):
        self.assertFalse(date_functions.validate_year(0))
        self.assertFalse(date_functions.validate_year('0'))
        self.assertFalse(date_functions.validate_year(-1))
        self.assertFalse(date_functions.validate_year('-1'))
        self.assertFalse(date_functions.validate_year(MAXYEAR + 1))
        self.assertFalse(date_functions.validate_year(str(MAXYEAR + 1)))
        self.assertFalse(date_functions.validate_year('a'))
        self.assertFalse(date_functions.validate_year('32a'))
