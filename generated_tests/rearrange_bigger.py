def rearrange_bigger(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False

import pytest

def test_next_bigger_number_exists():
    # Find next bigger number by rearranging digits when a bigger permutation exists
    n = 12
    expected = 21
    assert rearrange_bigger(n) == expected

def test_no_bigger_permutation_descending_order():
    # Return False when digits are in descending order (no bigger permutation)
    n = 21
    expected = False
    assert rearrange_bigger(n) == expected

def test_next_bigger_number_with_repeated_digits():
    # Find next bigger number for a multi-digit number with repeated digits
    n = 513
    expected = 531
    assert rearrange_bigger(n) == expected

def test_next_bigger_number_multiple_digits_rearrangement():
    # Find next bigger number when multiple digits need rearrangement
    n = 2017
    expected = 2071
    assert rearrange_bigger(n) == expected

def test_no_bigger_permutation_all_digits_equal():
    # Return False when all digits are equal
    n = 1111
    expected = False
    assert rearrange_bigger(n) == expected

def test_next_bigger_number_mixed_order_digits():
    # Find next bigger number with digits in mixed order
    n = 1234
    expected = 1243
    assert rearrange_bigger(n) == expected

def test_next_bigger_number_last_two_digits_swapped():
    # Find next bigger number when last two digits can be swapped
    n = 534976
    expected = 536479
    assert rearrange_bigger(n) == expected