def ntimes_list(nums,n):
    result = map(lambda x:n*x, nums) 
    return list(result)

import pytest

def test_multiply_positive_integers_by_positive_integer():
    # Each element in [1, 2, 3] is multiplied by 3, resulting in [3, 6, 9].
    assert ntimes_list([1, 2, 3], 3) == [3, 6, 9]

def test_multiply_positive_integers_by_zero():
    # Multiplying any number by zero results in zero, so all elements become 0.
    assert ntimes_list([4, 5, 6], 0) == [0, 0, 0]

def test_multiply_negative_and_positive_integers_by_negative_integer():
    # Each element is multiplied by -2: -1*-2=2, 0*-2=0, 1*-2=-2.
    assert ntimes_list([-1, 0, 1], -2) == [2, 0, -2]

def test_multiply_empty_list_by_any_integer():
    # An empty list multiplied by any number remains an empty list.
    assert ntimes_list([], 5) == []

def test_multiply_floats_by_float():
    # Each float element is multiplied by 2.0, resulting in [3.0, 4.0, 7.0].
    assert ntimes_list([1.5, 2.0, 3.5], 2.0) == [3.0, 4.0, 7.0]