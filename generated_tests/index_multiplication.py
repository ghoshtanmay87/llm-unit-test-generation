def index_multiplication(test_tup1, test_tup2):
  res = tuple(tuple(a * b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res)

import pytest

def test_multiplying_two_tuples_each_containing_two_tuples_of_equal_length():
    test_tup1 = ((1, 2), (3, 4))
    test_tup2 = ((5, 6), (7, 8))
    expected_output = ((5, 12), (21, 32))
    assert index_multiplication(test_tup1, test_tup2) == expected_output

def test_multiplying_two_tuples_each_containing_three_tuples_of_length_3():
    test_tup1 = ((1, 0, 2), (3, 4, 5), (6, 7, 8))
    test_tup2 = ((9, 8, 7), (6, 5, 4), (3, 2, 1))
    expected_output = ((9, 0, 14), (18, 20, 20), (18, 14, 8))
    assert index_multiplication(test_tup1, test_tup2) == expected_output

def test_multiplying_two_tuples_each_containing_one_empty_tuple():
    test_tup1 = ((),)
    test_tup2 = ((),)
    expected_output = ((),)
    assert index_multiplication(test_tup1, test_tup2) == expected_output

def test_multiplying_two_empty_tuples():
    test_tup1 = ()
    test_tup2 = ()
    expected_output = ()
    assert index_multiplication(test_tup1, test_tup2) == expected_output