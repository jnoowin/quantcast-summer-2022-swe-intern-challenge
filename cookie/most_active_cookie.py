import sys
import re

def parse_input(argv):
    '''
    Parses command line input and asserts correctness
    Main function to read cookie log and return most active cookie
    '''
    LENGTH_ERROR = 'Number of arguments did not match expected format "most_active_cookie.py <LOG-NAME>.csv -d <DATE>"'
    PARAM_ERROR = 'Expected parameter flag: -d'
    DATE_ERROR = 'Expected date in UTC date format: YYYY-MM-DD'

    try:
        assert len(argv) == 4, LENGTH_ERROR
        csv_path = argv[1]
        param = argv[2]
        date = argv[3]

        assert param == '-d', PARAM_ERROR
        assert is_utc(date), DATE_ERROR

        log = read_cookie_log(csv_path)

        cookies = get_most_active_cookie(log, date)
        for cookie in cookies:
            print(cookie)
    except AssertionError as error:
        print(error)
    except FileNotFoundError:
        print('Invalid CSV cookie log path')
    except IOError:
        print('An IO error occurred')

def read_cookie_log(csv_path):
    '''
    Given a path for a csv cookie log to read, returns a dictionary mapping a date 
    to all cookies for that day. Each cookie maps to the frequency.
    '''
    log = {}
    with open(csv_path, 'r') as csv_file:
        csv_file.readline()  # remove header
        for line in csv_file.read().splitlines():
            cookie, date_time_tz = line.split(',')  # [cookie_value, utc_date]
            date, _ = date_time_tz.split('T')  # [YYYY-MM-DD, hh:mm:ssTZD]
            if date not in log:
                log[date] = {cookie: 1}
            else:
                log[date][cookie] = log[date].get(cookie, 0) + 1
    return log

def get_most_active_cookie(log, date):
    '''
    Given a log returned by 'read_cookie_log' and a date, 
    returns a list of that day's most active cookies
    '''
    cookies_in_day = log.get(date)

    if not cookies_in_day:
        return []

    max_freq = max(cookies_in_day.values())
    return filter(lambda cookie: cookies_in_day[cookie] == max_freq, cookies_in_day.keys())

def is_utc(date):
    '''Asserts UTC date format of YYYY-MM-DD according to https://www.w3.org/TR/NOTE-datetime'''
    pattern = '\d{4}-\d{2}-\d{2}'
    return bool(re.search(pattern, date))


if __name__ == '__main__':
    parse_input(sys.argv)
