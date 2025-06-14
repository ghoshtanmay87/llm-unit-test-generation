def combinations_list(list1):
    if len(list1) == 0:
        return [[]]
    result = []
    for el in combinations_list(list1[1:]):
        result += [el, el+[list1[0]]]
    return result

import pytest

def test_empty_input_returns_list_with_empty_list():
    # scenario: Empty input list returns list with empty list
    input_list = []
    expected = [[]]
    assert combinations_list(input_list) == expected

def test_single_element_list_returns_empty_and_single_element_subsets():
    # scenario: Single element list returns empty subset and subset with that element
    input_list = [5]
    expected = [[], [5]]
    assert combinations_list(input_list) == expected

def test_two_elements_list_returns_all_subsets_including_empty_and_pairs():
    # scenario: Two elements list returns all subsets including empty, single elements, and both elements
    input_list = [1, 2]
    expected = [[], [1], [2], [2, 1]]
    assert combinations_list(input_list) == expected

def test_three_elements_list_returns_all_subsets_including_triplet():
    # scenario: Three elements list returns all subsets including empty, single, pairs, and triplet
    input_list = [1, 2, 3]
    expected = [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
    assert combinations_list(input_list) == expected

def test_list_with_repeated_elements_returns_all_subsets_including_duplicates():
    # scenario: List with repeated elements returns all subsets including duplicates
    input_list = [1, 1]
    expected = [[], [1], [1], [1, 1]]
    assert combinations_list(input_list) == expected