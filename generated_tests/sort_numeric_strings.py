def sort_numeric_strings(nums_str):
    result = [int(x) for x in nums_str]
    result.sort()
    return result

import pytest

def test_sort_positive_integer_strings():
    # Sort a list of numeric strings representing positive integers
    input_data = ['3', '1', '2']
    expected = [1, 2, 3]
    assert sort_numeric_strings(input_data) == expected

def test_sort_numeric_strings_multiple_digits():
    # Sort a list of numeric strings with multiple digits
    input_data = ['10', '2', '30']
    expected = [2, 10, 30]
    assert sort_numeric_strings(input_data) == expected

def test_sort_numeric_strings_including_zero():
    # Sort a list of numeric strings including zero
    input_data = ['0', '5', '3']
    expected = [0, 3, 5]
    assert sort_numeric_strings(input_data) == expected

def test_sort_empty_list():
    # Sort an empty list
    input_data = []
    expected = []
    assert sort_numeric_strings(input_data) == expected

def test_sort_numeric_strings_with_negative_numbers():
    # Sort a list of numeric strings with negative numbers
    input_data = ['-1', '2', '-3']
    expected = [-3, -1, 2]
    assert sort_numeric_strings(input_data) == expected

def test_sort_numeric_strings_with_duplicates():
    # Sort a list of numeric strings with duplicates
    input_data = ['4', '2', '4', '1']
    expected = [1, 2, 4, 4]
    assert sort_numeric_strings(input_data) == expected