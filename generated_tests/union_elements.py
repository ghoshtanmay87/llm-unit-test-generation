def union_elements(test_tup1, test_tup2):
  res = tuple(set(test_tup1 + test_tup2))
  return (res)

import pytest

def test_union_no_overlapping_elements():
    # Union of two tuples with no overlapping elements
    test_tup1 = (1, 2, 3)
    test_tup2 = (4, 5, 6)
    expected_output = (1, 2, 3, 4, 5, 6)
    result = union_elements(test_tup1, test_tup2)
    assert set(result) == set(expected_output)
    assert isinstance(result, tuple)

def test_union_some_overlapping_elements():
    # Union of two tuples with some overlapping elements
    test_tup1 = (1, 2, 3)
    test_tup2 = (3, 4, 5)
    expected_output = (1, 2, 3, 4, 5)
    result = union_elements(test_tup1, test_tup2)
    assert set(result) == set(expected_output)
    assert isinstance(result, tuple)

def test_union_one_empty_tuple():
    # Union of two tuples where one is empty
    test_tup1 = ()
    test_tup2 = (1, 2, 3)
    expected_output = (1, 2, 3)
    result = union_elements(test_tup1, test_tup2)
    assert set(result) == set(expected_output)
    assert isinstance(result, tuple)

def test_union_all_elements_overlapping():
    # Union of two tuples with all elements overlapping
    test_tup1 = (1, 1, 2)
    test_tup2 = (2, 1)
    expected_output = (1, 2)
    result = union_elements(test_tup1, test_tup2)
    assert set(result) == set(expected_output)
    assert isinstance(result, tuple)

def test_union_different_data_types():
    # Union of two tuples with different data types
    test_tup1 = (1, 'a', 3.0)
    test_tup2 = ('a', 4, 3.0)
    expected_output = (1, 'a', 3.0, 4)
    result = union_elements(test_tup1, test_tup2)
    assert set(result) == set(expected_output)
    assert isinstance(result, tuple)