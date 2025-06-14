def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

import pytest

def test_sort_even_even_length_list():
    # Sort even-indexed elements and interleave with odd-indexed elements for even-length list
    input_list = [4, 3, 2, 1]
    expected = [2, 3, 4, 1]
    assert sort_even(input_list) == expected

def test_sort_even_odd_length_list():
    # Sort even-indexed elements and interleave with odd-indexed elements for odd-length list
    input_list = [5, 7, 3, 9, 1]
    expected = [1, 7, 3, 9, 5]
    assert sort_even(input_list) == expected

def test_sort_even_single_element_list():
    # Single element list returns the same single element
    input_list = [10]
    expected = [10]
    assert sort_even(input_list) == expected

def test_sort_even_empty_list():
    # Empty list returns empty list
    input_list = []
    expected = []
    assert sort_even(input_list) == expected

def test_sort_even_two_elements_list():
    # List with two elements swaps even elements if needed
    input_list = [8, 6]
    expected = [8, 6]
    assert sort_even(input_list) == expected

def test_sort_even_three_elements_list():
    # List with three elements sorts evens and appends last even
    input_list = [9, 4, 7]
    expected = [7, 4, 9]
    assert sort_even(input_list) == expected

def test_sort_even_all_even_index_elements_equal():
    # List with all even-indexed elements equal
    input_list = [2, 5, 2, 3, 2]
    expected = [2, 5, 2, 3, 2]
    assert sort_even(input_list) == expected