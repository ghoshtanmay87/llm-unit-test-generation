def front_and_rear(test_tup):
  res = (test_tup[0], test_tup[-1])
  return (res)

import pytest

def test_front_and_rear_multiple_elements():
    # Input tuple with multiple elements
    test_tup = (1, 2, 3, 4, 5)
    expected_output = (1, 5)
    assert front_and_rear(test_tup) == expected_output

def test_front_and_rear_two_elements():
    # Input tuple with two elements
    test_tup = (10, 20)
    expected_output = (10, 20)
    assert front_and_rear(test_tup) == expected_output

def test_front_and_rear_single_element():
    # Input tuple with one element
    test_tup = (42,)
    expected_output = (42, 42)
    assert front_and_rear(test_tup) == expected_output

def test_front_and_rear_strings():
    # Input tuple with strings
    test_tup = ('apple', 'banana', 'cherry')
    expected_output = ('apple', 'cherry')
    assert front_and_rear(test_tup) == expected_output

def test_front_and_rear_mixed_types():
    # Input tuple with mixed types
    test_tup = (True, 3.14, 'end')
    expected_output = (True, 'end')
    assert front_and_rear(test_tup) == expected_output