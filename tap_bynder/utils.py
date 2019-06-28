import singer
import pendulum
import re


def format_last_updated_for_request(last_updated, key_format):
    updated_str = pendulum.parse(last_updated).to_datetime_string()
    date_str = re.search('([0-9]{4}-[0-1][0-9]-[0-3][0-9]) '
                         '[0-2][0-9]:[0-5][0-9]:[0-5][0-9]',
                         updated_str).group(1)
    time_str = re.search('[0-9]{4}-[0-1][0-9]-[0-3][0-9] '
                         '([0-2][0-9]:[0-5][0-9]:[0-5][0-9])',
                         updated_str).group(1)
    date_str += 'T'
    time_str += 'Z'
    date_str += time_str
    return date_str
