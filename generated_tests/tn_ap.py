def tn_ap(a,n,d):
  tn = a + (n - 1) * d
  return tn

import pytest

def test_calculate_first_term_of_arithmetic_progression():
    # For n=1, the term is the first term itself, so tn = a + (1-1)*d = 5 + 0 = 5.
    result = tn_ap(a=5, n=1, d=3)
    assert result == 5

def test_calculate_fifth_term_with_positive_common_difference():
    # tn = a + (n-1)*d = 2 + (5-1)*4 = 2 + 16 = 18.
    result = tn_ap(a=2, n=5, d=4)
    assert result == 18

def test_calculate_third_term_with_negative_common_difference():
    # tn = 10 + (3-1)*(-2) = 10 + 2*(-2) = 10 - 4 = 6.
    result = tn_ap(a=10, n=3, d=-2)
    assert result == 6

def test_calculate_tenth_term_with_zero_common_difference():
    # With d=0, all terms are equal to a, so tn = 7 + (10-1)*0 = 7.
    result = tn_ap(a=7, n=10, d=0)
    assert result == 7

def test_calculate_fourth_term_with_floating_point_values():
    # tn = 1.5 + (4-1)*0.5 = 1.5 + 3*0.5 = 1.5 + 1.5 = 3.0.
    result = tn_ap(a=1.5, n=4, d=0.5)
    assert result == 3.0