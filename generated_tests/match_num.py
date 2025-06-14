import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False

import pytest

def test_string_starts_with_digit_5():
    # The regex ^5 matches strings that start with '5'.
    # Since '5abc' starts with '5', the function returns True.
    assert match_num('5abc') is True

def test_string_starts_with_digit_other_than_5():
    # The regex ^5 only matches strings starting with '5'.
    # '4abc' starts with '4', so the function returns False.
    assert match_num('4abc') is False

def test_string_starts_with_5_followed_by_digits():
    # The string starts with '5', so the regex ^5 matches and the function returns True.
    assert match_num('5123') is True

def test_string_does_not_start_with_digit():
    # The string starts with 'a', not '5', so the regex ^5 does not match and the function returns False.
    assert match_num('abc5') is False

def test_empty_string_input():
    # An empty string does not start with '5', so the regex ^5 does not match and the function returns False.
    assert match_num('') is False