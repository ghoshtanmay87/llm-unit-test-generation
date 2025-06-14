def all_unique(test_list):
    if len(test_list) > len(set(test_list)):
        return False
    return True

import pytest

def test_all_unique_with_all_unique_elements():
    # List with all unique elements
    test_list = [1, 2, 3, 4, 5]
    expected_output = True
    assert all_unique(test_list) == expected_output

def test_all_unique_with_duplicate_elements():
    # List with duplicate elements
    test_list = [1, 2, 2, 3, 4]
    expected_output = False
    assert all_unique(test_list) == expected_output

def test_all_unique_with_empty_list():
    # Empty list
    test_list = []
    expected_output = True
    assert all_unique(test_list) == expected_output

def test_all_unique_with_all_identical_elements():
    # List with all identical elements
    test_list = [7, 7, 7, 7]
    expected_output = False
    assert all_unique(test_list) == expected_output

def test_all_unique_with_unique_strings():
    # List with unique strings
    test_list = ['apple', 'banana', 'cherry']
    expected_output = True
    assert all_unique(test_list) == expected_output

def test_all_unique_with_duplicate_strings():
    # List with duplicate strings
    test_list = ['apple', 'banana', 'apple']
    expected_output = False
    assert all_unique(test_list) == expected_output