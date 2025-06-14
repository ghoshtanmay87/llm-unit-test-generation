def even_num(x):
  if x%2==0:
     return True
  else:
    return False

import pytest

def test_even_num_with_even_positive_integer():
    # Input is an even positive integer
    x = 4
    expected = True
    assert even_num(x) == expected

def test_even_num_with_odd_positive_integer():
    # Input is an odd positive integer
    x = 7
    expected = False
    assert even_num(x) == expected

def test_even_num_with_zero():
    # Input is zero
    x = 0
    expected = True
    assert even_num(x) == expected

def test_even_num_with_negative_even_integer():
    # Input is a negative even integer
    x = -8
    expected = True
    assert even_num(x) == expected

def test_even_num_with_negative_odd_integer():
    # Input is a negative odd integer
    x = -3
    expected = False
    assert even_num(x) == expected