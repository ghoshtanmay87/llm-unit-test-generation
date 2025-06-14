from itertools import groupby 
def extract_elements(numbers, n):
    result = [i for i, j in groupby(numbers) if len(list(j)) == n] 
    return result

import pytest

def test_extract_elements_appear_exactly_twice_consecutively():
    numbers = [1, 1, 2, 3, 3, 4, 4, 4]
    n = 2
    expected_output = [1, 3]
    assert extract_elements(numbers, n) == expected_output

def test_extract_elements_appear_exactly_once_consecutively():
    numbers = [5, 5, 6, 7, 7, 8]
    n = 1
    expected_output = [6, 8]
    assert extract_elements(numbers, n) == expected_output

def test_extract_elements_appear_exactly_three_times_consecutively():
    numbers = [9, 9, 9, 10, 10, 11, 11, 11, 11]
    n = 3
    expected_output = [9]
    assert extract_elements(numbers, n) == expected_output

def test_no_elements_appear_exactly_four_times_consecutively():
    numbers = [1, 1, 2, 2, 3, 3]
    n = 4
    expected_output = []
    assert extract_elements(numbers, n) == expected_output

def test_extract_elements_appear_exactly_once_in_mixed_list():
    numbers = [4, 5, 5, 6, 7, 7, 7, 8]
    n = 1
    expected_output = [4, 6, 8]
    assert extract_elements(numbers, n) == expected_output