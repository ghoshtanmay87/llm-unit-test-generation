def tuple_to_int(nums):
    result = int(''.join(map(str,nums)))
    return result

import pytest

def test_convert_single_digit_tuple_to_int():
    # Convert a tuple of single-digit integers to an integer
    nums = (1, 2, 3)
    expected_output = 123
    assert tuple_to_int(nums) == expected_output

def test_convert_multiple_digits_elements_tuple_to_int():
    # Convert a tuple with multiple digits in elements to an integer
    nums = (10, 20, 30)
    expected_output = 102030
    assert tuple_to_int(nums) == expected_output

def test_convert_single_element_tuple_to_int():
    # Convert a tuple with a single element to an integer
    nums = (7,)
    expected_output = 7
    assert tuple_to_int(nums) == expected_output

def test_convert_zeros_and_single_digits_tuple_to_int():
    # Convert a tuple with zeros and single digits to an integer
    nums = (0, 4, 5)
    expected_output = 45
    assert tuple_to_int(nums) == expected_output