import math
def largest_triangle(a,b): 
    if (a < 0 or b < 0): 
        return -1 
    area = (3 * math.sqrt(3) * pow(a, 2)) / (4 * b);  
    return area

import pytest

def test_both_inputs_positive_a_less_than_b():
    a = 2
    b = 4
    expected_output = 1.299038105676658
    assert largest_triangle(a, b) == expected_output

def test_both_inputs_positive_a_greater_than_b():
    a = 5
    b = 3
    expected_output = 10.825317547305485
    assert largest_triangle(a, b) == expected_output

def test_a_zero_b_positive():
    a = 0
    b = 5
    expected_output = 0.0
    assert largest_triangle(a, b) == expected_output

def test_a_negative_b_positive():
    a = -1
    b = 2
    expected_output = -1
    assert largest_triangle(a, b) == expected_output

def test_a_positive_b_negative():
    a = 2
    b = -3
    expected_output = -1
    assert largest_triangle(a, b) == expected_output

def test_a_and_b_equal_positive():
    a = 3
    b = 3
    expected_output = 3.89711455245
    assert largest_triangle(a, b) == pytest.approx(expected_output, rel=1e-9)