def odd_Days(N): 
    hund1 = N // 100
    hund4 = N // 400
    leap = N >> 2
    ordd = N - leap 
    if (hund1): 
        ordd += hund1 
        leap -= hund1 
    if (hund4): 
        ordd -= hund4 
        leap += hund4 
    days = ordd + leap * 2
    odd = days % 7
    return odd

import pytest

def test_odd_days_base_case_zero():
    # Calculate odd days for N=0 (base case)
    result = odd_Days(0)
    assert result == 0

def test_odd_days_smallest_positive_integer():
    # Calculate odd days for N=1 (smallest positive integer)
    result = odd_Days(1)
    assert result == 1

def test_odd_days_first_leap_year():
    # Calculate odd days for N=4 (first leap year)
    result = odd_Days(4)
    assert result == 1

def test_odd_days_one_century():
    # Calculate odd days for N=100 (one century)
    result = odd_Days(100)
    assert result == 2

def test_odd_days_one_400_year_cycle():
    # Calculate odd days for N=400 (one 400-year cycle)
    result = odd_Days(400)
    assert result == 0

def test_odd_days_one_common_year():
    # Calculate odd days for N=365 (one common year)
    result = odd_Days(365)
    assert result == 1

def test_odd_days_two_centuries():
    # Calculate odd days for N=200 (two centuries)
    result = odd_Days(200)
    assert result == 4