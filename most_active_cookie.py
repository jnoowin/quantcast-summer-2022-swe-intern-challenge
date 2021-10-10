import sys
import re

def parse_input(argv):
    LENGTH_ERROR = 'Number of arguments did not match expected format "most_active_cookie.py <LOG-NAME>.csv -d <DATE>"'
    PARAM_ERROR = 'Expected parameter flag: -d'
    DATE_ERROR = 'Expected date in UTC Day Format YYYY-MM-DD'

    try:
        assert len(argv) == 4, LENGTH_ERROR
        csv_path = argv[1]
        param = argv[2]
        day = argv[3]

        assert param == '-d', PARAM_ERROR
        assert is_utc(day), DATE_ERROR

        log = read_cookie_log(csv_path)

        cookies = get_most_active_cookie(log, day)
        for cookie in cookies:
            print(cookie)
    except AssertionError as error:
        print(error)
    except FileNotFoundError:
        print('Invalid CSV cookie log path')
    except IOError:
        print('An IO error occurred')

def read_cookie_log(csv_path):
    log = {}
    with open(csv_path, 'r') as csv_file:
        csv_file.readline()  # remove header
        for line in csv_file.read().splitlines():
            cookie, date = line.split(',')
            day, time_offset = date.split('T')
            time, _ = re.split('\+|\-', time_offset)
            if day not in log:
                log[day] = {cookie: 1}
            else:
                log[day][cookie] = log[day].get(cookie, 0) + 1
    return log

def get_most_active_cookie(log, day):
    cookies_in_day = log.get(day)

    if not cookies_in_day:
        return []

    max_freq = max(cookies_in_day.values())
    return filter(lambda cookie: cookies_in_day[cookie] == max_freq, cookies_in_day.keys())

def is_utc(day):
    '''Asserts UTC date format of YYYY-MM-DD according to https://www.w3.org/TR/NOTE-datetime'''
    pattern = '\d{4}-\d{2}-\d{2}'
    return bool(re.search(pattern, day))


if __name__ == '__main__':
    parse_input(sys.argv)
