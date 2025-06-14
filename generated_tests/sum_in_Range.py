def sum_Odd(n): 
    terms = (n + 1)//2
    sum1 = terms * terms 
    return sum1  
def sum_in_Range(l,r): 
    return sum_Odd(r) - sum_Odd(l - 1)

import pytest

def test_sum_odd_numbers_1_to_5():
    # Sum of odd numbers from 1 to 5
    result = sum_in_Range(1, 5)
    assert result == 9

def test_sum_odd_numbers_2_to_7():
    # Sum of odd numbers from 2 to 7
    # Note: corrected expected output to 15 as per reasoning
    result = sum_in_Range(2, 7)
    assert result == 15

def test_sum_odd_numbers_3_to_3():
    # Sum of odd numbers from 3 to 3 (single odd number)
    result = sum_in_Range(3, 3)
    assert result == 3

def test_sum_odd_numbers_4_to_4():
    # Sum of odd numbers from 4 to 4 (single even number, no odd numbers in range)
    result = sum_in_Range(4, 4)
    assert result == 0

def test_sum_odd_numbers_1_to_1():
    # Sum of odd numbers from 1 to 1 (single odd number)
    result = sum_in_Range(1, 1)
    assert result == 1

def test_sum_odd_numbers_10_to_15():
    # Sum of odd numbers from 10 to 15
    # Note: corrected expected output to 39 as per reasoning
    result = sum_in_Range(10, 15)
    assert result == 39

def test_sum_odd_numbers_0_to_0():
    # Sum of odd numbers from 0 to 0 (empty range)
    result = sum_in_Range(0, 0)
    assert result == 0