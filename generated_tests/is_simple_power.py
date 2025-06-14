def is_simple_power(x, n):
    if n == 1:
        return x == 1
    power = 1
    while power < x:
        power = power * n
    return power == x

import pytest

def test_is_simple_power_one_and_one():
    # Check if 1 is a simple power of 1
    assert is_simple_power(1, 1) is True

def test_is_simple_power_two_and_one():
    # Check if 2 is a simple power of 1
    assert is_simple_power(2, 1) is False

def test_is_simple_power_eight_and_two():
    # Check if 8 is a simple power of 2
    assert is_simple_power(8, 2) is True

def test_is_simple_power_twelve_and_two():
    # Check if 12 is a simple power of 2
    assert is_simple_power(12, 2) is False

def test_is_simple_power_twentyseven_and_three():
    # Check if 27 is a simple power of 3
    assert is_simple_power(27, 3) is True

def test_is_simple_power_twentyeight_and_three():
    # Check if 28 is a simple power of 3
    assert is_simple_power(28, 3) is False

def test_is_simple_power_one_and_five():
    # Check if 1 is a simple power of 5
    assert is_simple_power(1, 5) is True

def test_is_simple_power_onehundredtwentyfive_and_five():
    # Check if 125 is a simple power of 5
    assert is_simple_power(125, 5) is True

def test_is_simple_power_onehundredtwentysix_and_five():
    # Check if 126 is a simple power of 5
    assert is_simple_power(126, 5) is False

def test_is_simple_power_zero_and_two():
    # Check if 0 is a simple power of 2
    assert is_simple_power(0, 2) is False