def add_elements(arr, k):
    return sum((elem for elem in arr[:k] if len(str(elem)) <= 2))

import pytest

def test_sum_first_k_elements_all_length_le_2():
    # Scenario: Sum first k elements where all elements have string length <= 2
    arr = [10, 20, 30, 40]
    k = 3
    expected = 60
    assert add_elements(arr, k) == expected

def test_sum_first_k_elements_some_length_gt_2():
    # Scenario: Sum first k elements with some elements having string length > 2
    arr = [5, 123, 45, 9]
    k = 4
    expected = 59
    assert add_elements(arr, k) == expected

def test_sum_first_k_elements_k_zero():
    # Scenario: Sum first k elements when k is zero
    arr = [1, 2, 3]
    k = 0
    expected = 0
    assert add_elements(arr, k) == expected

def test_sum_first_k_elements_k_exceeds_length():
    # Scenario: Sum first k elements when k exceeds array length
    arr = [7, 88, 999, 10]
    k = 10
    expected = 105
    assert add_elements(arr, k) == expected

def test_sum_first_k_elements_empty_array():
    # Scenario: Sum first k elements with empty array
    arr = []
    k = 5
    expected = 0
    assert add_elements(arr, k) == expected

def test_sum_first_k_elements_elements_as_strings_integers():
    # Scenario: Sum first k elements with elements as strings (should be integers as per function usage)
    arr = [1, 2, 3]
    k = 2
    expected = 3
    assert add_elements(arr, k) == expected

def test_sum_first_k_elements_length_exactly_2():
    # Scenario: Sum first k elements with elements having string length exactly 2
    arr = [9, 10, 99, 100]
    k = 4
    expected = 118
    assert add_elements(arr, k) == expected

def test_sum_first_k_elements_negative_numbers_length_check():
    # Scenario: Sum first k elements with negative numbers and string length check
    arr = [-1, -22, -333, 44]
    k = 4
    expected = 43
    assert add_elements(arr, k) == expected