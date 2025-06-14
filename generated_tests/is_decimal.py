def is_decimal(num):
    import re
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dnumre.search(num)
    return bool(result)

import pytest

def test_valid_integer_string_without_decimal_point():
    # The regex matches one or more digits with no decimal part, so '123' matches ^[0-9]+$ and returns True.
    assert is_decimal('123') is True

def test_valid_decimal_string_with_one_decimal_place():
    # The regex allows one or two digits after a decimal point. '45.6' matches ^[0-9]+\.[0-9]{1,2}$ and returns True.
    assert is_decimal('45.6') is True

def test_valid_decimal_string_with_two_decimal_places():
    # '78.90' matches the pattern with exactly two digits after the decimal point, so returns True.
    assert is_decimal('78.90') is True

def test_invalid_decimal_string_with_three_decimal_places():
    # The regex restricts decimal places to one or two digits only. '12.345' has three digits after decimal, so no match and returns False.
    assert is_decimal('12.345') is False

def test_invalid_string_with_no_digits_before_decimal_point():
    # The regex requires one or more digits before the decimal point. '.45' lacks digits before '.', so returns False.
    assert is_decimal('.45') is False

def test_invalid_string_with_letters_included():
    # The regex only allows digits and an optional decimal point with digits. '123a.45' contains a letter 'a', so no match and returns False.
    assert is_decimal('123a.45') is False

def test_empty_string_input():
    # Empty string does not match the regex pattern requiring digits, so returns False.
    assert is_decimal('') is False

def test_valid_integer_zero():
    # '0' is a digit and matches the pattern with no decimal part, so returns True.
    assert is_decimal('0') is True

def test_valid_decimal_zero_with_two_decimal_places():
    # '0.00' matches digits before and exactly two digits after decimal, so returns True.
    assert is_decimal('0.00') is True

def test_invalid_negative_number_string():
    # The regex does not allow a leading minus sign, so '-123.45' does not match and returns False.
    assert is_decimal('-123.45') is False

def test_invalid_decimal_with_trailing_dot():
    # The regex requires one or two digits after the decimal point if decimal is present. '123.' has no digits after '.', so returns False.
    assert is_decimal('123.') is False

def test_invalid_decimal_with_leading_plus_sign():
    # The regex does not allow a leading plus sign, so '+123.45' does not match and returns False.
    assert is_decimal('+123.45') is False

def test_invalid_decimal_with_spaces():
    # The regex anchors to start and end of string and does not allow spaces, so ' 123.45 ' fails to match and returns False.
    assert is_decimal(' 123.45 ') is False

def test_valid_decimal_with_one_digit_after_decimal_and_no_leading_zeros():
    # '9.9' matches digits before decimal and exactly one digit after decimal, so returns True.
    assert is_decimal('9.9') is True

def test_valid_decimal_with_leading_zeros():
    # Leading zeros are allowed as digits, so '000123.45' matches the pattern and returns True.
    assert is_decimal('000123.45') is True