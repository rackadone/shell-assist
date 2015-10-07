#from shellassist.test.test_storage import TestStorageMethods
from shellassist.test.test_calendar import *
from shellassist.test.test_day import *
import unittest


suites = [
  unittest.TestLoader().loadTestsFromTestCase(CalendarLoadYearTestCase),
  unittest.TestLoader().loadTestsFromTestCase(CalendarSaveYearTestCase),
  
  unittest.TestLoader().loadTestsFromTestCase(RemoveActivityTestCase)
]

alltests = unittest.TestSuite(suites)

unittest.TextTestRunner(verbosity=2).run(alltests)

# from storage import storage
# print 'import success'