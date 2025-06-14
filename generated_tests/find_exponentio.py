def find_exponentio(test_tup1, test_tup2):
  res = tuple(ele1 ** ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res)

import pytest

def test_elementwise_exponentiation_positive_integers():
    test_tup1 = (2, 3, 4)
    test_tup2 = (3, 2, 1)
    expected_output = (8, 9, 4)
    assert find_exponentio(test_tup1, test_tup2) == expected_output

def test_elementwise_exponentiation_zero_exponent():
    test_tup1 = (5, 10, 7)
    test_tup2 = (0, 0, 0)
    expected_output = (1, 1, 1)
    assert find_exponentio(test_tup1, test_tup2) == expected_output

def test_elementwise_exponentiation_zero_base_and_exponent():
    test_tup1 = (0, 0, 0)
    test_tup2 = (0, 1, 2)
    expected_output = (1, 0, 0)
    assert find_exponentio(test_tup1, test_tup2) == expected_output

def test_elementwise_exponentiation_negative_exponents():
    test_tup1 = (2, 4, 8)
    test_tup2 = (-1, -2, -3)
    expected_output = (0.5, 0.0625, 0.001953125)
    assert find_exponentio(test_tup1, test_tup2) == expected_output

def test_elementwise_exponentiation_mixed_bases_and_exponents():
    test_tup1 = (-2, 3, -4)
    test_tup2 = (3, 0, 2)
    expected_output = (-8, 1, 16)
    assert find_exponentio(test_tup1, test_tup2) == expected_output