import math
def sum_gp(a,n,r):
 total = (a * (1 - math.pow(r, n ))) / (1- r)
 return total

import pytest

def test_sum_gp_first_5_terms_a2_r3():
    # Sum of first 5 terms of a geometric progression with a=2, r=3
    result = sum_gp(a=2, n=5, r=3)
    assert result == 242.0

def test_sum_gp_first_4_terms_a1_r05():
    # Sum of first 4 terms with a=1, r=0.5
    result = sum_gp(a=1, n=4, r=0.5)
    assert result == 1.875

def test_sum_gp_r_equals_1_edge_case():
    # Sum of first 3 terms with a=5, r=1 (edge case where r=1)
    # The function will raise ZeroDivisionError due to division by zero
    with pytest.raises(ZeroDivisionError):
        sum_gp(a=5, n=3, r=1)

def test_sum_gp_first_1_term_a10_r2():
    # Sum of first 1 term with a=10, r=2
    result = sum_gp(a=10, n=1, r=2)
    assert result == 10.0

def test_sum_gp_zero_terms_n0():
    # Sum of first 0 terms with a=3, r=4 (n=0 edge case)
    result = sum_gp(a=3, n=0, r=4)
    assert result == 0.0