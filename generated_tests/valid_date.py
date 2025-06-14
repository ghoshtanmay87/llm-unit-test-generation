def valid_date(date):
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = (int(month), int(day), int(year))
        if month < 1 or month > 12:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12] and day < 1 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False
    return True

import pytest

def test_valid_date_month_31_days():
    # Valid date with month having 31 days
    assert valid_date('12-25-2020') is True

def test_invalid_month_zero():
    # Invalid month (zero)
    assert valid_date('0-15-2020') is False

def test_invalid_day_too_high_31_day_month():
    # Invalid day for 31-day month (day too high)
    assert valid_date('1-32-2020') is False

def test_invalid_day_too_high_30_day_month():
    # Invalid day for 30-day month (day too high)
    assert valid_date('6-31-2020') is False

def test_valid_february_day_29():
    # Valid date for February with day 29
    assert valid_date('2-29-2020') is True

def test_invalid_february_day_30():
    # Invalid day for February (day too high)
    assert valid_date('2-30-2020') is False

def test_invalid_day_zero():
    # Invalid day zero
    assert valid_date('3-0-2020') is False

def test_valid_date_with_extra_spaces():
    # Invalid format with extra spaces
    assert valid_date(' 7-15-2020 ') is True

def test_invalid_format_missing_parts():
    # Invalid format with missing parts
    assert valid_date('12-2020') is False

def test_invalid_non_numeric_input():
    # Invalid non-numeric input
    assert valid_date('a-b-c') is False

def test_invalid_day_zero_31_day_month_operator_precedence():
    # Invalid day for 31-day month due to operator precedence bug
    assert valid_date('1-0-2020') is False

def test_valid_february_day_1():
    # Valid date on February 1
    assert valid_date('2-1-2020') is True