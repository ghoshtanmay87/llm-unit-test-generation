def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

import pytest

def test_median_middle_value_a_between_b_and_c():
    # Median is the middle value when a is between b and c
    a, b, c = 5, 3, 7
    expected = 5
    assert median_numbers(a, b, c) == expected

def test_median_b_when_a_greater_b_and_b_greater_c():
    # Median is b when a > b and b > c
    a, b, c = 6, 4, 2
    expected = 4
    assert median_numbers(a, b, c) == expected

def test_median_c_when_a_greater_b_and_b_not_greater_c():
    # Median is c when a > b and b <= c
    a, b, c = 8, 3, 5
    expected = 5
    assert median_numbers(a, b, c) == expected

def test_median_a_when_a_less_equal_b_and_a_greater_c():
    # Median is a when a <= b and a > c
    a, b, c = 4, 7, 3
    expected = 4
    assert median_numbers(a, b, c) == expected

def test_median_b_when_a_less_equal_b_and_a_less_equal_c_and_b_less_c():
    # Median is b when a <= b and a <= c and b < c
    a, b, c = 2, 5, 6
    expected = 5
    assert median_numbers(a, b, c) == expected

def test_median_c_when_a_less_equal_b_and_a_less_equal_c_and_b_not_less_c():
    # Median is c when a <= b and a <= c and b >= c
    a, b, c = 1, 7, 4
    expected = 4
    assert median_numbers(a, b, c) == expected

def test_median_all_equal():
    # Median when all three numbers are equal
    a, b, c = 3, 3, 3
    expected = 3
    assert median_numbers(a, b, c) == expected

def test_median_two_equal_median_is_that_value():
    # Median when two numbers are equal and median is that value
    a, b, c = 5, 5, 7
    expected = 5
    assert median_numbers(a, b, c) == expected

def test_median_two_equal_median_is_other_value():
    # Median when two numbers are equal and median is the other value
    a, b, c = 7, 5, 5
    expected = 5
    assert median_numbers(a, b, c) == expected