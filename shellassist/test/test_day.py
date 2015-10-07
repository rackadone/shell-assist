import unittest
from shellassist.calendar.day import Day
from shellassist.calendar.activity import Activity

class RemoveActivityTestCase(unittest.TestCase):
  def setUp(self):
    self.day = Day(1)

  def tearDown(self):
    self.day = None

  def test_noActivities_false(self):
    zero = self.day.remove_activity(0)
    self.assertFalse(zero)

    one = self.day.remove_activity(1)
    self.assertFalse(one)

    minus_one = self.day.remove_activity(-1)
    self.assertFalse(minus_one)

  def test_withinBounds_true(self):
    # arrange
    self.day.add_activity(Activity(1, 1, 1))

    # act
    zero = self.day.remove_activity(0)

    # assert
    self.assertTrue(zero)
    self.assertEqual(self.day.activity_count(), 0)

  def test_outOfBounds_false(self):
    # arrange
    self.day.add_activity(Activity(1, 1, 1))

    # act/assert
    one = self.day.remove_activity(1)
    self.assertFalse(one)

    minus_one = self.day.remove_activity(-1)
    self.assertFalse(minus_one)
    

    

