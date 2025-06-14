def is_Diff(n): 
    return (n % 11 == 0)

import pytest

def test_is_Diff_multiple_of_11():
    # Input is a multiple of 11
    n = 33
    expected = True
    assert is_Diff(n) == expected

def test_is_Diff_not_multiple_of_11():
    # Input is not a multiple of 11
    n = 25
    expected = False
    assert is_Diff(n) == expected

def test_is_Diff_zero_input():
    # Input is zero
    n = 0
    expected = True
    assert is_Diff(n) == expected

def test_is_Diff_negative_multiple_of_11():
    # Input is a negative multiple of 11
    n = -44
    expected = True
    assert is_Diff(n) == expected

def test_is_Diff_negative_not_multiple_of_11():
    # Input is a negative number not multiple of 11
    n = -15
    expected = False
    assert is_Diff(n) == expected