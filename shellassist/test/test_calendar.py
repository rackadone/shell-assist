import os
import shutil
import pickle
import unittest
from shellassist.calendar.calendar import Calendar
from shellassist.calendar.year import Year


class CalendarLoadYearTestCase(unittest.TestCase):
    def setUp(self):
        if os.path.exists('saves'):
            shutil.rmtree('saves')

    def tearDown(self):
        if os.path.exists('saves'):
                shutil.rmtree('saves')

    def test_folderDoesntExists_newYearCreated(self):
        # act
        year = Calendar.load_year(2015)
        year_number = year.number

        # assert
        self.assertEqual(year_number, 2015)

    def test_folderAlreadyExists_yearReturned(self):
        # arrange
        sample_year = Year(2015)
        os.makedirs('saves')
        pickle.dump(sample_year, open(
            'saves/' + str(sample_year.number) + '.p', 'wb'))

        # act
        year = Calendar.load_year(2015)
        year_number = year.number

        # assert
        self.assertEqual(year_number, 2015)


class CalendarSaveYearTestCase(unittest.TestCase):
    def setUp(self):
        if os.path.exists('saves'):
            shutil.rmtree('saves')

    def tearDown(self):
        if os.path.exists('saves'):
                shutil.rmtree('saves')

    def test_folderDoesntExist_newYearCreated(self):
        # arrange
        test_year = Year(2015)

        # act
        file_path = 'saves/' + str(2015) + '.p'
        Calendar.save_year(test_year)
        year = pickle.load(open(file_path, 'rb'))
        year_number = year.number

        # assert
        self.assertEqual(year_number, 2015)
