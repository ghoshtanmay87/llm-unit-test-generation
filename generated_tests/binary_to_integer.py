def binary_to_integer(test_tup):
  res = int("".join(str(ele) for ele in test_tup), 2)
  return (str(res))

import pytest

def test_binary_to_integer_zero():
    # Convert a binary tuple representing zero
    test_tup = (0, 0, 0)
    expected_output = '0'
    assert binary_to_integer(test_tup) == expected_output

def test_binary_to_integer_one():
    # Convert a binary tuple representing one
    test_tup = (0, 0, 1)
    expected_output = '1'
    assert binary_to_integer(test_tup) == expected_output

def test_binary_to_integer_five():
    # Convert a binary tuple representing five
    test_tup = (1, 0, 1)
    expected_output = '5'
    assert binary_to_integer(test_tup) == expected_output

def test_binary_to_integer_fifteen():
    # Convert a binary tuple representing fifteen
    test_tup = (1, 1, 1, 1)
    expected_output = '15'
    assert binary_to_integer(test_tup) == expected_output

def test_binary_to_integer_two_hundred_fifty_five():
    # Convert a binary tuple representing two hundred and fifty-five
    test_tup = (1, 1, 1, 1, 1, 1, 1, 1)
    expected_output = '255'
    assert binary_to_integer(test_tup) == expected_output

def test_binary_to_integer_ten():
    # Convert a binary tuple representing the number ten
    test_tup = (1, 0, 1, 0)
    expected_output = '10'
    assert binary_to_integer(test_tup) == expected_output