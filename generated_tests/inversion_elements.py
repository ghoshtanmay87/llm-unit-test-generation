def inversion_elements(test_tup):
  res = tuple(list(map(lambda x: ~x, list(test_tup))))
  return (res)

import pytest

def test_inverting_bits_positive_integers():
    # Inverting bits of a tuple with positive integers
    test_tup = (1, 2, 3)
    expected_output = (-2, -3, -4)
    assert inversion_elements(test_tup) == expected_output

def test_inverting_bits_zero_and_positive_integers():
    # Inverting bits of a tuple with zero and positive integers
    test_tup = (0, 4, 7)
    expected_output = (-1, -5, -8)
    assert inversion_elements(test_tup) == expected_output

def test_inverting_bits_negative_integers():
    # Inverting bits of a tuple with negative integers
    test_tup = (-1, -2, -3)
    expected_output = (0, 1, 2)
    assert inversion_elements(test_tup) == expected_output

def test_inverting_bits_mixed_positive_negative_integers():
    # Inverting bits of a tuple with mixed positive and negative integers
    test_tup = (-5, 0, 5)
    expected_output = (4, -1, -6)
    assert inversion_elements(test_tup) == expected_output

def test_inverting_bits_single_zero_element():
    # Inverting bits of a tuple with a single zero element
    test_tup = (0,)
    expected_output = (-1,)
    assert inversion_elements(test_tup) == expected_output

def test_inverting_bits_empty_tuple():
    # Inverting bits of an empty tuple
    test_tup = ()
    expected_output = ()
    assert inversion_elements(test_tup) == expected_output