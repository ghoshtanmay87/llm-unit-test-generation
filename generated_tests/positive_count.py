from array import array
def positive_count(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x > 0:
            n1 += 1
        else:
          None
    return round(n1/n,2)

import pytest

def test_all_positive_numbers_in_list():
    # All 5 numbers are positive, ratio is 5/5 = 1.0
    result = positive_count([1, 2, 3, 4, 5])
    assert result == 1.0

def test_mixed_positive_and_negative_numbers():
    # 2 positive numbers out of 5, ratio is 2/5 = 0.4
    result = positive_count([-1, 2, -3, 4, 0])
    assert result == 0.4

def test_all_zero_and_negative_numbers():
    # No positive numbers, ratio is 0/4 = 0.0
    result = positive_count([0, -1, -2, -3])
    assert result == 0.0

def test_single_positive_number():
    # One positive number, ratio is 1/1 = 1.0
    result = positive_count([10])
    assert result == 1.0

def test_single_zero_number():
    # One zero number (not positive), ratio is 0/1 = 0.0
    result = positive_count([0])
    assert result == 0.0

def test_empty_list_input_raises_zero_division_error():
    # Empty list causes division by zero error
    with pytest.raises(ZeroDivisionError):
        positive_count([])