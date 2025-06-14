def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

import pytest

def test_choose_num_x_greater_than_y():
    # Scenario: x is greater than y
    # Since x (5) is greater than y (3), the function immediately returns -1.
    assert choose_num(5, 3) == -1

def test_choose_num_y_even_x_less_than_y():
    # Scenario: y is even and x is less than y
    # x (2) is not greater than y (4), so the first condition fails.
    # y (4) is even, so the function returns y (4).
    assert choose_num(2, 4) == 4

def test_choose_num_x_equals_y_y_odd():
    # Scenario: x equals y and y is odd
    # x (7) is not greater than y (7), so first condition fails.
    # y (7) is odd, so second condition fails.
    # x equals y, so the function returns -1.
    assert choose_num(7, 7) == -1

def test_choose_num_x_less_than_y_y_odd_x_not_equal_y():
    # Scenario: x less than y, y is odd, and x not equal to y
    # x (3) is not greater than y (5), so first condition fails.
    # y (5) is odd, so second condition fails.
    # x (3) is not equal to y (5), so third condition fails.
    # The function returns y - 1, which is 4.
    assert choose_num(3, 5) == 4

def test_choose_num_x_less_than_y_y_even():
    # Scenario: x less than y, y is even
    # x (0) is not greater than y (10), so first condition fails.
    # y (10) is even, so the function returns y (10).
    assert choose_num(0, 10) == 10