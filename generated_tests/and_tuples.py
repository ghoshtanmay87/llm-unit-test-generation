def and_tuples(test_tup1, test_tup2):
  res = tuple(ele1 & ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res)

import pytest

def test_and_tuples_positive_integers():
    # Bitwise AND of two tuples with positive integers
    test_tup1 = (5, 3, 12)
    test_tup2 = (3, 7, 10)
    expected_output = (1, 3, 8)
    assert and_tuples(test_tup1, test_tup2) == expected_output

def test_and_tuples_with_zeros():
    # Bitwise AND of two tuples with zeros
    test_tup1 = (0, 0, 0)
    test_tup2 = (1, 2, 3)
    expected_output = (0, 0, 0)
    assert and_tuples(test_tup1, test_tup2) == expected_output

def test_and_tuples_identical_elements():
    # Bitwise AND of two tuples with identical elements
    test_tup1 = (7, 7, 7)
    test_tup2 = (7, 7, 7)
    expected_output = (7, 7, 7)
    assert and_tuples(test_tup1, test_tup2) == expected_output

def test_and_tuples_mixed_bits():
    # Bitwise AND of two tuples with mixed bits
    test_tup1 = (15, 8, 4)
    test_tup2 = (1, 8, 7)
    expected_output = (1, 8, 4)
    assert and_tuples(test_tup1, test_tup2) == expected_output

def test_and_tuples_different_lengths():
    # Bitwise AND of two tuples with different lengths (only zipped pairs considered)
    test_tup1 = (1, 2, 3, 4)
    test_tup2 = (4, 3, 2)
    expected_output = (0, 2, 2)
    assert and_tuples(test_tup1, test_tup2) == expected_output