import sys
import re

def parse_input(argv):
    LENGTH_ERROR = 'Number of arguments did not match expected format "most_active_cookie.py <LOG-NAME>.csv -d <DATE>"'
    PARAM_ERROR = 'Expected parameter flag: -d'
    DATE_ERROR = 'Expected date in UTC Day Format YYYY-MM-DD'
    print(argv)
    try:
        assert len(argv) == 4, LENGTH_ERROR
        csv_path = argv[1]
        param = argv[2]
        day = argv[3]

        assert param == '-d', PARAM_ERROR
        assert is_utc(day), DATE_ERROR
    except AssertionError as error:
        print(error)


def is_utc(day):
    '''Asserts UTC date format of YYYY-MM-DD according to https://www.w3.org/TR/NOTE-datetime'''
    pattern = '\d{4}-\d{2}-\d{2}'
    return bool(re.search(pattern, day))



if __name__ == '__main__':
    parse_input(sys.argv)
