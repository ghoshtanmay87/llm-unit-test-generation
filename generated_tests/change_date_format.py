import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\3-\2-\1', dt)

import pytest

def test_convert_standard_iso_date_with_zero_padded_month_and_day():
    # Convert a standard ISO date with zero-padded month and day
    input_dt = '2023-04-15'
    expected = '15-04-2023'
    assert change_date_format(input_dt) == expected

def test_convert_date_with_single_digit_month_and_day():
    # Convert a date with single-digit month and day
    input_dt = '2023-4-5'
    expected = '5-4-2023'
    assert change_date_format(input_dt) == expected

def test_convert_date_embedded_in_longer_string():
    # Convert a date embedded in a longer string
    input_dt = 'Date: 2023-12-01 is the deadline'
    expected = 'Date: 01-12-2023 is the deadline'
    assert change_date_format(input_dt) == expected

def test_string_with_multiple_dates_only_first_replaced():
    # String with multiple dates, only first date replaced
    input_dt = 'Start: 2023-1-1, End: 2023-12-31'
    expected = 'Start: 1-1-2023, End: 2023-12-31'
    assert change_date_format(input_dt) == expected

def test_string_with_no_matching_date_pattern():
    # String with no matching date pattern
    input_dt = 'No date here'
    expected = 'No date here'
    assert change_date_format(input_dt) == expected

def test_date_with_day_and_month_two_digits_without_zero_padding():
    # Date with day and month as two digits without zero-padding
    input_dt = '2023-11-9'
    expected = '9-11-2023'
    assert change_date_format(input_dt) == expected