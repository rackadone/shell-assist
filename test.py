from shellassist.test.test_storage import TestStorageMethods
import unittest

suite = unittest.TestLoader().loadTestsFromTestCase(TestStorageMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

# from storage import storage
# print 'import success'