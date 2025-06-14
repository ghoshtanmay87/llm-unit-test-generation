def compute_Last_Digit(A,B): 
    variable = 1
    if (A == B): 
        return 1
    elif ((B - A) >= 5):  
        return 0
    else:   
        for i in range(A + 1,B + 1): 
            variable = (variable * (i % 10)) % 10
        return variable % 10

import pytest

def test_when_A_equals_B_returns_1():
    # When A equals B, the function returns 1
    A = 5
    B = 5
    expected_output = 1
    assert compute_Last_Digit(A, B) == expected_output

def test_difference_B_minus_A_5_or_more_returns_0():
    # When the difference between B and A is 5 or more, the function returns 0
    A = 3
    B = 8
    expected_output = 0
    assert compute_Last_Digit(A, B) == expected_output

def test_difference_less_than_5_product_last_digits_mod_10_case_1():
    # When the difference between B and A is less than 5, compute product of last digits modulo 10
    A = 2
    B = 4
    expected_output = 4
    assert compute_Last_Digit(A, B) == expected_output

def test_difference_less_than_5_product_last_digits_mod_10_case_2():
    # Check last digit product for a small range with difference less than 5
    A = 7
    B = 10
    expected_output = 0
    assert compute_Last_Digit(A, B) == expected_output

def test_difference_exactly_4_product_last_digits_mod_10():
    # When difference is exactly 4, compute product of last digits modulo 10
    A = 1
    B = 5
    expected_output = 0
    assert compute_Last_Digit(A, B) == expected_output

def test_difference_zero_A_equals_B_returns_1():
    # When difference is 0 (A equals B), returns 1
    A = 0
    B = 0
    expected_output = 1
    assert compute_Last_Digit(A, B) == expected_output

def test_difference_1_multiply_last_digit_of_B_only():
    # When difference is 1, multiply last digit of B only
    A = 9
    B = 10
    expected_output = 0
    assert compute_Last_Digit(A, B) == expected_output

def test_difference_3_multiply_last_digits_of_range():
    # When difference is 3, multiply last digits of numbers in range
    A = 11
    B = 14
    expected_output = 2
    assert compute_Last_Digit(A, B) == expected_output