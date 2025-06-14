def divisible_by_digits(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]

import pytest

def test_check_range_with_single_number_divisible_by_its_digits():
    startnum = 1
    endnum = 10
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert divisible_by_digits(startnum, endnum) == expected_output

def test_check_range_including_number_with_zero_digit():
    startnum = 10
    endnum = 15
    expected_output = [11, 12, 15]
    assert divisible_by_digits(startnum, endnum) == expected_output

def test_check_range_with_multi_digit_numbers_all_divisible_by_their_digits():
    startnum = 22
    endnum = 25
    expected_output = [22, 24]
    assert divisible_by_digits(startnum, endnum) == expected_output

def test_check_range_with_numbers_containing_zero_digit():
    startnum = 100
    endnum = 105
    expected_output = []
    assert divisible_by_digits(startnum, endnum) == expected_output

def test_check_range_with_no_valid_numbers():
    startnum = 30
    endnum = 32
    expected_output = []
    assert divisible_by_digits(startnum, endnum) == expected_output

def test_check_range_with_larger_numbers():
    startnum = 120
    endnum = 130
    expected_output = [122, 124, 126, 128]
    assert divisible_by_digits(startnum, endnum) == expected_output