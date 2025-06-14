def add_nested_tuples(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res)

import pytest

def test_add_nested_tuples_equal_length_integer_pairs():
    test_tup1 = ((1, 2), (3, 4))
    test_tup2 = ((5, 6), (7, 8))
    expected_output = ((6, 8), (10, 12))
    assert add_nested_tuples(test_tup1, test_tup2) == expected_output

def test_add_nested_tuples_negative_and_zero_values():
    test_tup1 = ((0, -1), (-2, 3))
    test_tup2 = ((4, 1), (2, -3))
    expected_output = ((4, 0), (0, 0))
    assert add_nested_tuples(test_tup1, test_tup2) == expected_output

def test_add_nested_tuples_floating_point_numbers():
    test_tup1 = ((1.5, 2.5), (3.0, 4.0))
    test_tup2 = ((0.5, 1.5), (2.0, 3.0))
    expected_output = ((2.0, 4.0), (5.0, 7.0))
    assert add_nested_tuples(test_tup1, test_tup2) == expected_output

def test_add_nested_tuples_single_element_inner_tuples():
    test_tup1 = ((10,), (20,))
    test_tup2 = ((1,), (2,))
    expected_output = ((11,), (22,))
    assert add_nested_tuples(test_tup1, test_tup2) == expected_output

def test_add_nested_tuples_empty_tuples():
    test_tup1 = ()
    test_tup2 = ()
    expected_output = ()
    assert add_nested_tuples(test_tup1, test_tup2) == expected_output

def test_add_nested_tuples_inner_tuples_different_lengths_truncation():
    test_tup1 = ((1, 2, 3), (4, 5))
    test_tup2 = ((10, 20), (30, 40, 50))
    expected_output = ((11, 22), (34, 45))
    assert add_nested_tuples(test_tup1, test_tup2) == expected_output