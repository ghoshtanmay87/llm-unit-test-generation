def substract_elements(test_tup1, test_tup2):
  res = tuple(tuple(a - b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res)

import pytest

def test_subtract_positive_integer_tuples():
    test_tup1 = ((5, 10, 15), (20, 25, 30))
    test_tup2 = ((1, 2, 3), (4, 5, 6))
    expected_output = ((4, 8, 12), (16, 20, 24))
    assert substract_elements(test_tup1, test_tup2) == expected_output

def test_subtract_negative_and_positive_integer_tuples():
    test_tup1 = ((-1, 0, 1), (2, -2, 2))
    test_tup2 = ((1, -1, 0), (0, 2, -2))
    expected_output = ((-2, 1, 1), (2, -4, 4))
    assert substract_elements(test_tup1, test_tup2) == expected_output

def test_subtract_float_tuples():
    test_tup1 = ((1.5, 2.5), (3.5, 4.5))
    test_tup2 = ((0.5, 1.5), (1.5, 2.5))
    expected_output = ((1.0, 1.0), (2.0, 2.0))
    assert substract_elements(test_tup1, test_tup2) == expected_output

def test_subtract_single_element_tuples():
    test_tup1 = ((10,), (20,))
    test_tup2 = ((5,), (15,))
    expected_output = ((5,), (5,))
    assert substract_elements(test_tup1, test_tup2) == expected_output

def test_subtract_empty_inner_tuples():
    test_tup1 = ((), ())
    test_tup2 = ((), ())
    expected_output = ((), ())
    assert substract_elements(test_tup1, test_tup2) == expected_output