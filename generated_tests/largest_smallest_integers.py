def largest_smallest_integers(lst):
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)

import pytest

def test_list_with_negative_and_positive_integers():
    result = largest_smallest_integers([-10, -3, 0, 2, 5, 8])
    assert result == (-3, 2)

def test_list_with_only_negative_integers():
    result = largest_smallest_integers([-7, -1, -20, -3])
    assert result == (-1, None)

def test_list_with_only_positive_integers():
    result = largest_smallest_integers([4, 10, 1, 7])
    assert result == (None, 1)

def test_list_with_zeros_only():
    result = largest_smallest_integers([0, 0, 0])
    assert result == (None, None)

def test_list_with_negative_positive_and_zero_values():
    result = largest_smallest_integers([-5, 0, 3, -2, 0, 4])
    assert result == (-2, 3)

def test_empty_list():
    result = largest_smallest_integers([])
    assert result == (None, None)

def test_list_with_one_negative_and_one_positive_integer():
    result = largest_smallest_integers([-1, 1])
    assert result == (-1, 1)

def test_list_with_multiple_negative_and_positive_integers_including_duplicates():
    result = largest_smallest_integers([-4, -4, 2, 2, 3, -1])
    assert result == (-1, 2)