import datetime
def check_date(m, d, y):
    try:
        m, d, y = map(int, (m, d, y))
        datetime.date(y, m, d)
        return True
    except ValueError:
        return False

import pytest

def test_valid_date_with_typical_values():
    # The inputs '12', '25', '2023' convert to integers 12, 25, 2023 which form a valid date December 25, 2023.
    assert check_date('12', '25', '2023') is True

def test_invalid_date_with_day_out_of_range():
    # February 30, 2023 is invalid because February has at most 29 days in a leap year and 28 otherwise. 2023 is not a leap year.
    assert check_date('2', '30', '2023') is False

def test_valid_leap_year_date():
    # February 29, 2024 is valid because 2024 is a leap year.
    assert check_date('2', '29', '2024') is True

def test_invalid_leap_year_date_on_non_leap_year():
    # February 29, 2023 is invalid because 2023 is not a leap year.
    assert check_date('2', '29', '2023') is False

def test_invalid_month_value_zero():
    # Month 0 is invalid since months must be between 1 and 12.
    assert check_date('0', '10', '2023') is False

def test_invalid_month_value_greater_than_12():
    # Month 13 is invalid since months must be between 1 and 12.
    assert check_date('13', '10', '2023') is False

def test_valid_date_with_single_digit_month_and_day():
    # April 7, 2023 is a valid date.
    assert check_date('4', '7', '2023') is True

def test_invalid_day_value_zero():
    # Day 0 is invalid since days must be between 1 and the number of days in the month.
    assert check_date('5', '0', '2023') is False

def test_invalid_day_value_too_large_for_month():
    # April has only 30 days, so day 31 is invalid.
    assert check_date('4', '31', '2023') is False

def test_valid_date_with_year_as_string_with_leading_zeros():
    # January 1, year 1 is a valid date; leading zeros in year string are correctly converted to integer 1.
    assert check_date('1', '1', '0001') is True