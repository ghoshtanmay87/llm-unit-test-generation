def frequency_lists(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data

import pytest

def test_frequency_lists_empty_input_list():
    # Scenario: Empty input list
    input_data = []
    expected = {}
    assert frequency_lists(input_data) == expected

def test_frequency_lists_single_sublist_with_unique_elements():
    # Scenario: Single sublist with unique elements
    input_data = [[1, 2, 3]]
    expected = {1: 1, 2: 1, 3: 1}
    assert frequency_lists(input_data) == expected

def test_frequency_lists_multiple_sublists_with_repeated_elements():
    # Scenario: Multiple sublists with repeated elements
    input_data = [[1, 2], [2, 3], [1, 1]]
    expected = {1: 3, 2: 2, 3: 1}
    assert frequency_lists(input_data) == expected

def test_frequency_lists_sublists_with_negative_and_zero_values():
    # Scenario: Sublists with negative and zero values
    input_data = [[0, -1, -1], [0, 2]]
    expected = {0: 2, -1: 2, 2: 1}
    assert frequency_lists(input_data) == expected

def test_frequency_lists_sublists_with_single_repeated_element():
    # Scenario: Sublists with single repeated element
    input_data = [[5], [5], [5]]
    expected = {5: 3}
    assert frequency_lists(input_data) == expected