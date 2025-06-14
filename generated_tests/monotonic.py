def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False

import pytest

def test_monotonic_strictly_increasing():
    # The list is sorted in ascending order, so it matches sorted(l). The function returns True.
    assert monotonic([1, 2, 3, 4, 5]) is True

def test_monotonic_strictly_decreasing():
    # The list is sorted in descending order, so it matches sorted(l, reverse=True). The function returns True.
    assert monotonic([5, 4, 3, 2, 1]) is True

def test_monotonic_constant_list():
    # The list is equal to both sorted(l) and sorted(l, reverse=True) since all elements are the same. The function returns True.
    assert monotonic([3, 3, 3, 3]) is True

def test_monotonic_neither_increasing_nor_decreasing():
    # The list is not sorted ascending or descending. It does not match sorted(l) or sorted(l, reverse=True). The function returns False.
    assert monotonic([1, 3, 2, 4, 5]) is False

def test_monotonic_with_duplicates_increasing():
    # The list is sorted ascending with duplicates allowed, so it matches sorted(l). The function returns True.
    assert monotonic([1, 2, 2, 3, 4]) is True

def test_monotonic_with_duplicates_not_monotonic():
    # The list is not sorted ascending or descending due to the '3, 2' sequence. It does not match sorted(l) or sorted(l, reverse=True). The function returns False.
    assert monotonic([1, 2, 3, 2, 4]) is False

def test_monotonic_empty_list():
    # An empty list is trivially sorted ascending and descending. The function returns True.
    assert monotonic([]) is True

def test_monotonic_single_element_list():
    # A single element list is trivially sorted ascending and descending. The function returns True.
    assert monotonic([42]) is True