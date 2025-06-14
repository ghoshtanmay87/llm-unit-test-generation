def similar_elements(test_tup1, test_tup2):
  res = tuple(set(test_tup1) & set(test_tup2))
  return (res)

import pytest

def test_common_elements_some_overlap():
    # Find common elements between two tuples with some overlap
    test_tup1 = (1, 2, 3, 4)
    test_tup2 = (3, 4, 5, 6)
    expected_output = (3, 4)
    assert similar_elements(test_tup1, test_tup2) == expected_output

def test_common_elements_no_overlap():
    # Find common elements when tuples have no overlap
    test_tup1 = (1, 2)
    test_tup2 = (3, 4)
    expected_output = ()
    assert similar_elements(test_tup1, test_tup2) == expected_output

def test_common_elements_one_empty_tuple():
    # Find common elements when one tuple is empty
    test_tup1 = ()
    test_tup2 = (1, 2, 3)
    expected_output = ()
    assert similar_elements(test_tup1, test_tup2) == expected_output

def test_common_elements_identical_tuples():
    # Find common elements when both tuples are identical
    test_tup1 = (7, 8, 9)
    test_tup2 = (7, 8, 9)
    expected_output = (8, 9, 7)
    assert similar_elements(test_tup1, test_tup2) == expected_output

def test_common_elements_repeated_elements():
    # Find common elements with repeated elements in tuples
    test_tup1 = (1, 2, 2, 3)
    test_tup2 = (2, 2, 4)
    expected_output = (2,)
    assert similar_elements(test_tup1, test_tup2) == expected_output