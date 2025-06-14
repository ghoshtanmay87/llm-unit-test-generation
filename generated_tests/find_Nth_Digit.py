def find_Nth_Digit(p,q,N) :  
    while (N > 0) : 
        N -= 1;  
        p *= 10;  
        res = p // q;  
        p %= q;  
    return res;

import pytest

def test_find_1st_digit_after_decimal_for_half():
    # scenario: Find the 1st digit after decimal for 1/2
    p = 1
    q = 2
    N = 1
    expected_output = 5
    assert find_Nth_Digit(p, q, N) == expected_output

def test_find_6th_digit_after_decimal_for_one_over_eleven():
    # scenario: Find the 6th digit after decimal for 1/11
    p = 1
    q = 11
    N = 6
    expected_output = 9
    assert find_Nth_Digit(p, q, N) == expected_output

def test_find_2nd_digit_after_decimal_for_one_third():
    # scenario: Find the 2nd digit after decimal for 1/3
    p = 1
    q = 3
    N = 2
    expected_output = 3
    assert find_Nth_Digit(p, q, N) == expected_output

def test_find_3rd_digit_after_decimal_for_one_seventh():
    # scenario: Find the 3rd digit after decimal for 1/7
    p = 1
    q = 7
    N = 3
    expected_output = 2
    assert find_Nth_Digit(p, q, N) == expected_output

def test_find_5th_digit_after_decimal_for_twenty_two_sevenths():
    # scenario: Find the 5th digit after decimal for 22/7
    p = 22
    q = 7
    N = 5
    expected_output = 5
    assert find_Nth_Digit(p, q, N) == expected_output

def test_find_4th_digit_after_decimal_for_one_sixteenth():
    # scenario: Find the 4th digit after decimal for 1/16
    p = 1
    q = 16
    N = 4
    expected_output = 5
    assert find_Nth_Digit(p, q, N) == expected_output