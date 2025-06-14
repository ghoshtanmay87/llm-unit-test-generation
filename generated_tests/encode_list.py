from itertools import groupby
def encode_list(list1):
    return [[len(list(group)), key] for key, group in groupby(list1)]

import pytest

def test_encode_list_consecutive_repeated_elements():
    # Encoding a list with consecutive repeated elements
    input_list = [1, 1, 2, 2, 2, 3]
    expected = [[2, 1], [3, 2], [1, 3]]
    assert encode_list(input_list) == expected

def test_encode_list_no_repeated_consecutive_elements():
    # Encoding a list with no repeated consecutive elements
    input_list = [4, 5, 6]
    expected = [[1, 4], [1, 5], [1, 6]]
    assert encode_list(input_list) == expected

def test_encode_list_empty_list():
    # Encoding an empty list
    input_list = []
    expected = []
    assert encode_list(input_list) == expected

def test_encode_list_all_elements_same():
    # Encoding a list with all elements the same
    input_list = [7, 7, 7, 7]
    expected = [[4, 7]]
    assert encode_list(input_list) == expected

def test_encode_list_alternating_elements():
    # Encoding a list with alternating elements
    input_list = [1, 2, 1, 2, 1, 2]
    expected = [[1, 1], [1, 2], [1, 1], [1, 2], [1, 1], [1, 2]]
    assert encode_list(input_list) == expected