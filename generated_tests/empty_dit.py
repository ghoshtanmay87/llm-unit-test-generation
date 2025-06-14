def empty_dit(list1):
 empty_dit=all(not d for d in list1)
 return empty_dit

import pytest

def test_all_dictionaries_empty():
    # Scenario: All dictionaries in the list are empty
    input_data = {'list1': [{}, {}, {}]}
    expected = True
    assert empty_dit(**input_data) == expected

def test_list_contains_non_empty_dictionary():
    # Scenario: List contains at least one non-empty dictionary
    input_data = {'list1': [{}, {'key': 'value'}, {}]}
    expected = False
    assert empty_dit(**input_data) == expected

def test_single_empty_dictionary():
    # Scenario: List contains only one empty dictionary
    input_data = {'list1': [{}]}
    expected = True
    assert empty_dit(**input_data) == expected

def test_single_non_empty_dictionary():
    # Scenario: List contains only one non-empty dictionary
    input_data = {'list1': [{'a': 1}]}
    expected = False
    assert empty_dit(**input_data) == expected

def test_empty_list_input():
    # Scenario: Empty list input
    input_data = {'list1': []}
    expected = True
    assert empty_dit(**input_data) == expected