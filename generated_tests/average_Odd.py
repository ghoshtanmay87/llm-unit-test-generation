def average_Odd(n) : 
    if (n%2==0) : 
        return ("Invalid Input") 
        return -1 
    sm =0
    count =0
    while (n>=1) : 
        count=count+1
        sm = sm + n 
        n = n-2
    return sm//count

import pytest

def test_average_odd_with_odd_positive_integer_7():
    # Input is an odd positive integer, calculating average of odd numbers down to 1
    n = 7
    expected = 4
    assert average_Odd(n) == expected

def test_average_odd_with_even_number_8():
    # Input is an even number, should return 'Invalid Input'
    n = 8
    expected = "Invalid Input"
    assert average_Odd(n) == expected

def test_average_odd_with_smallest_odd_positive_integer_1():
    # Input is 1, the smallest odd positive integer
    n = 1
    expected = 1
    assert average_Odd(n) == expected

def test_average_odd_with_larger_odd_number_15():
    # Input is a larger odd number, 15
    n = 15
    expected = 8
    assert average_Odd(n) == expected

def test_average_odd_with_odd_number_3():
    # Input is an odd number 3
    n = 3
    expected = 2
    assert average_Odd(n) == expected