def upper_ctr(str):
    upper_ctr = 0
    for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
          return upper_ctr

import pytest

def test_upper_ctr_empty_string():
    # The input string is empty, so the loop does not run and the function returns 0 immediately.
    assert upper_ctr('') == 0

def test_upper_ctr_single_uppercase_letter():
    # The first character 'A' is uppercase, so upper_ctr increments to 1 and returns immediately.
    assert upper_ctr('A') == 1

def test_upper_ctr_single_lowercase_letter():
    # The first character 'a' is lowercase, so upper_ctr remains 0 and returns immediately.
    assert upper_ctr('a') == 0

def test_upper_ctr_multiple_characters_first_uppercase():
    # The function only checks the first character due to the misplaced return inside the loop.
    # 'A' is uppercase, so it returns 1 immediately without checking the rest.
    assert upper_ctr('AbcD') == 1

def test_upper_ctr_multiple_characters_first_lowercase():
    # The function checks only the first character 'a', which is lowercase,
    # so it returns 0 immediately without checking the rest.
    assert upper_ctr('aBCD') == 0