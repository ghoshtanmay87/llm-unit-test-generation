def ap_sum(a,n,d):
  total = (n * (2 * a + (n - 1) * d)) / 2
  return total

import pytest

def test_sum_first_5_terms_ap_start_1_diff_1():
    # Sum of first 5 terms of an AP starting at 1 with common difference 1
    result = ap_sum(a=1, n=5, d=1)
    assert result == 15.0

def test_sum_first_4_terms_ap_start_3_diff_2_corrected():
    # Sum of first 4 terms of an AP starting at 3 with common difference 2 (corrected)
    result = ap_sum(a=3, n=4, d=2)
    assert result == 24.0

def test_sum_first_1_term_ap_start_10_diff_5():
    # Sum of first 1 term of an AP starting at 10 with common difference 5
    result = ap_sum(a=10, n=1, d=5)
    assert result == 10.0

def test_sum_first_0_terms_ap_start_5_diff_3():
    # Sum of first 0 terms of an AP starting at 5 with common difference 3
    result = ap_sum(a=5, n=0, d=3)
    assert result == 0.0

def test_sum_first_3_terms_ap_start_0_diff_0():
    # Sum of first 3 terms of an AP starting at 0 with common difference 0
    result = ap_sum(a=0, n=3, d=0)
    assert result == 0.0

def test_sum_first_6_terms_ap_start_neg2_diff_3_corrected():
    # Sum of first 6 terms of an AP starting at -2 with common difference 3 (corrected)
    result = ap_sum(a=-2, n=6, d=3)
    assert result == 33.0