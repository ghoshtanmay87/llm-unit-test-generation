def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
    return count

import pytest

def test_count_numbers_greater_than_10_with_odd_first_and_last_digits():
    nums = [11, 13, 15, 17, 19]
    expected = 5
    assert specialFilter(nums) == expected

def test_numbers_greater_than_10_but_with_even_first_digit():
    nums = [20, 22, 24, 26, 28]
    expected = 0
    assert specialFilter(nums) == expected

def test_numbers_greater_than_10_with_odd_first_digit_but_even_last_digit():
    nums = [12, 14, 16, 18, 30]
    expected = 0
    assert specialFilter(nums) == expected

def test_mixed_numbers_with_some_matching_criteria():
    nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    expected = 5
    assert specialFilter(nums) == expected

def test_numbers_less_than_or_equal_to_10():
    nums = [1, 3, 5, 7, 9, 10]
    expected = 0
    assert specialFilter(nums) == expected

def test_empty_list_input():
    nums = []
    expected = 0
    assert specialFilter(nums) == expected

def test_numbers_with_odd_first_and_last_digits_but_not_greater_than_10():
    nums = [9, 7, 5, 3, 1]
    expected = 0
    assert specialFilter(nums) == expected

def test_large_numbers_with_odd_first_and_last_digits():
    nums = [13579, 97531, 12345, 54321]
    expected = 4
    assert specialFilter(nums) == expected

def test_numbers_with_odd_first_digit_and_odd_last_digit_all_greater_than_10():
    nums = [31, 51, 71, 91, 11]
    expected = 5
    assert specialFilter(nums) == expected