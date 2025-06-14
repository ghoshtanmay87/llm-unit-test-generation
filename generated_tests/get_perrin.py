def get_perrin(n):
  if (n == 0):
    return 3
  if (n == 1):
    return 0
  if (n == 2):
    return 2 
  return get_perrin(n - 2) + get_perrin(n - 3)

import pytest

def test_perrin_number_n_0():
    # Calculate Perrin number for n=0 (base case)
    result = get_perrin(0)
    assert result == 3

def test_perrin_number_n_1():
    # Calculate Perrin number for n=1 (base case)
    result = get_perrin(1)
    assert result == 0

def test_perrin_number_n_2():
    # Calculate Perrin number for n=2 (base case)
    result = get_perrin(2)
    assert result == 2

def test_perrin_number_n_3():
    # Calculate Perrin number for n=3 (recursive case)
    result = get_perrin(3)
    assert result == 3

def test_perrin_number_n_4():
    # Calculate Perrin number for n=4 (recursive case)
    result = get_perrin(4)
    assert result == 2

def test_perrin_number_n_5():
    # Calculate Perrin number for n=5 (recursive case)
    result = get_perrin(5)
    assert result == 5

def test_perrin_number_n_6():
    # Calculate Perrin number for n=6 (recursive case)
    result = get_perrin(6)
    assert result == 5

def test_perrin_number_n_7():
    # Calculate Perrin number for n=7 (recursive case)
    result = get_perrin(7)
    assert result == 7