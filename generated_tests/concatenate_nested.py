def concatenate_nested(test_tup1, test_tup2):
  res = test_tup1 + test_tup2
  return (res)

import pytest

def test_concatenate_two_non_empty_tuples_of_integers():
    test_tup1 = (1, 2, 3)
    test_tup2 = (4, 5, 6)
    expected_output = (1, 2, 3, 4, 5, 6)
    assert concatenate_nested(test_tup1, test_tup2) == expected_output

def test_concatenate_empty_tuple_with_non_empty_tuple():
    test_tup1 = ()
    test_tup2 = (7, 8)
    expected_output = (7, 8)
    assert concatenate_nested(test_tup1, test_tup2) == expected_output

def test_concatenate_non_empty_tuple_with_empty_tuple():
    test_tup1 = (9, 10)
    test_tup2 = ()
    expected_output = (9, 10)
    assert concatenate_nested(test_tup1, test_tup2) == expected_output

def test_concatenate_two_empty_tuples():
    test_tup1 = ()
    test_tup2 = ()
    expected_output = ()
    assert concatenate_nested(test_tup1, test_tup2) == expected_output

def test_concatenate_tuples_containing_nested_tuples():
    test_tup1 = ((1, 2), (3, 4))
    test_tup2 = ((5, 6),)
    expected_output = ((1, 2), (3, 4), (5, 6))
    assert concatenate_nested(test_tup1, test_tup2) == expected_output

def test_concatenate_tuples_containing_mixed_data_types():
    test_tup1 = (1, 'a', (2, 3))
    test_tup2 = (4.5, None)
    expected_output = (1, 'a', (2, 3), 4.5, None)
    assert concatenate_nested(test_tup1, test_tup2) == expected_output