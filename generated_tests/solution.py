def solution(lst):
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])

import pytest

def test_sum_of_odd_numbers_at_even_indices_in_mixed_list():
    lst = [1, 2, 3, 4, 5, 6]
    expected = 9
    assert solution(lst) == expected

def test_list_with_no_odd_numbers_at_even_indices():
    lst = [2, 3, 4, 5, 6, 7]
    expected = 0
    assert solution(lst) == expected

def test_empty_list_input():
    lst = []
    expected = 0
    assert solution(lst) == expected

def test_all_odd_numbers_at_even_indices():
    lst = [7, 2, 9, 4, 11, 6]
    expected = 27
    assert solution(lst) == expected

def test_all_even_numbers_at_even_indices():
    lst = [8, 1, 4, 3, 6, 5]
    expected = 0
    assert solution(lst) == expected

def test_single_element_list_with_odd_number():
    lst = [5]
    expected = 5
    assert solution(lst) == expected

def test_single_element_list_with_even_number():
    lst = [4]
    expected = 0
    assert solution(lst) == expected

def test_list_with_negative_odd_numbers_at_even_indices():
    lst = [-1, 2, -3, 4, -5, 6]
    expected = -9
    assert solution(lst) == expected

def test_list_with_zero_and_odd_numbers_at_even_indices():
    lst = [0, 1, 3, 5, 0, 7]
    expected = 3
    assert solution(lst) == expected

def test_long_list_with_mixed_values():
    lst = [10, 11, 13, 14, 15, 16, 17, 18, 19, 20]
    expected = 64
    assert solution(lst) == expected