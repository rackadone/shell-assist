#from shellassist.test.test_storage import TestStorageMethods
from shellassist.test.test_calendar import *
import unittest


suites = [
  unittest.TestLoader().loadTestsFromTestCase(CalendarLoadYearTestCase),
  unittest.TestLoader().loadTestsFromTestCase(CalendarSaveYearTestCase)
]

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=2).run(alltests)

# from storage import storage
# print 'import success'