def does_Contain_B(a,b,c): 
    if (a == b): 
        return True
    if ((b - a) * c > 0 and (b - a) % c == 0): 
        return True
    return False

import pytest

def test_a_equals_b_should_return_true_regardless_of_c():
    # Since a == b, the function returns True immediately.
    assert does_Contain_B(a=5, b=5, c=3) is True

def test_b_greater_than_a_c_positive_divisible_by_c_expected_false_in_story():
    # (b - a) = 6, which is positive and c=3 is positive,
    # but expected_output is False as per user story despite reasoning inconsistency.
    assert does_Contain_B(a=2, b=8, c=3) is False

def test_b_greater_than_a_c_positive_divisible_by_c_expected_true():
    # (b - a) = 6, which is positive and c=2 is positive,
    # and 6 % 2 == 0 is True, so the function returns True.
    assert does_Contain_B(a=2, b=8, c=2) is True

def test_b_less_than_a_c_negative_divisible_by_c():
    # (b - a) = -6, which is negative and c=-2 is negative,
    # and (-6) % (-2) == 0 is True, so the function returns True.
    assert does_Contain_B(a=10, b=4, c=-2) is True

def test_b_less_than_a_c_positive_no_divisibility():
    # (b - a) = -6, c=3 is positive,
    # so (b - a) * c = -18 < 0, condition fails, returns False.
    assert does_Contain_B(a=10, b=4, c=3) is False

def test_b_greater_than_a_c_negative_no_divisibility():
    # (b - a) = 6, c=-3 negative,
    # (b - a) * c = -18 < 0, condition fails, returns False.
    assert does_Contain_B(a=3, b=9, c=-3) is False

def test_b_equals_a_c_zero():
    # Since a == b, function returns True immediately, c value irrelevant.
    assert does_Contain_B(a=7, b=7, c=0) is True

def test_b_greater_than_a_c_zero_no_division_by_zero():
    # First condition fails (a != b).
    # Second condition: (b - a)*c = 3*0=0 not > 0, so returns False.
    # No division by zero error because modulo not evaluated.
    assert does_Contain_B(a=1, b=4, c=0) is False