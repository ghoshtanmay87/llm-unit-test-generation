def generate_integers(a, b):
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))
    return [i for i in range(lower, upper + 1) if i % 2 == 0]

import pytest

def test_both_inputs_within_range_a_less_than_b():
    # Both inputs within range and a < b
    a = 3
    b = 7
    expected = [4, 6]
    assert generate_integers(a, b) == expected

def test_both_inputs_within_range_a_greater_than_b():
    # Both inputs within range and a > b
    a = 7
    b = 3
    expected = [4, 6]
    assert generate_integers(a, b) == expected

def test_inputs_spanning_below_and_above_bounds():
    # Inputs spanning below and above bounds
    a = 1
    b = 9
    expected = [2, 4, 6, 8]
    assert generate_integers(a, b) == expected

def test_inputs_equal_within_bounds_and_even():
    # Inputs equal and within bounds and even
    a = 4
    b = 4
    expected = [4]
    assert generate_integers(a, b) == expected

def test_inputs_equal_within_bounds_and_odd():
    # Inputs equal and within bounds and odd
    a = 5
    b = 5
    expected = []
    assert generate_integers(a, b) == expected

def test_inputs_equal_and_below_lower_bound():
    # Inputs equal and below lower bound
    a = 1
    b = 1
    expected = []
    assert generate_integers(a, b) == expected

def test_inputs_equal_and_above_upper_bound():
    # Inputs equal and above upper bound
    a = 9
    b = 9
    expected = []
    assert generate_integers(a, b) == expected

def test_inputs_below_lower_bound():
    # Inputs below lower bound
    a = 0
    b = 1
    expected = []
    assert generate_integers(a, b) == expected

def test_inputs_above_upper_bound():
    # Inputs above upper bound
    a = 10
    b = 12
    expected = []
    assert generate_integers(a, b) == expected