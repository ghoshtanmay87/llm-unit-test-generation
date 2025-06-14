def div_of_nums(nums,m,n):
 result = list(filter(lambda x: (x % m == 0 and x % n == 0), nums)) 
 return result

import pytest

def test_divisible_by_2_and_3_in_mixed_list():
    nums = [1, 2, 3, 4, 5, 6, 12, 18, 20]
    m = 2
    n = 3
    expected = [6, 12, 18]
    assert div_of_nums(nums, m, n) == expected

def test_divisible_by_5_and_10_in_list():
    nums = [10, 15, 20, 25, 30, 40]
    m = 5
    n = 10
    expected = [10, 20, 30, 40]
    assert div_of_nums(nums, m, n) == expected

def test_no_numbers_divisible_by_7_and_11():
    nums = [1, 2, 3, 4, 5, 6]
    m = 7
    n = 11
    expected = []
    assert div_of_nums(nums, m, n) == expected

def test_all_numbers_divisible_by_1_and_1():
    nums = [7, 14, 21]
    m = 1
    n = 1
    expected = [7, 14, 21]
    assert div_of_nums(nums, m, n) == expected

def test_empty_input_list_returns_empty():
    nums = []
    m = 3
    n = 4
    expected = []
    assert div_of_nums(nums, m, n) == expected

def test_divisible_by_4_and_6_in_list():
    nums = [12, 24, 36, 48, 50]
    m = 4
    n = 6
    expected = [12, 24, 36, 48]
    assert div_of_nums(nums, m, n) == expected