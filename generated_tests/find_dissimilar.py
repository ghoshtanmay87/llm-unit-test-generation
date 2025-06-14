def find_dissimilar(test_tup1, test_tup2):
  res = tuple(set(test_tup1) ^ set(test_tup2))
  return (res)

import pytest

def test_find_dissimilar_some_common_some_unique():
    test_tup1 = (1, 2, 3)
    test_tup2 = (2, 3, 4)
    expected_output = (1, 4)
    result = find_dissimilar(test_tup1, test_tup2)
    assert set(result) == set(expected_output)

def test_find_dissimilar_identical_tuples():
    test_tup1 = (5, 5, 5)
    test_tup2 = (5, 5)
    expected_output = ()
    result = find_dissimilar(test_tup1, test_tup2)
    assert result == expected_output

def test_find_dissimilar_one_empty_tuple():
    test_tup1 = ()
    test_tup2 = (1, 2, 3)
    expected_output = (1, 2, 3)
    result = find_dissimilar(test_tup1, test_tup2)
    assert set(result) == set(expected_output)

def test_find_dissimilar_no_common_elements():
    test_tup1 = (7, 8)
    test_tup2 = (9, 10)
    expected_output = (8, 9, 10, 7)
    result = find_dissimilar(test_tup1, test_tup2)
    assert set(result) == set(expected_output)

def test_find_dissimilar_tuples_with_strings():
    test_tup1 = ('apple', 'banana')
    test_tup2 = ('banana', 'cherry')
    expected_output = ('apple', 'cherry')
    result = find_dissimilar(test_tup1, test_tup2)
    assert set(result) == set(expected_output)