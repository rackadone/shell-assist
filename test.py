from shellassist.test.test_calendar import *
from shellassist.test.test_day import *
from shellassist.test.test_date_functions import *
from shellassist.test.test_time_functions import *
import unittest


suites = [
  unittest.TestLoader().loadTestsFromTestCase(CalendarLoadYearTestCase),
  unittest.TestLoader().loadTestsFromTestCase(CalendarSaveYearTestCase),

  unittest.TestLoader().loadTestsFromTestCase(RemoveActivityTestCase),
  unittest.TestLoader().loadTestsFromTestCase(DateFunctionsTestCase),
  unittest.TestLoader().loadTestsFromTestCase(ValidateDayTestCase),
  unittest.TestLoader().loadTestsFromTestCase(ValidateMonthTestCase),
  unittest.TestLoader().loadTestsFromTestCase(ValidateYearTestCase),

  unittest.TestLoader().loadTestsFromTestCase(ParseTimeTestCase),
]

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=2).run(alltests)
