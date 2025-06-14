def next_Power_Of_2(n): 
    count = 0; 
    if (n and not(n & (n - 1))): 
        return n   
    while( n != 0): 
        n >>= 1
        count += 1
    return 1 << count;

import pytest

def test_input_already_power_of_two_8():
    # Input is already a power of two
    n = 8
    expected = 8
    assert next_Power_Of_2(n) == expected

def test_input_zero_returns_one():
    # Input is zero
    n = 0
    expected = 1
    assert next_Power_Of_2(n) == expected

def test_input_one_power_of_two():
    # Input is one, which is a power of two
    n = 1
    expected = 1
    assert next_Power_Of_2(n) == expected

def test_input_not_power_of_two_5():
    # Input is not a power of two, next power of two is larger
    n = 5
    expected = 8
    assert next_Power_Of_2(n) == expected

def test_input_not_power_of_two_12():
    # Input is not a power of two, next power of two is larger
    n = 12
    expected = 16
    assert next_Power_Of_2(n) == expected

def test_input_large_power_of_two_1024():
    # Input is a large power of two
    n = 1024
    expected = 1024
    assert next_Power_Of_2(n) == expected

def test_input_just_below_power_of_two_15():
    # Input is just below a power of two
    n = 15
    expected = 16
    assert next_Power_Of_2(n) == expected