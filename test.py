import unittest
import io
import sys
from most_active_cookie import parse_input, read_cookie_log, get_most_active_cookie, is_utc, LENGTH_ERROR, PARAM_ERROR, DATE_ERROR

class Test(unittest.TestCase):
    def test_is_utc_valid(self):
        date = '2019-12-08'
        self.assertTrue(is_utc(date))

    def test_is_utc_invalid(self):
        date = '12-08-2019'
        self.assertFalse(is_utc(date))

    def test_get_most_active_cookie_valid(self):
        log = {'2019-12-08': {'most_active1': 3,
                              'most_active2': 3, 'least_active': 1}}
        date = '2019-12-08'
        self.assertEqual(['most_active1', 'most_active2'],
                         get_most_active_cookie(log, date))

    def test_get_most_active_cookie_empty_log(self):
        log = {}
        date = '2019-12-08'
        self.assertEqual([], get_most_active_cookie(log, date))

    def test_get_most_active_cookie_empty_date(self):
        log = {'2019-12-08': {}}
        date = '2019-12-08'
        self.assertEqual([], get_most_active_cookie(log, date))

    def test_read_cookie_log_valid(self):
        expected = {'2018-12-09': {'AtY0laUfhglK3lC7': 2, 'SAZuXPGUrfbcn5UA': 1, '5UAVanZf6UtGyKVS': 1},
                    '2018-12-08': {'SAZuXPGUrfbcn5UA': 1, '4sMM2LxV07bPJzwf': 1, 'fbcn5UAVanZf6UtG': 1},
                    '2018-12-07': {'4sMM2LxV07bPJzwf': 1}}
        actual = read_cookie_log('cookie_log.csv')
        self.assertEqual(expected, actual)

    def test_parse_input_length_error(self):
        console_output = io.StringIO()
        sys.stdout = console_output
        parse_input([])
        sys.stdout = sys.__stdout__
        self.assertEqual(LENGTH_ERROR, console_output.getvalue())

    def test_parse_input_param_error(self):
        console_output = io.StringIO()
        sys.stdout = console_output
        parse_input(['most_active_cookie.py',
                     'cookie_log.csv', '-bad', '2018-12-08'])
        sys.stdout = sys.__stdout__
        self.assertEqual(PARAM_ERROR, console_output.getvalue())

    def test_parse_input_date_error(self):
        console_output = io.StringIO()
        sys.stdout = console_output
        parse_input(['most_active_cookie.py',
                     'cookie_log.csv', '-d', '12-08-2018'])
        sys.stdout = sys.__stdout__
        self.assertEqual(DATE_ERROR, console_output.getvalue())

    def test_parse_input_date_valid(self):
        console_output = io.StringIO()
        sys.stdout = console_output
        parse_input(['most_active_cookie.py',
                     'cookie_log.csv', '-d', '2018-12-08'])
        sys.stdout = sys.__stdout__
        expected = 'SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n'
        self.assertEqual(expected, console_output.getvalue())


if __name__ == '__main__':
    unittest.main()
