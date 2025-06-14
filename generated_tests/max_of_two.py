def max_of_two( x, y ):
    if x > y:
        return x
    return y

import pytest

def test_max_of_two_x_greater_than_y():
    # Scenario: x is greater than y
    x = 5
    y = 3
    expected = 5
    assert max_of_two(x, y) == expected

def test_max_of_two_y_greater_than_x():
    # Scenario: y is greater than x
    x = 2
    y = 7
    expected = 7
    assert max_of_two(x, y) == expected

def test_max_of_two_x_equal_to_y():
    # Scenario: x is equal to y
    x = 4
    y = 4
    expected = 4
    assert max_of_two(x, y) == expected

def test_max_of_two_x_negative_less_than_y():
    # Scenario: x is negative and less than y
    x = -10
    y = -5
    expected = -5
    assert max_of_two(x, y) == expected

def test_max_of_two_x_negative_greater_than_y():
    # Scenario: x is negative and greater than y
    x = -3
    y = -8
    expected = -3
    assert max_of_two(x, y) == expected