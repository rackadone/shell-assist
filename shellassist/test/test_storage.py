import unittest
from shellassist.storage.storage import Storage

class TestStorageMethods(unittest.TestCase):
  def suite(self):
    print('suite loaded')
    return unittest.TestLoader().loadTestsFromTestCase(TestStorageMethods)

  def test_setup(self):
    print "test_setup"
    Storage.setup(1, 1)
    self.assertEqual(1, 1)