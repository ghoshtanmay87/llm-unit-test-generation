def geometric_sum(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)

import pytest

def test_geometric_sum_n_zero():
    # Calculate geometric sum for n = 0
    result = geometric_sum(0)
    assert result == 1.0

def test_geometric_sum_n_one():
    # Calculate geometric sum for n = 1
    result = geometric_sum(1)
    assert result == 1.5

def test_geometric_sum_n_two():
    # Calculate geometric sum for n = 2
    result = geometric_sum(2)
    assert result == 1.75

def test_geometric_sum_n_three():
    # Calculate geometric sum for n = 3
    result = geometric_sum(3)
    assert result == 1.875

def test_geometric_sum_negative_n():
    # Calculate geometric sum for negative n = -1
    result = geometric_sum(-1)
    assert result == 0

def test_geometric_sum_n_four():
    # Calculate geometric sum for n = 4
    result = geometric_sum(4)
    assert result == 1.9375