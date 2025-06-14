def add_pairwise(test_tup):
  res = tuple(i + j for i, j in zip(test_tup, test_tup[1:]))
  return (res)

import pytest

def test_add_pairwise_positive_integers():
    # Adding consecutive pairs in a tuple of positive integers
    test_tup = (1, 2, 3, 4)
    expected_output = (3, 5, 7)
    assert add_pairwise(test_tup) == expected_output

def test_add_pairwise_negative_and_positive_integers():
    # Adding consecutive pairs in a tuple with negative and positive integers
    test_tup = (-1, 0, 1)
    expected_output = (-1, 1)
    assert add_pairwise(test_tup) == expected_output

def test_add_pairwise_single_element():
    # Adding consecutive pairs in a tuple with a single element
    test_tup = (5,)
    expected_output = ()
    assert add_pairwise(test_tup) == expected_output

def test_add_pairwise_empty_tuple():
    # Adding consecutive pairs in an empty tuple
    test_tup = ()
    expected_output = ()
    assert add_pairwise(test_tup) == expected_output

def test_add_pairwise_floats():
    # Adding consecutive pairs in a tuple with floating point numbers
    test_tup = (1.5, 2.5, 3.0)
    expected_output = (4.0, 5.5)
    assert add_pairwise(test_tup) == expected_output

def test_add_pairwise_zeros():
    # Adding consecutive pairs in a tuple with zeros
    test_tup = (0, 0, 0)
    expected_output = (0, 0)
    assert add_pairwise(test_tup) == expected_output