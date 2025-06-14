def min_of_two( x, y ):
    if x < y:
        return x
    return y

import pytest

def test_min_of_two_x_less_than_y():
    # Scenario: x is less than y
    x = 3
    y = 5
    expected = 3
    assert min_of_two(x, y) == expected

def test_min_of_two_x_greater_than_y():
    # Scenario: x is greater than y
    x = 10
    y = 7
    expected = 7
    assert min_of_two(x, y) == expected

def test_min_of_two_x_equal_to_y():
    # Scenario: x is equal to y
    x = 4
    y = 4
    expected = 4
    assert min_of_two(x, y) == expected

def test_min_of_two_x_negative_and_less_than_y():
    # Scenario: x is negative and less than y
    x = -2
    y = 1
    expected = -2
    assert min_of_two(x, y) == expected

def test_min_of_two_y_negative_and_less_than_x():
    # Scenario: y is negative and less than x
    x = 0
    y = -5
    expected = -5
    assert min_of_two(x, y) == expected