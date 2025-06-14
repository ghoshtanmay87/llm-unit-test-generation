def sum_nums(x, y,m,n):
    sum_nums= x + y
    if sum_nums in range(m, n):
        return 20
    else:
        return sum_nums

import pytest

def test_sum_within_range_returns_20():
    # Sum of x and y is within the range [m, n) and returns 20
    result = sum_nums(x=5, y=10, m=10, n=20)
    assert result == 20

def test_sum_equal_to_lower_bound_returns_20():
    # Sum of x and y is equal to the lower bound m and returns 20
    result = sum_nums(x=7, y=3, m=10, n=15)
    assert result == 20

def test_sum_equal_to_upper_bound_returns_sum():
    # Sum of x and y is equal to the upper bound n and returns sum
    result = sum_nums(x=10, y=10, m=5, n=20)
    assert result == 20

def test_sum_less_than_lower_bound_returns_sum():
    # Sum of x and y is less than m and returns sum
    result = sum_nums(x=2, y=3, m=10, n=15)
    assert result == 5

def test_sum_greater_than_or_equal_to_upper_bound_returns_sum():
    # Sum of x and y is greater than or equal to n and returns sum
    result = sum_nums(x=15, y=10, m=5, n=20)
    assert result == 25