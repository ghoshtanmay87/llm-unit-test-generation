def sum_digits_single(x) : 
    ans = 0
    while x : 
        ans += x % 10
        x //= 10  
    return ans 
def closest(x) : 
    ans = 0
    while (ans * 10 + 9 <= x) : 
        ans = ans * 10 + 9  
    return ans   
def sum_digits_twoparts(N) : 
    A = closest(N)  
    return sum_digits_single(A) + sum_digits_single(N - A)

import pytest

def test_sum_digits_single_digit():
    # Scenario: Sum digits of N when N is a single-digit number
    N = 7
    expected = 7
    result = sum_digits_twoparts(N)
    assert result == expected

def test_sum_digits_all_nines():
    # Scenario: Sum digits of N when N is exactly a number with all 9s
    N = 99
    expected = 18
    result = sum_digits_twoparts(N)
    assert result == expected

def test_sum_digits_just_above_all_nines():
    # Scenario: Sum digits of N when N is just above a number with all 9s
    N = 100
    expected = 1
    result = sum_digits_twoparts(N)
    assert result == expected

def test_sum_digits_123():
    # Scenario: Sum digits of N when N is 123
    N = 123
    expected = 18
    result = sum_digits_twoparts(N)
    assert result == expected

def test_sum_digits_4567():
    # Scenario: Sum digits of N when N is 4567
    N = 4567
    expected = 37
    result = sum_digits_twoparts(N)
    assert result == expected