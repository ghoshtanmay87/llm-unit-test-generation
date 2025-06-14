def average_Even(n) : 
    if (n% 2!= 0) : 
        return ("Invalid Input") 
        return -1  
    sm = 0
    count = 0
    while (n>= 2) : 
        count = count+1
        sm = sm+n 
        n = n-2
    return sm // count

import pytest

def test_average_even_with_even_positive_integer_10():
    # Input is an even positive integer 10
    # Expected output is 8 as per user story (though reasoning states 6, we trust expected_output)
    assert average_Even(10) == 8

def test_average_even_with_odd_positive_integer_7():
    # Input is an odd positive integer 7
    # Expected output is "Invalid Input"
    assert average_Even(7) == "Invalid Input"

def test_average_even_with_smallest_even_positive_integer_2():
    # Input is the smallest even positive integer 2
    # Expected output is 2
    assert average_Even(2) == 2

def test_average_even_with_large_even_integer_20():
    # Input is a large even integer 20
    # Expected output is 11
    assert average_Even(20) == 11