def smallest_change(arr):
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

import pytest

def test_array_already_palindrome():
    arr = [1, 2, 3, 2, 1]
    expected = 0
    assert smallest_change(arr) == expected

def test_array_one_mismatched_pair():
    arr = [1, 2, 3, 4, 1]
    expected = 1
    assert smallest_change(arr) == expected

def test_array_all_elements_different():
    arr = [1, 2, 3, 4, 5]
    expected = 2
    assert smallest_change(arr) == expected

def test_even_length_palindrome_array():
    arr = [1, 2, 2, 1]
    expected = 0
    assert smallest_change(arr) == expected

def test_even_length_array_with_mismatches():
    arr = [1, 3, 2, 1]
    expected = 1
    assert smallest_change(arr) == expected

def test_single_element_array():
    arr = [7]
    expected = 0
    assert smallest_change(arr) == expected

def test_empty_array():
    arr = []
    expected = 0
    assert smallest_change(arr) == expected

def test_array_two_different_elements():
    arr = [1, 2]
    expected = 1
    assert smallest_change(arr) == expected

def test_array_two_same_elements():
    arr = [5, 5]
    expected = 0
    assert smallest_change(arr) == expected

def test_long_palindrome_array():
    arr = [1, 3, 5, 7, 5, 3, 1]
    expected = 0
    assert smallest_change(arr) == expected

def test_long_array_multiple_mismatches():
    arr = [1, 3, 5, 7, 8, 3, 2]
    expected = 2
    assert smallest_change(arr) == expected