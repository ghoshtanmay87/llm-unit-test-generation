def add(lst):
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])

import pytest

def test_sum_even_elements_at_odd_indices_mixed_even_odd():
    # Indices 1, 3, 5 are odd indices. Elements at these indices are 2, 4, 6 respectively.
    # All are even, so sum is 2 + 4 + 6 = 12.
    assert add([1, 2, 3, 4, 5, 6]) == 12

def test_sum_even_elements_at_odd_indices_some_odd_numbers():
    # Odd indices are 1, 3, 5 with elements 3, 5, 8.
    # Only 8 is even, so sum is 8.
    assert add([10, 3, 20, 5, 30, 8]) == 8

def test_sum_even_elements_at_odd_indices_empty_list():
    # List is empty, so no elements at odd indices exist, sum is 0.
    assert add([]) == 0

def test_sum_even_elements_at_odd_indices_single_element():
    # Only index 0 exists which is even index, no odd indices, sum is 0.
    assert add([7]) == 0

def test_sum_even_elements_at_odd_indices_even_numbers_only():
    # Odd indices 1, 3, 5 have elements 2, 4, 6 all even,
    # sum is 2 + 4 + 6 = 12.
    assert add([0, 2, 0, 4, 0, 6]) == 12

def test_sum_even_elements_at_odd_indices_odd_numbers_only():
    # Odd indices 1, 3, 5 have elements 1, 3, 5 all odd,
    # so sum is 0.
    assert add([0, 1, 0, 3, 0, 5]) == 0

def test_sum_even_elements_at_odd_indices_negative_even_numbers():
    # Odd indices 1, 3, 5 have elements -2, -4, -6 all even,
    # sum is -2 + -4 + -6 = -12.
    assert add([10, -2, 20, -4, 30, -6]) == -12

def test_sum_even_elements_at_odd_indices_zero_at_odd_indices():
    # Zero is even, odd indices 1, 3, 5 have elements 0, 0, 0,
    # sum is 0.
    assert add([1, 0, 3, 0, 5, 0]) == 0