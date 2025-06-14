def bitwise_xor(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res)

import pytest

def test_xor_two_tuples_equal_length_simple_integers():
    test_tup1 = (1, 2, 3)
    test_tup2 = (4, 5, 6)
    expected_output = (5, 7, 5)
    assert bitwise_xor(test_tup1, test_tup2) == expected_output

def test_xor_two_tuples_with_zeros():
    test_tup1 = (0, 0, 0)
    test_tup2 = (0, 0, 0)
    expected_output = (0, 0, 0)
    assert bitwise_xor(test_tup1, test_tup2) == expected_output

def test_xor_two_tuples_one_element_each():
    test_tup1 = (255,)
    test_tup2 = (128,)
    expected_output = (127,)
    assert bitwise_xor(test_tup1, test_tup2) == expected_output

def test_xor_two_tuples_different_values_length_4():
    test_tup1 = (10, 20, 30, 40)
    test_tup2 = (1, 2, 3, 4)
    expected_output = (11, 22, 29, 44)
    assert bitwise_xor(test_tup1, test_tup2) == expected_output

def test_xor_two_tuples_one_with_larger_numbers():
    test_tup1 = (1023, 512, 256)
    test_tup2 = (511, 256, 128)
    expected_output = (512, 768, 384)
    assert bitwise_xor(test_tup1, test_tup2) == expected_output

def test_xor_two_tuples_with_negative_numbers():
    test_tup1 = (-1, -2, -3)
    test_tup2 = (-4, -5, -6)
    expected_output = (3, 7, 5)
    assert bitwise_xor(test_tup1, test_tup2) == expected_output

def test_xor_two_empty_tuples():
    test_tup1 = ()
    test_tup2 = ()
    expected_output = ()
    assert bitwise_xor(test_tup1, test_tup2) == expected_output