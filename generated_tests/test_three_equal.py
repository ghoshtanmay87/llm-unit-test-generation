def test_three_equal(x,y,z):
  result= set([x,y,z])
  if len(result)==3:
    return 0
  else:
    return (4-len(result))

import pytest

def test_all_three_inputs_distinct_integers():
    # All three inputs are distinct
    assert test_three_equal(1, 2, 3) == 0

def test_two_inputs_equal_one_different_integers():
    # Two inputs are equal, one is different
    assert test_three_equal(5, 5, 7) == 2

def test_two_inputs_equal_one_different_integers_different_order():
    # Two inputs are equal, one is different (different order)
    assert test_three_equal(10, 20, 10) == 2

def test_all_three_inputs_equal_integers():
    # All three inputs are equal
    assert test_three_equal(3, 3, 3) == 3

def test_two_inputs_equal_one_different_strings():
    # Two inputs equal, one different (strings)
    assert test_three_equal('a', 'a', 'b') == 2

def test_all_three_inputs_distinct_strings():
    # All three inputs distinct (strings)
    assert test_three_equal('x', 'y', 'z') == 0