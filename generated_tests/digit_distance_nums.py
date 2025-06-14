def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

import pytest

def test_digit_distance_multiple_digits():
    # Calculate digit distance between two positive integers with multiple digits
    n1 = 123
    n2 = 456
    expected_output = 18
    assert digit_distance_nums(n1, n2) == expected_output

def test_digit_distance_larger_number_difference_multiple_digits():
    # Calculate digit distance when one number is larger and difference has multiple digits
    n1 = 1000
    n2 = 1
    expected_output = 1
    assert digit_distance_nums(n1, n2) == expected_output

def test_digit_distance_numbers_equal():
    # Calculate digit distance when numbers are equal
    n1 = 500
    n2 = 500
    expected_output = 0
    assert digit_distance_nums(n1, n2) == expected_output

def test_digit_distance_difference_single_digit():
    # Calculate digit distance when difference is a single digit
    n1 = 10
    n2 = 7
    expected_output = 3
    assert digit_distance_nums(n1, n2) == expected_output

def test_digit_distance_difference_includes_zero_digits():
    # Calculate digit distance when difference includes zero digits
    n1 = 100
    n2 = 90
    expected_output = 1
    assert digit_distance_nums(n1, n2) == expected_output