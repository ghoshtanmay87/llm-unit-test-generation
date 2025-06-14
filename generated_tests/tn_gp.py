import math
def tn_gp(a,n,r):
  tn = a * (math.pow(r, n - 1))
  return tn

import pytest

def test_term_positive_integer_n_r_greater_than_one():
    # Calculate the term of a geometric progression with positive integer n and r > 1
    a = 2
    n = 4
    r = 3
    expected = 54.0
    result = tn_gp(a, n, r)
    assert result == expected

def test_term_first_term_n_equals_one():
    # Calculate the first term of a geometric progression (n=1)
    a = 5
    n = 1
    r = 10
    expected = 5.0
    result = tn_gp(a, n, r)
    assert result == expected

def test_term_fractional_common_ratio_less_than_one():
    # Calculate the term with fractional common ratio r < 1
    a = 8
    n = 3
    r = 0.5
    expected = 2.0
    result = tn_gp(a, n, r)
    assert result == expected

def test_term_negative_common_ratio():
    # Calculate the term with negative common ratio
    a = 3
    n = 5
    r = -2
    expected = -48.0
    result = tn_gp(a, n, r)
    assert result == expected

def test_term_n_equals_two_r_equals_one():
    # Calculate the term with n=2 and r=1 (common ratio 1)
    a = 7
    n = 2
    r = 1
    expected = 7.0
    result = tn_gp(a, n, r)
    assert result == expected