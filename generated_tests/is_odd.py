def is_odd(n) : 
    if (n^1 == n-1) :
        return True; 
    else :
        return False;

import pytest

def test_is_odd_with_1():
    # Check if 1 is odd
    result = is_odd(1)
    assert result is True

def test_is_odd_with_2():
    # Check if 2 is odd
    result = is_odd(2)
    assert result is False

def test_is_odd_with_3():
    # Check if 3 is odd
    result = is_odd(3)
    assert result is True

def test_is_odd_with_0():
    # Check if 0 is odd
    result = is_odd(0)
    assert result is False

def test_is_odd_with_10():
    # Check if 10 is odd
    result = is_odd(10)
    assert result is False

def test_is_odd_with_11():
    # Check if 11 is odd
    result = is_odd(11)
    assert result is True