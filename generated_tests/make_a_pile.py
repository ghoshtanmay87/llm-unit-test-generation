def make_a_pile(n):
    return [n + 2 * i for i in range(n)]

import pytest

def test_make_a_pile_empty_pile():
    # Create a pile with n=0 (empty pile)
    result = make_a_pile(0)
    expected = []
    assert result == expected

def test_make_a_pile_single_element():
    # Create a pile with n=1 (single element)
    result = make_a_pile(1)
    expected = [1]
    assert result == expected

def test_make_a_pile_multiple_elements():
    # Create a pile with n=3 (multiple elements)
    result = make_a_pile(3)
    expected = [3, 5, 7]
    assert result == expected

def test_make_a_pile_larger_pile():
    # Create a pile with n=5 (larger pile)
    result = make_a_pile(5)
    expected = [5, 7, 9, 11, 13]
    assert result == expected

def test_make_a_pile_small_pile():
    # Create a pile with n=2 (small pile)
    result = make_a_pile(2)
    expected = [2, 4]
    assert result == expected