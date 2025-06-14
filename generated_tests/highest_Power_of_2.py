def highest_Power_of_2(n): 
    res = 0; 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i; 
            break; 
    return res;

import pytest

def test_highest_power_of_2_less_than_or_equal_10():
    # The highest power of 2 less than or equal to 10 is 8.
    assert highest_Power_of_2(10) == 8

def test_highest_power_of_2_less_than_or_equal_1():
    # 1 is a power of 2, so the function returns 1 immediately.
    assert highest_Power_of_2(1) == 1

def test_highest_power_of_2_less_than_or_equal_15():
    # The highest power of 2 less than or equal to 15 is 8.
    assert highest_Power_of_2(15) == 8

def test_highest_power_of_2_less_than_or_equal_16():
    # 16 is a power of 2, so the function returns 16 immediately.
    assert highest_Power_of_2(16) == 16

def test_highest_power_of_2_less_than_or_equal_31():
    # The highest power of 2 less than or equal to 31 is 16.
    assert highest_Power_of_2(31) == 16

def test_highest_power_of_2_less_than_or_equal_64():
    # 64 is a power of 2, so the function returns 64 immediately.
    assert highest_Power_of_2(64) == 64

def test_highest_power_of_2_less_than_or_equal_0():
    # For n=0, the loop does not run, so the result remains 0.
    assert highest_Power_of_2(0) == 0

def test_highest_power_of_2_less_than_or_equal_3():
    # The highest power of 2 less than or equal to 3 is 2.
    assert highest_Power_of_2(3) == 2