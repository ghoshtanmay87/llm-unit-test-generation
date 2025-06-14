def sum_squares(lst):
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i) ** 2
    return squared

import pytest

def test_sum_squares_with_positive_integers():
    # Sum of squares with positive integers
    result = sum_squares([1, 2, 3])
    assert result == 14

def test_sum_squares_with_positive_floats_including_exact_integers():
    # Sum of squares with positive floats including exact integers
    result = sum_squares([1.0, 2.0, 3.0])
    assert result == 14

def test_sum_squares_with_negative_floats():
    # Sum of squares with negative floats
    result = sum_squares([-1.2, -2.5, -3.1])
    assert result == 14

def test_sum_squares_with_empty_list():
    # Sum of squares with empty list
    result = sum_squares([])
    assert result == 0

def test_sum_squares_with_positive_floats():
    # Sum of squares with positive floats
    result = sum_squares([1.2, 2.5, 3.1])
    assert result == 29

def test_sum_squares_with_mixed_positive_and_negative_floats():
    # Sum of squares with mixed positive and negative floats
    result = sum_squares([-1.7, 0, 2.3])
    assert result == 10

def test_sum_squares_with_zero_and_positive_floats():
    # Sum of squares with zero and positive floats
    result = sum_squares([0, 0.1, 0.9])
    assert result == 2

def test_sum_squares_with_large_numbers():
    # Sum of squares with large numbers
    result = sum_squares([10.1, 20.9, 30.5])
    assert result == 1523