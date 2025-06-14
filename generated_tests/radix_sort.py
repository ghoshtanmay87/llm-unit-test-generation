def radix_sort(nums):
    RADIX = 10
    placement = 1
    max_digit = max(nums)

    while placement < max_digit:
      buckets = [list() for _ in range( RADIX )]
      for i in nums:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          nums[a] = i
          a += 1
      placement *= RADIX
    return nums

import pytest

def test_sort_single_digit_numbers():
    # Scenario: Sort a list of single-digit numbers
    input_nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert radix_sort(input_nums) == expected

def test_sort_multiple_digits_tens_and_units():
    # Scenario: Sort a list with multiple digits including tens and units
    input_nums = [170, 45, 75, 90, 802, 24, 2, 66]
    expected = [2, 24, 45, 66, 75, 90, 170, 802]
    assert radix_sort(input_nums) == expected

def test_sort_list_with_repeated_numbers():
    # Scenario: Sort a list with repeated numbers
    input_nums = [5, 3, 8, 3, 9, 1, 5]
    expected = [1, 3, 3, 5, 5, 8, 9]
    assert radix_sort(input_nums) == expected

def test_sort_single_element_list():
    # Scenario: Sort a list with a single element
    input_nums = [42]
    expected = [42]
    assert radix_sort(input_nums) == expected

def test_sort_numbers_with_different_digit_lengths():
    # Scenario: Sort a list with numbers having different digit lengths
    input_nums = [1, 22, 333, 44, 5]
    expected = [1, 5, 22, 44, 333]
    assert radix_sort(input_nums) == expected